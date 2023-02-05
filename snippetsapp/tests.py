from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve

from snippetsapp.views import top, snippet_new, snippet_edit, snippet_detail

# Create your tests here.     
class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")
        
class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve("/snippets/new/")
        self.assertEqual(found.func, snippet_new)
        
class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(found.func, snippet_edit)
        
class DetailSnippetTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/")
        self.assertEqual(found.func, snippet_detail)