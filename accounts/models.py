from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    source = models.ForeignKey('AccountSource', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} at {self.source}'


class AccountSource(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
