from django.urls import path

from targets.views import (
    TargetRetrieveUpdateView,
)

urlpatterns = [
    path("target/<uuid:id>/", TargetRetrieveUpdateView.as_view()),
]
