from django.urls import path

from cats.views import CatListCreateView

urlpatterns = [
    path("cat", CatListCreateView.as_view()),
]
