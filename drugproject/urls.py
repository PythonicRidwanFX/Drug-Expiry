"""
URL configuration for drugproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_view
from dashboard import views as dashboard_view
from django.conf import settings
from django.conf.urls.static import static

## Drug Expiry Alert scheduler
import schedule
import time
from dashboard.task import send_expiring_notification
from threading import Thread

def start_alert_thread():
    schedule.every(2).minutes.do(send_expiring_notification)
    
    while True:
        schedule.run_pending()
        time.sleep(2)

mail_thread = Thread(target=start_alert_thread)
mail_thread.start()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', user_view.register, name='user-register'),
    path('profile/', user_view.profile, name='user-profile'),
    path('profile/update/', user_view.profile_update, name='user-profile-update'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
