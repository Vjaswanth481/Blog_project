from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import logout_user
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blog.urls')),
    path('', include('users.urls')),

    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('logout/', logout_user, name='logout'),

]

# ✅ THIS LINE FIXES YOUR 404 MEDIA ERROR
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
