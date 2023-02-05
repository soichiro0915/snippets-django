from django.test import TestCase, Client, RequestFactory
from django.http import HttpRequest
from django.urls import resolve
from django.contrib.auth import get_user_model

from snippetsapp.models import Snippet
from snippetsapp.views import top
from snippetsapp.views import top, snippet_new, snippet_edit, snippet_detail

UserModel = get_user_model()

# Create your tests here.     
class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='test_password'
        )
        self.snippet = Snippet.objects.create(
            title='test_title',
            code='test_code',
            description='test_description',
            created_by=self.user
        )
            
    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)
        
    def test_should_return_username(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)
        
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