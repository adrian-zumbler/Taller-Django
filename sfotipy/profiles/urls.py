from django.conf.urls import url
from .views import CreateUserView, LoginUserView

urlpatterns = [
    url(r'^register/',CreateUserView.as_view()),
    url(r'^login/',LoginUserView.as_view()),
]
