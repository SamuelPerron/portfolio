from django.db import models


class Position(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=6, blank=False, null=False)
    exchange = models.ForeignKey(
        'positions.Exchange', 
        on_delete=models.SET_NULL, 
        null=True
    )
    allocation = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.account} - {self.exchange}.{self.symbol}'


class Exchange(models.Model):
    name = models.CharField(max_length=255, blank=False)
    label = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.label
