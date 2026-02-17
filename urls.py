from django.contrib import admin
from django.urls import path
from myapp import views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL shows the home view
]
