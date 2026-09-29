"""GET-only prototype pages; feature templates keep stable, feature-owned paths."""
from django.shortcuts import render
from django.views.decorators.http import require_GET
from . import sample_data as samples


def _page(request, template, title, section, **context):
    return render(request, template, {"title": title, "section": section, **context})


@require_GET
def landing(request):
    return _page(request, "accounts/landing.html", "Welcome", "landing")


@require_GET
def profile(request):
    return _page(request, "accounts/profile.html", "Profile", "profile", profile=samples.PROFILE)


@require_GET
def profile_edit(request):
    return _page(request, "accounts/profile_edit.html", "Edit Profile", "profile", profile=samples.PROFILE)


@require_GET
def home(request):
    return _page(request, "core/home.html", "Home", "home", people=samples.SUGGESTED_PEOPLE)


@require_GET
def clubs(request):
    return _page(request, "clubs/index.html", "Clubs", "clubs", groups=samples.CLUBS, officers=samples.EBOARD)


@require_GET
def community(request):
    return _page(request, "clubs/community.html", "Community", "community", groups=samples.COMMUNITIES)


@require_GET
def connections(request):
    return _page(request, "connections/index.html", "Connections", "connections", people=samples.CONNECTIONS)


@require_GET
def messages(request):
    return _page(request, "messaging/inbox.html", "Messages", "messages", people=samples.CONNECTIONS[:2])


@require_GET
def message_individual(request):
    return _page(request, "messaging/individual.html", "Jack Mullen", "messages", conversation=samples.CONVERSATIONS["individual"])


@require_GET
def message_club(request):
    return _page(request, "messaging/club.html", "CS Club — Fall Hackathon", "messages", conversation=samples.CONVERSATIONS["club"])


@require_GET
def message_marketplace(request):
    return _page(request, "messaging/marketplace.html", "Mini-Fridge conversation", "messages", conversation=samples.CONVERSATIONS["marketplace"])


@require_GET
def events(request):
    return _page(request, "events/index.html", "Events", "events", club_events=samples.CLUB_EVENTS, campus_events=samples.CAMPUS_EVENTS)


@require_GET
def event_detail(request):
    return _page(request, "events/detail.html", "Events", "events", people=samples.CONNECTIONS)


@require_GET
def event_create(request):
    return _page(request, "events/create.html", "Events", "events")


@require_GET
def marketplace(request):
    return _page(request, "marketplace/index.html", "Marketplace", "marketplace", listings=samples.LISTINGS)


@require_GET
def listing_create(request):
    return _page(request, "marketplace/create.html", "Marketplace", "marketplace")


@require_GET
def news(request):
    return _page(request, "news/index.html", "News", "news", bc_news=samples.BC_NEWS, today_news=samples.TODAY_NEWS)
