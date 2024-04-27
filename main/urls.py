from django.urls import path
from .views import ProtectedView

urlpatterns = [
    path("clouse/",ProtectedView.as_view()),

]

