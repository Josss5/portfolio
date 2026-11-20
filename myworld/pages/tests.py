import json

from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage
from .portfolio_data import HERO, PROFILE, PROJECTS


class HomePageTests(TestCase):
    def test_home_renders(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_personalized_sections_and_projects_render(self):
        response = self.client.get(reverse("home"))
        for anchor in ("id=\"about\"", "id=\"skills\"", "id=\"projects\"", "id=\"leadership\"", "id=\"contact\""):
            self.assertContains(response, anchor)
        self.assertContains(response, PROFILE["full_name"])
        self.assertContains(response, HERO["headline"])
        for project in PROJECTS:
            self.assertContains(response, project["name"])

    def test_static_files_are_cache_busted(self):
        html = self.client.get(reverse("home")).content.decode()
        self.assertRegex(html, r'site/css/site\.css\?v=\d+')
        self.assertRegex(html, r'site/js/site\.js\?v=\d+')


class ContactTests(TestCase):
    def post(self, data):
        return self.client.post(reverse("contact"), json.dumps(data), content_type="application/json")

    def test_valid_message_is_saved(self):
        response = self.post({"name": "Ana", "email": "ana@example.com", "message": "Hello!"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_invalid_email_rejected(self):
        response = self.post({"name": "Ana", "email": "nope", "message": "Hello!"})
        self.assertEqual(response.status_code, 400)

    def test_honeypot_is_ignored(self):
        response = self.post({"name": "Bot", "email": "b@example.com", "message": "spam", "website": "x"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
