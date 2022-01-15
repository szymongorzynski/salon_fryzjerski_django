from fryzjer import views
from django.urls import path

urlpatterns = [

    # dla testów
    path('show', views.showUsers),

    path('user', views.getUser),

    path('register', views.registerApi),
    path('login', views.loginApi),
    
    path('visit', views.visitApi),
    path('visitW', views.visitApiW),
    path('visit/<int:id>/', views.visitApi),
    path('visitW/<int:id>/', views.visitApiW),
    path('servicee', views.serviceeApi),
    path('servicee/<int:id>', views.serviceeApi)
]
