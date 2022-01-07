from django.urls import path
from .views import MainList,DeleteW , CustomLoginView, TaskUpdate,MainDetail, TaskCreater
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='log-out'),

    path('', MainList.as_view(), name='main'),
    path('reg/<int:pk>/', MainDetail.as_view(), name='main_det'),
    path('create-task/', TaskCreater.as_view(), name='create'),
    path('task-up/<int:pk>', TaskUpdate.as_view(), name='edit'),
    path('task-d/<int:pk>', DeleteW.as_view(), name='del'),
]