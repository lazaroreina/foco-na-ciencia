from django.urls.conf import path
from . import views

urlpatterns = [
    path('board', views.board, name='board'),
]