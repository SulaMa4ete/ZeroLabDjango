from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from datetime import date

def home_template(request):
    return render(request, 'home.html', {'today': date.today()})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_template),
]