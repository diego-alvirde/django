from django.contrib import admin
from django.urls import path
from . import views
from products.views import ProductListView
from django.urls import include

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/register', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls'))
]
