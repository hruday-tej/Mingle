# from django.contrib import admin
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

app_name = 'profiles'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.home_view, name='home_view')
    path('myprofile', views.my_profile_view, name='my-profile-view')
]