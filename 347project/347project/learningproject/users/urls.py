from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile_update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('terms_conditions/', views.TermsConditions.as_view(), name='terms_conditions'),
    path('privacy/', views.Privacy.as_view(), name='privacy'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('help/helpdescribe/', views.HelpDescribe.as_view(), name='help_describe'),
    path('contact/', views.contact, name='contact_us'),


]

