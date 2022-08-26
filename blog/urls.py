from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail')
]
