from django.conf import settings
from django.db import models


class Stock(models.Model):
    """Company Stock Model."""
    name = models.CharField(max_length=48)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name


class StockOwned(models.Model):
    """Stocks own by a user."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="stocks_owned", on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, related_name='stock_owners', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.stock.name} quantity: {self.quantity} "
