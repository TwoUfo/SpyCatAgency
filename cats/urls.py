from django.urls import path

from cats.views import CatListCreateView, CatRetrieveUpdateDestroyView

urlpatterns = [
    path("cat", CatListCreateView.as_view()),
    path("cat/<uuid:id>", CatRetrieveUpdateDestroyView.as_view()),
]
