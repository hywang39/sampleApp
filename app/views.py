from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.serializers import UserSerializer, DepositAccountSerializer, LoanAccountSerializer, UserWithoutAccountSerializer
from django.shortcuts import render
import requests
from django.http import JsonResponse
from app.models import deposit_account, loan_account

from django.views.decorators.csrf import csrf_exempt
#debug use only

import random as ra
from random import randint
# math generator imports

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

from app.serializers import UserSerializer, DepositAccountSerializer, LoanAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        generateDataInput()
        return JsonResponse({'message':(randint(0, 1))})
    return render(request,'test.html')


#This function will generate one random account one each customer with random values
def generateDataInput():
    # randNum = randint(0, 1)
    # custList = []
    # custList.append(User(username='Abagnale', password=make_password('Aba4567890!')))
    # custList.append(User(username='Bloomberg', password=make_password('Blo4567890!')))  
    # custList.append(User(username='Charlies', password=make_password('Cha7890lie!')))
    # custList.append(User(username='DouglasK', password=make_password('Dou3456las7890!')))
    # custList.append(User(username='elainnaW', password=make_password('Ela456ina7890!')))
    # custList.append(User(username='FrancisU', password=make_password('Fra78s9nci0!')))
    # custList.append(User(username='Gillbert', password=make_password('Gil4567890l!')))
    # custList.append(User(username='Hindenburg', password=make_password('Hin456en7890!')))
    # custList.append(User(username='Isabella', password=make_password('Bel45la67890@!')))
    # custList.append(User(username='JohnSnoow', password=make_password('snO34567890!w')))
    # for cust in custList:
        
    #     cust.save()
    

    first_id = User.objects.first().id
    last_id = User.objects.last().id
    
    accountList = []
    for i in range(first_id,last_id + 1):
        num = randint(0, 1)
        if (num==0):
            credit_limit = round(ra.uniform(0.0,1000.0),2)
            current_balance = round(ra.uniform(0.0,credit_limit),2)
            # print('@@@@@@@@@@' + str(credit_limit))
            # print('&&&&&&&&&&' + str(current_balance))
            loan_acc = loan_account(credit_limit=credit_limit,current_balance=current_balance, User_id=i)
            loan_acc.save()
            accountList.append(loan_acc)
        else:
            current_balance = round(ra.uniform(0.0,1000.0),2)
            on_hold=round(ra.uniform(0.0,100.0),2)
            over_draft=round(ra.uniform(0.0,1000.0),2)
            # print('cccccc' + str(current_balance))
            # print('dddddd' + str(on_hold))
            # print('eeeeee' + str(over_draft)) 
            deposit_acc = deposit_account(current_balance= current_balance,
                                                    on_hold=on_hold,
                                                    over_draft=over_draft,
                                                    User_id=i)
            deposit_acc.save()
            accountList.append(deposit_acc)

class UserList(APIView):
    """
    List all Users, or create a new User.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserWithoutAccountSerializer(users, many=True)
        return Response(serializer.data)    

    def post(self, request, format=None):
        serializer = UserWithoutAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a User instance.
    """
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

