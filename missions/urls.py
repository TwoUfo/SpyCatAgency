from django.urls import path

from missions.views import MissionListCreateView, MissionRetrieveUpdateDestroyView

urlpatterns = [
    path("mission", MissionListCreateView.as_view()),
    path("mission/<uuid:id>", MissionRetrieveUpdateDestroyView.as_view()),
]
