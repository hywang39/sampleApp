from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=20) 

#     class Meta:
#         app_label = 'app'
#         db_table = 'customer'


class deposit_account(models.Model):
    id = models.AutoField(primary_key=True)
    current_balance = models.DecimalField(decimal_places=2, max_digits=20)
    over_draft = models.DecimalField(decimal_places=2, max_digits=20)
    on_hold = models.DecimalField(decimal_places=2, max_digits=20)
    User = models.ForeignKey(
        User,
        related_name='deposit_account',
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = 'app'
        db_table = 'deposit_account'


class loan_account(models.Model):
    id = models.AutoField(primary_key=True)
    current_balance = models.DecimalField(decimal_places=2, max_digits=20)
    credit_limit = models.DecimalField(decimal_places=2, max_digits=20)
    User = models.ForeignKey(
        User,
        related_name='loan_account',
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = 'app'
        db_table = 'loan_account'
