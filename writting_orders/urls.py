from django.urls import path
from . import views
from django.contrib.auth import views as auth_views






urlpatterns = [

    path('', views.Index.as_view(), name="index"),
    path('register/', views.register, name="register"),
    #path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/done-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
    #path('order/', views.OrderCreateView.as_view(), name='order-create'),
    path('create/', views.order_create, name='order-create'),

]