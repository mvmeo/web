from django.urls import path
from .views import HomeView
# from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', HomeView.as_view(template_name='blog/index.html'), name='home'),
]