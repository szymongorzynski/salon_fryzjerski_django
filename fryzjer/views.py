from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from fryzjer.models import User, Visit, Servicee
from fryzjer.serializers import UserSerializer, LoginSerializer, VisitSerializer, VisitAllSerializer, VisitAddSerializer, ServiceeSerializer, RegisterSerializer, ProfileSerializer, UserIdSerializer, VisitStatusSerializer

@csrf_exempt
def getUser(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if (user_data['Name'] != "" or user_data['LastName'] != ""):
            if(User.objects.filter(Name = user_data['Name'], LastName = user_data['LastName'])):
                user = User.objects.filter(Name = user_data['Name'], LastName = user_data['LastName'])
                userid_serializer = UserIdSerializer(user, many = True)
                return JsonResponse(userid_serializer.data, safe = False)
    return JsonResponse("Failed Search", safe = False)

@csrf_exempt
def showUsers(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return JsonResponse(user_serializer.data, safe = False)

@csrf_exempt
def loginApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if (user_data['Email'] != "" or user_data['Pass'] != ""):
            if(User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])):
                user = User.objects.filter(Email = user_data['Email'], Pass = user_data['Pass'])
                profile_serializer = ProfileSerializer(user, many = True)
                return JsonResponse(profile_serializer.data, safe = False)
    return JsonResponse("Failed to Add", safe = False)


@csrf_exempt
def registerApi(request, id=0):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        register_serializer = RegisterSerializer(data = user_data)
        if register_serializer.is_valid():
            register_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)


@csrf_exempt
def visitApi(request, id=0):
    if request.method == 'GET':
        visit = Visit.objects.filter(userr=id, Status='N')
        visit_serializer = VisitSerializer(visit, many = True)
        return JsonResponse(visit_serializer.data, safe = False)

    elif request.method == 'POST':
        visit_data = JSONParser().parse(request)
        visit_add_serializer = VisitAddSerializer(data = visit_data)
        if visit_add_serializer.is_valid():
            visit_add_serializer.save()
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
def visitApiW(request, id=0):
     if request.method == 'GET':
        visit = Visit.objects.filter(userr=id, Status='W')
        visit_serializer = VisitSerializer(visit, many = True)
        return JsonResponse(visit_serializer.data, safe = False)


@csrf_exempt
def serviceeApi(request, id=0):
    if request.method == 'GET':
        servicee = Servicee.objects.all()
        servicee_serializer = ServiceeSerializer(servicee, many = True)
        return JsonResponse(servicee_serializer.data, safe = False)

# później nie potrzebne
    elif request.method == 'POST':
        servicee_data = JSONParser().parse(request)
        servicee_serializer = ServiceeSerializer(data = servicee_data)
        if servicee_serializer.is_valid():
            servicee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe = False)

@csrf_exempt
def visitAllApi(request):
    if request.method == 'GET':
        visit = Visit.objects.filter(Status='N')
        visit_serializer = VisitAllSerializer(visit, many = True)
        return JsonResponse(visit_serializer.data, safe = False)

