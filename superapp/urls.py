from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create/', views.add_items, name='add-items'),
	path('all/', views.view_items, name='view_items'),
	path('update/<int:pk>/', views.update_items, name='update-items'),
	path('delete/<int:pk>/', views.delete_items, name='delete-items'),
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
	path('basic/', views.API_objects.as_view()),
    path('basic/<int:pk>/', views.API_objects_details.as_view()),
]
