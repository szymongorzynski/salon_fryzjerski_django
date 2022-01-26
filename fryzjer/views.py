from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# from fryzjer.models import User, Visit, Servicee
# from fryzjer.serializers import UserSerializer, LoginSerializer, VisitSerializer, ServiceeSerializer, RegisterSerializer, ProfileSerializer, UserIdSerializer, VisitStatusSerializer,  VisitNewSerializer

from fryzjer.models import User, Visit, Servicee, Customer, Employee, Discount
from fryzjer.serializers import UserSerializer, CustomerSerializer, EmployeeSerializer, DiscountSerializer, ServiceeSerializer, EmployeeServiceeSerializer, VisitSerializer, UserIdSerializer, VisitUnRSerializer, CustomerUnRSerializer, VisitStatusSerializer

#Rejestracja użytkownika
@csrf_exempt
def registerLoginApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        register_serializer = UserSerializer(data = user_data)
        if register_serializer.is_valid():
            register_serializer.save()
            user = User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])
            userid_serializer = UserIdSerializer(user, many = True)
            return JsonResponse(userid_serializer.data, safe = False)
        return JsonResponse("Failed to Add", safe = False)


@csrf_exempt
def registerApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        register_serializer = CustomerSerializer(data = user_data)
        if register_serializer.is_valid():
            register_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)

#Logowanie
@csrf_exempt
def loginApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if (user_data['Email'] != "" or user_data['Pass'] != ""):
            if(User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])):
                user = User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])
                user_serializer = UserIdSerializer(user,  many = True)
                return JsonResponse(user_serializer.data, safe = False)
    return JsonResponse("Failed to Add", safe = False)

@csrf_exempt
def profileApi(request, id=0):
    if request.method == 'POST':
        user = JSONParser().parse(request)
        profile = Customer.objects.filter(UserId = user['UserId'])
        profile_serializer = CustomerSerializer(profile, many = True)
        return JsonResponse(profile_serializer.data, safe = False)

#Dodawanie, zmiana, usuwanie zniżki
@csrf_exempt
def discountApi(request, id=0):
    if request.method == 'GET':
        discount = Discount.objects.all()
        discount_serializer = DiscountSerializer(discount, many = True)
        return JsonResponse(discount_serializer.data, safe = False)

    elif request.method == 'POST':
        discount_data = JSONParser().parse(request)
        discount_serializer = DiscountSerializer(data = discount_data)
        if discount_serializer.is_valid():
            discount_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)

    elif request.method == 'PUT':
        discount_data = JSONParser().parse(request)
        discount = Discount.objects.get(DiscountId = id)
        discount_serializer = DiscountSerializer(discount, data = discount_data)
        if discount_serializer.is_valid():
            discount_serializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update.", safe = False)

    elif request.method=='DELETE':
        discount = Discount.objects.get(DiscountId=id)
        discount.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

#Dodawanie, zmiana, usuwanie usługi
@csrf_exempt
def serviceeApi(request, id=0):
    if request.method == 'GET':
        servicee = Servicee.objects.all()
        servicee_serializer = ServiceeSerializer(servicee, many = True)
        return JsonResponse(servicee_serializer.data, safe = False)

    elif request.method == 'POST':
        servicee_data = JSONParser().parse(request)
        servicee_serializer = ServiceeSerializer(data = servicee_data)
        if servicee_serializer.is_valid():
            servicee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)

    elif request.method == 'PUT':
        servicee_data = JSONParser().parse(request)
        servicee = Servicee.objects.get(ServiceeId = id)
        servicee_serializer = ServiceeSerializer(servicee, data = servicee_data)
        if servicee_serializer.is_valid():
            servicee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update.", safe = False)

    elif request.method=='DELETE':
        servicee = Servicee.objects.get(ServiceeId=id)
        servicee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# nowa wizyta osób niezarejestrowanych w salonie i zarejestrowanych
@csrf_exempt
def customerUnRApi(request, id=0):
    if request.method == 'GET':
        customer = Customer.objects.all()
        customer_serializer = CustomerSerializer(customer, many = True)
        return JsonResponse(customer_serializer.data, safe = False)

    #dodanie i wysłanie id klienta lub poszukanie i wysłanie jeśli nie istnieje
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerUnRSerializer(data = customer_data)
        if(Customer.objects.filter(Phone = customer_data['Phone'])):
            customer = Customer.objects.filter(Phone = customer_data['Phone'])
            custom_serializer = CustomerSerializer(customer,  many = True)
            return JsonResponse(custom_serializer.data, safe = False)
        elif customer_serializer.is_valid():
            customer_serializer.save()
            customer = Customer.objects.filter(Phone = customer_data['Phone'])
            custom_serializer = CustomerSerializer(customer,  many = True)
            return JsonResponse(custom_serializer.data, safe = False)
        return JsonResponse("Failed to Add", safe = False)

#obsługa wizyt
@csrf_exempt
def visitApi(request, id=0):
    if request.method == 'GET':
        visits = Visit.objects.filter(Customerr = id)
        visit_serializer = VisitSerializer(visits, many = False)
        return JsonResponse(visit_serializer.data, safe=False)


    elif request.method == 'POST':
        visit_data = JSONParser().parse(request)
        visit_serializer = VisitUnRSerializer(data = visit_data)
        if visit_serializer.is_valid():
            visit_serializer.save()
            return JsonResponse("Visit Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)

    elif request.method=='DELETE':
        visit = Visit.objects.get(VisitId=id)
        visit.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

    elif request.method == 'PUT':
        visit_data = JSONParser().parse(request)
        visit = Visit.objects.get(VisitId = id)
        visit_serializer = VisitStatusSerializer(visit, data = visit_data)
        if visit_serializer.is_valid():
            visit_serializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update.", safe = False)

@csrf_exempt
def nextVisitApi(request, id=0):
    user = JSONParser().parse(request)
    if request.method == 'POST':
        visit = Visit.objects.filter(Customerr=user['CustomerId'], Status='N')
        visit_serializer = VisitSerializer(visit, many = True)
        return JsonResponse(visit_serializer.data, safe = False)


#wyświetlanie Wykonanych wizyt danego klienta
@csrf_exempt
def visitApiW(request, id=0):
     if request.method == 'GET':
        visit = Visit.objects.filter(Customerr=id, Status='W')
        visit_serializer = VisitSerializer(visit, many = True)
        return JsonResponse(visit_serializer.data, safe = False)

#Wyświetlenie dla pracownika
@csrf_exempt
def visitAllApi(request, id=0):
    if request.method == 'GET':
        visit = Visit.objects.filter(Status='N')
        visit_serializer = VisitSerializer(visit, many = True)
        return JsonResponse(visit_serializer.data, safe = False)


# @csrf_exempt
# def checkdateApi(request):
#     date = JSONParser().parse(request)
#     if request.method == 'POST':
#         if(Visit.objects.filter(Ddate = date['Ddate'])):
#             return JsonResponse("Invalid", safe = False)
#         return JsonResponse("Valid".data, safe = False)
