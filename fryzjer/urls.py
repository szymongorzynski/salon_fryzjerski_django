from fryzjer import views
from django.urls import path

urlpatterns = [

    #rejestracja użytkownika
    path('registerlogin', views.registerLoginApi), #tutaj login i hasło postem a dostajesz id usera i email
    path('register', views.registerApi), #tutaj resztę danych klienta  postem + id które dostałeś wyżej

    #logowanie
    path('login', views.loginApi),
    path('auth', views.profileApi),


    #zniżki
    path('discount', views.discountApi), #Post dodawanie, Get wyświtlenie wszystkich sprawdzić tego geta!!
    path('discount/<int:id>', views.discountApi), #put zmiana np. ilości wizyt lub procentów, delete usunięcie

    #Usługi
    path('servicee', views.serviceeApi), #Post dodawanie, Get wyświtlenie wszystkich sprawdzić tego geta!!
    path('servicee/<int:id>', views.serviceeApi), #put zmiana np. nazwy, ceny, czasu, delete usunięcie

    #Dodanie niezarejestrowanego użytkownika
    path('customerunr', views.customerUnRApi), #Zwraca CustomerId a jak trzeba to go tworzy

    #Wizyty
    path('visit', views.visitApi),#dodawanie, usuwanie, zmiana statusu
    path('visit/<int:id>/', views.visitApi),

    #Wizyty wyświetlanie przyszłych
    path('nextvisit', views.nextVisitApi),

    #Wizyty wykonane
    #path('visitW', views.visitApiW),
    path('visitW/<int:id>/', views.visitApiW),

    #Wyświetlenie wizyt dla pracownika
    path('vall', views.visitAllApi),

    # path('checkdate', views.checkdateApi),

]
