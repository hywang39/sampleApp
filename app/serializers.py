from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from app.models import customer, deposit_account, loan_account
from app.models import deposit_account, loan_account


class DepositAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = deposit_account
        fields = ('id', 'current_balance', 'over_draft','on_hold','User_id')

class LoanAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = loan_account
        fields = ('id', 'current_balance', 'credit_limit','User_id')

class UserSerializer(serializers.ModelSerializer):
    deposit_account = DepositAccountSerializer(many=True, read_only=True)
    loan_account = LoanAccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','deposit_account','loan_account')
# This is the serializer with all information for customers, used to retreive detail info of one customer

class UserWithoutAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
# This is the serializer without account info, used to retrieve authentication info of all customers