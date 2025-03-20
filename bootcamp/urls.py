from django.shortcuts import render
from core.views import home_view, api_view, animal_speak_view
from core.views import PostListView
from django.contrib import admin
from django.urls import path, include
from core.views import create_order_and_items
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),  #ensures admin panel is accessible
    path('', home_view, name= 'home'),  # handles requests to homepage
    path('api/', api_view, name='api_view'),  
    path('animal-speak/', animal_speak_view),
    path('blog/', PostListView.as_view(), name='post_list'),  # call .as_view() for cbvs
    path('api-auth/', include('rest_framework.urls')),
    path('create-order/', create_order_and_items, name='create_order'),
    path("order-success/", lambda request: render(request, "core/order_success.html"), name="order_success"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]

