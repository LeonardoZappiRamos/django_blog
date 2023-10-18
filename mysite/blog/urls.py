from django.urls import path

from .views import PostView

urlpatterns = [
    path('home', PostView.as_view(), name='home'),
    path('<slug:slug>/', PostView.as_view(), name='post_detail')
]
