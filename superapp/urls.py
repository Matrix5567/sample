from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create/', views.add_items, name='add-items'),
	path('all/', views.view_items, name='view_items'),
	path('update/<int:pk>/', views.update_items, name='update-items'),
	path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
