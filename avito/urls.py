from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_list, name='home'),
    path("search/", views.search, name="search_results"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
