"""Smoke checks for the prototype screens and bc.edu-only Google sign-in."""
from html.parser import HTMLParser

from django.contrib.staticfiles import finders
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .adapters import is_allowed_google_account


SCREENS = [
    ("accounts:edit", "accounts/profile_edit.html"),
    ("accounts:profile", "accounts/profile.html"),
    ("home", "core/home.html"),
    ("clubs:index", "clubs/index.html"),
    ("community", "clubs/community.html"),
    ("connections:index", "connections/index.html"),
    ("messaging:inbox", "messaging/inbox.html"),
    ("messaging:individual", "messaging/individual.html"),
    ("messaging:club", "messaging/club.html"),
    ("messaging:marketplace", "messaging/marketplace.html"),
    ("events:index", "events/index.html"),
    ("events:detail", "events/detail.html"),
    ("events:create", "events/create.html"),
    ("marketplace:index", "marketplace/index.html"),
    ("marketplace:create", "marketplace/create.html"),
    ("news:index", "news/index.html"),
]


class PageReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = set()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        source = attrs.get("src") if tag == "img" else attrs.get("href")
        if source and source.startswith("/static/"):
            self.assets.add(source.removeprefix("/static/"))
        if tag == "a" and source and source.startswith("/"):
            self.links.add(source)


class PrototypeScreensTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "eagle", "eagle@bc.edu", first_name="Baldwin", last_name="Eagle")
        self.client.force_login(self.user)

    def test_all_screens_render_with_resolvable_assets_and_links(self):
        links = set()
        for name, template in SCREENS:
            with self.subTest(screen=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)
                parser = PageReferences()
                parser.feed(response.content.decode())
                self.assertIn("vendor/bootstrap/bootstrap.min.css", parser.assets)
                self.assertIn("core/css/styles.css", parser.assets)
                for asset in parser.assets:
                    self.assertIsNotNone(finders.find(asset), asset)
                links.update(parser.links)
        for link in links:
            with self.subTest(link=link):
                # The landing page sends signed-in students on to home.
                self.assertIn(self.client.get(link).status_code, (200, 302))

    def test_screens_do_not_accept_post_requests(self):
        for name, _ in SCREENS:
            with self.subTest(screen=name):
                self.assertEqual(self.client.post(reverse(name), {}).status_code, 405)

    def test_profile_shows_signed_in_student(self):
        response = self.client.get(reverse("accounts:profile"))
        self.assertContains(response, "Baldwin Eagle")
        self.assertContains(response, "eagle@bc.edu")


class SignInRequiredTests(TestCase):
    def test_landing_is_public_and_links_to_google(self):
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/accounts/google/login/")

    def test_app_pages_redirect_signed_out_visitors_to_landing(self):
        for name, _ in SCREENS:
            with self.subTest(screen=name):
                response = self.client.get(reverse(name))
                self.assertRedirects(response, f"{reverse('landing')}?next={reverse(name)}",
                                     fetch_redirect_response=False)


class BCEmailRuleTests(TestCase):
    def claims(self, email, hd="bc.edu", verified=True):
        return {"email": email, "hd": hd, "email_verified": verified}

    def test_verified_bc_edu_account_is_allowed(self):
        self.assertTrue(is_allowed_google_account(self.claims("eagle@bc.edu")))
        self.assertTrue(is_allowed_google_account(self.claims("Eagle@BC.EDU")))

    def test_other_accounts_are_rejected(self):
        for claims in [
            self.claims("someone@gmail.com", hd=None),
            self.claims("eagle@notbc.edu", hd="notbc.edu"),
            self.claims("eagle@bc.edu.evil.com", hd="bc.edu.evil.com"),
            self.claims("eagle@bc.edu", verified=False),
            self.claims("eagle@bc.edu", hd=None),
            {},
        ]:
            with self.subTest(claims=claims):
                self.assertFalse(is_allowed_google_account(claims))
