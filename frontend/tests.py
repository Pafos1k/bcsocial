"""Smoke checks for the prototype's rendering and intentionally static boundary."""
from html.parser import HTMLParser

from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


SCREENS = [
    ("landing", "accounts/landing.html"),
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


class PrototypeScreensTests(SimpleTestCase):
    # SimpleTestCase forbids database queries: these pages must stay independent.
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
                self.assertEqual(self.client.get(link).status_code, 200)

    def test_screens_do_not_accept_post_requests(self):
        for name, _ in SCREENS:
            with self.subTest(screen=name):
                self.assertEqual(self.client.post(reverse(name), {}).status_code, 405)
