from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_list, name='home'),
    path("search/", views.search, name="search_results"),           # Поиск
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Подробности объявления
    path('account/', views.account, name='account')                 # Личный кабинет пользователя
]
