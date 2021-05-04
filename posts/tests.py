from django.test import TestCase
from .models import Posts
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Posts.objects.create(text="Just a test")

    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_obj_name = f"{post.text}"
        self.assertEqual(expected_obj_name, "Just a test")

class HomePageViewTest(TestCase):
    def setUp(self):
        Posts.objects.create(text="This is another test")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
# Create your tests here.
