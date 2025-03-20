from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
#from core.utils import fetch_data
from core.animals import Dog, Cat
from django.db import transaction
from .models import Order, OrderItem

def home_view(request):
    return render(request, "core/home.html")

def api_view(request):
    data = {
        "message": "Welcome to Django Bootcamp API!",
        "status": "success"
    }
    return render(request, 'core/api.html', {'data': data})

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


@transaction.atomic
def create_order_and_items(request):
    if request.method == "POST":
        order_data = {
            "customer_name": request.POST.get("customer_name")
        }
        items_data = [
            {"product_name": request.POST.get("product_name"), "quantity": int(request.POST.get("quantity"))}
        ]

        try:
            order = Order.objects.create(**order_data)
            for item in items_data:
                if item.get("quantity", 0) <= 0:
                    raise ValueError("Quantity must be greater than zero!")
                OrderItem.objects.create(order=order, **item)
            return redirect("order_success")
        except Exception as e:
            return render(request, "core/order_error.html", {"error": str(e)})

    return render(request, "core/create_order.html")
