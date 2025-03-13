from django.urls import path
from core.views import home_view, api_view, animal_speak_view
from core.views import PostListView
urlpatterns = [
    path('', home_view),
    path('api/', api_view),
    path('animal-speak/', animal_speak_view),
]
urlpatterns = [
    path('blog/', PostListView.as_view()),  # call .as_view() for CBVs
]
