"""Move each namespace to its future app without changing template links."""
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", views.home, name="home"),
    path("profile/", include(([
        path("", views.profile, name="profile"),
        path("edit/", views.profile_edit, name="edit"),
    ], "accounts"))),
    path("clubs/", include(([path("", views.clubs, name="index")], "clubs"))),
    path("community/", views.community, name="community"),
    path("connections/", include(([path("", views.connections, name="index")], "connections"))),
    path("messages/", include(([
        path("", views.messages, name="inbox"),
        path("individual/", views.message_individual, name="individual"),
        path("club/", views.message_club, name="club"),
        path("marketplace/", views.message_marketplace, name="marketplace"),
    ], "messaging"))),
    path("events/", include(([
        path("", views.events, name="index"),
        path("fall-concert/", views.event_detail, name="detail"),
        path("new/", views.event_create, name="create"),
    ], "events"))),
    path("marketplace/", include(([
        path("", views.marketplace, name="index"),
        path("new/", views.listing_create, name="create"),
    ], "marketplace"))),
    path("news/", include(([path("", views.news, name="index")], "news"))),
]
