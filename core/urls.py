from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "api/",
        include(
            [
                path("", include("cats.urls")),
                path("", include("missions.urls")),
                path("", include("targets.urls")),
            ],
        ),
    ),
]
