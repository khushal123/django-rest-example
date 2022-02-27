from .views import UserDetailsView, UserView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", UserView.as_view(), name="user-view"),
    path("<int:id>", UserDetailsView.as_view(), name="user-details")
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)