from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post

def home_view(request):
    return HttpResponse("Hello, Django Bootcamp!")

def api_view(request):
    data = {
        "message": "Welcome to Django Bootcamp API!",
        "status": "success"
    }
    return JsonResponse(data)

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'core/post_list.html', {'posts': posts})