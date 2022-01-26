from rest_framework import serializers
from fryzjer.models import User, Visit, Servicee, Employee, Discount, Customer

#Tworzenie usera
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email','Pass')

#Rejestracja klienta (pobranie id usera)
class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email')

#Tworzenie klienta
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
       model = Customer
       fields = ('CustomerId', 'UserId', 'Name', 'LastName', 'Phone')

#Tworzenie pracownika
class EmployeeSerializer(serializers.ModelSerializer):
    Userr = UserSerializer(many=False)

    class Meta:
       model = Employee
       fields = ('EmployeeId', 'Userr', 'Name', 'LastName', 'Pesel', 'Town', 'HouseNumber', 'Salary', 'Phone')

#Zniżka
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
       model = Discount
       fields = ('DiscountId', 'Percent', 'VisitCount')

#Usługa
class ServiceeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Servicee
       fields = ('ServiceeId', 'Name', 'Price', 'Time')

#Pracownik do wizyty
class EmployeeServiceeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Employee
       fields = ('EmployeeId', 'Name', 'LastName')

#potrzebne do wyświetlania wizyt i innych informacji z nię związanych
class VisitSerializer(serializers.ModelSerializer):

    servicee = ServiceeSerializer(many=False)
    Employeee = EmployeeServiceeSerializer(many=False)
    Customerr = CustomerSerializer(many=False)

    class Meta:
       model = Visit
       fields = ('VisitId', 'Customerr', 'Employeee', 'Ddate', 'Hhour', 'Status', 'servicee')


#potrzebne do dodania klienta bez konta
class CustomerUnRSerializer(serializers.ModelSerializer):

    class Meta:
       model = Customer
       fields = ( 'Name','LastName', 'Phone')

#potrzebne do dodania wizyty
class VisitUnRSerializer(serializers.ModelSerializer):

    class Meta:
       model = Visit
       fields = ('VisitId', 'Customerr', 'servicee', 'Employeee', 'DiscountId', 'Ddate', 'Hhour', 'Status', )

#potrzebne do zmiany statusu wizyty
class VisitStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('VisitId', 'Status')
