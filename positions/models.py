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

    def get_current_position_size(self):
        raise NotImplementedError()

    def get_nb_shares(self):
        raise NotImplementedError()

    def get_cost_basis(self):
        raise NotImplementedError()

    def get_total_invested(self):
        raise NotImplementedError()

    def get_investment_value(self):
        raise NotImplementedError()

    def get_roi(self):
        raise NotImplementedError()

    def get_day_pl(self):
        raise NotImplementedError()

    def get_leftovers(self):
        raise NotImplementedError()


    def __str__(self):
        return f'{self.account} - {self.exchange}.{self.symbol}'


class Exchange(models.Model):
    name = models.CharField(max_length=255, blank=False)
    label = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.label
