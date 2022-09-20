from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns
#<str:pk>

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('book_manager', views.book_manager, name='book_manager'),

    # APIS
    path('api/users/list/', views.UserList.as_view()),
    path('api/users/detail/', views.UserDetailAPI.as_view()),

    path('api/books/', views.BookList.as_view()),
    path('api/books/<int:pk>', views.BookDetailAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
