from django.urls import path
from . import views
app_name = 'accounts'
 
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('all/',views.ShowProfiles.as_view() , name='all-profiles'),
    path('customers/',views.ShowCustomers.as_view() , name='all-customers'),
    path('managers/',views.ShowManagers.as_view() , name='all-managers'),
    path('profile-update/<int:pk>/', views.UpdateProfiles.as_view(), name='profile-update'),
    path('profile-show/<int:pk>/', views.ShowProfile.as_view(), name='profile-detail'),
]