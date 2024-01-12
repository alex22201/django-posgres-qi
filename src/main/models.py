from django.db import models

from django.db import models


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price_in_usd = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_by_name(cls, name):
        return cls.objects.filter(name=name).first()
