from django.urls import path

from .views import (AgentListAPIview, GetProfileAPIView, TopAgentsListAPIView,
                    UpdateProfileAPIView)

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update-profile"
    ),
    path("agents/all/", AgentListAPIview.as_view(), name="all-agents"),
    path("top-agents/all/", TopAgentsListAPIView.as_view(), name="top-agents"),
]
