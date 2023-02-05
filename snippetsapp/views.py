from django.shortcuts import render
from django.http import HttpResponse
from snippetsapp.models import Snippet

# Create your views here.
def top(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/top.html', context)

def snippet_new(request):
    return HttpResponse("snippet_new")

def snippet_edit(request, snippet_id):
    return HttpResponse("snippet_edit")

def snippet_detail(request, snippet_id):
    return HttpResponse("snippet_detail")