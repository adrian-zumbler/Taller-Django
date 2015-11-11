from django.conf.urls import url
from .views import CreateUserView

urlpatterns = [
    url(r'^register/',CreateUserView.as_view()),
]
