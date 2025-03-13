from django.urls import path
from core.views import home_view
from core.views import api_view
from core.views import post_list_view
urlpatterns = [
    path('', home_view),
]
urlpatterns += [
    path('api/', api_view),
]

urlpatterns += [
    path('blog/', post_list_view),
]