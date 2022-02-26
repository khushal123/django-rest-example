from .views import UserDetailsView, UserView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", UserView.as_view()),
    path("<int:id>", UserDetailsView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)