from django.urls import path
from . import views
from .views import export_subscriptions_xls

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:sub_id>', views.cv_detail, name='cv_detail'),
    path('subscription/', views.subscription, name='subscription'),
    path('subscription/done/', views.subscription_done, name='subscription_done'),
    path('admin/export-subscriptions/', export_subscriptions_xls, name='export_subscriptions_xls'),
]
