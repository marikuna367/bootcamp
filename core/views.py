from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from core.utils import fetch_data
from core.animals import Dog, Cat

def home_view(request):
    return HttpResponse("Hello, Django Bootcamp!")

def api_view(request):
    data = {
        "message": "Welcome to Django Bootcamp API!",
        "status": "success"
    }
    return JsonResponse(data)

#def post_list_view(request):
 #   return JsonResponse({"posts": fetch_data(Post)})

def animal_speak_view(request):
    dog = Dog()
    cat = Cat()

    # i am using polymorphism to call speak() on both objects
    response = {
        "dog_says": dog.speak(),
        "cat_says": cat.speak()
    }

    return JsonResponse(response)

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'core/post_list.html', {'posts': posts})


