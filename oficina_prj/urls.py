from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/cliente/', views.signup_cliente, name='signup_cliente'),
    path('cadastro/oficina/', views.signup_oficina, name='signup_oficina'),
    
    path('painel/cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('painel/oficina/', views.dashboard_oficina, name='dashboard_oficina'),
    
    path('servico/<int:pk>/pegar/', views.pegar_servico, name='pegar_servico'),
    path('servico/<int:pk>/concluir/', views.concluir_servico, name='concluir_servico'),
]

# Serve arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)