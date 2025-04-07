from rest_framework import serializers
from .models import Stock, Index


class StockSerializer(serializers.ModelSerializer):
    """Serializer for the Stock model."""

    # Optionally include related Index info
    # index_name = serializers.CharField(source='index.name', read_only=True)

    class Meta:
        model = Stock
        fields = ["id", "ticker", "name"]  # Add other fields as needed
        # fields = ['id', 'ticker', 'name', 'index_name'] # If including index


class IndexSerializer(serializers.ModelSerializer):
    """Serializer for the Index model."""

    class Meta:
        model = Index
        fields = ["id", "name", "description"]
