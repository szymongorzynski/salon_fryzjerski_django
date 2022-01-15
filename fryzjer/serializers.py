from rest_framework import serializers
from fryzjer.models import User, Visit, Servicee


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Name')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Email', 'Pass')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email', 'Name', 'LastName')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email', 'Pass', 'Name', 'LastName', 'Phone')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email', 'Pass', 'Name', 'LastName', 'Phone')

class ServiceeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Servicee
       fields = ('ServiceeId', 'Name', 'Price', 'Time')

class VisitSerializer(serializers.ModelSerializer):
    
    # service = serializers.SerializerMethodField('x')

    # def x(self, obj):
    #     y = getattr(obj, 'Name')
    #     return y

    class Meta:
       model = Visit
       fields = ('VisitId', 'UserId', 'ServiceeId', 'Ddate', 'Hhour', 'Status')
