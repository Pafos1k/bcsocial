"""Server-side enforcement that only verified bc.edu Google accounts can sign in."""
from allauth.core.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect


def is_allowed_google_account(extra_data):
    """True only for a Google-verified address exactly on the allowed domain."""
    domain = settings.ALLOWED_EMAIL_DOMAIN
    email = (extra_data.get("email") or "").strip().lower()
    verified = extra_data.get("email_verified") in (True, "true")
    # Compare the part after the last "@" so "x@notbc.edu" or "x@bc.edu.evil.com" fail.
    return verified and email.rpartition("@")[2] == domain and extra_data.get("hd") == domain


class BCSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if not is_allowed_google_account(sociallogin.account.extra_data):
            messages.error(request, "Please sign in with your @bc.edu Google account.")
            raise ImmediateHttpResponse(redirect("landing"))

    def is_open_for_signup(self, request, sociallogin):
        return is_allowed_google_account(sociallogin.account.extra_data)
