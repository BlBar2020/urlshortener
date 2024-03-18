from django.urls import path
from shortener import views  # Make sure to import the views

# Define the URL patterns
urlpatterns = [
    # The path for the index page that will show the URL shortening form
    path('', views.index, name='index'),  
    # The path for handling short URLs and redirecting to the original long URL
    path('<str:short_url>/', views.redirect_view, name='redirect_view'),  
]
