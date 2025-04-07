from django.db import models

# Create your models here.


class Index(models.Model):
    """Represents a stock market index (e.g., Nifty 500, S&P 500)."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    """Represents a single stock/security."""

    ticker = models.CharField(max_length=20, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    index = models.ForeignKey(
        Index,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stocks",
    )
    # Add other fields later as needed, e.g., sector, industry,
    # market_cap, price_data

    def __str__(self):
        return f"{self.name} ({self.ticker})"
