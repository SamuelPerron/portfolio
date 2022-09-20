from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    source = models.ForeignKey('AccountSource', null=True, on_delete=models.SET_NULL)

    def get_total_nb_shares(self):
        raise NotImplementedError()

    def get_amount_invested(self):
        raise NotImplementedError()

    def get_investment_value(self):
        raise NotImplementedError()

    def get_returns(self):
        raise NotImplementedError()

    def get_day_pl(self):
        raise NotImplementedError()

    def invest(self):
        raise NotImplementedError()

    def __str__(self):
        return f'{self.name} at {self.source}'


class AccountSource(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def invest(self, account):
        raise NotImplementedError()

    def __str__(self):
        return self.name
