from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('add/', views.add, name='add_api'),
    # path('add/addrecord/', views.addrecord, name='addrecord_api'),
    # path('delete/<int:id>', views.delete, name='delete_api'),
    # path('update/<int:id>', views.update, name='update_api'),
    # path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout, name='logout'),

]
