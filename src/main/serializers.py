from rest_framework import serializers
from .models import Cryptocurrency


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'price_in_usd', 'last_updated']

