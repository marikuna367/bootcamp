from django.urls import path
from core.views import home_view, api_view, animal_speak_view
from core.views import PostListView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # This ensures the admin panel is accessible
    path('', home_view),  # Handles requests to the homepage
    path('api/', api_view),  
    path('animal-speak/', animal_speak_view),
    path('blog/', PostListView.as_view()),  # Call .as_view() for CBVs
]
