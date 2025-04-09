import pytest
from django.urls import reverse
from rest_framework import status

# from rest_framework.test import APIClient # Removed DRF client
from django.test import Client  # Use standard Django test client

from .models import Stock, Index

# Mark all tests in this module to use the database
pytestmark = pytest.mark.django_db

# Create your tests here.

# --- Model Tests ---


def test_index_creation():
    """Test that an Index can be created."""
    index = Index.objects.create(name="Test Index", description="A test index.")
    assert index.name == "Test Index"
    assert index.description == "A test index."
    assert str(index) == "Test Index"
    assert Index.objects.count() == 1


def test_stock_creation():
    """Test that a Stock can be created."""
    index = Index.objects.create(name="Nifty Test")
    stock = Stock.objects.create(ticker="TEST.NS", name="Test Equity", index=index)
    assert stock.ticker == "TEST.NS"
    assert stock.name == "Test Equity"
    assert stock.index == index
    assert str(stock) == "Test Equity (TEST.NS)"
    assert Stock.objects.count() == 1


# --- API Tests Removed ---

# @pytest.fixture
# def api_client():
#     """Fixture to provide an API client."""
#     return APIClient()
#
# def test_stock_list_api_get(api_client):
#     """Test the GET request for the StockListAPIView."""
#     # Create some data first (using one of the tickers we fetched)
#     Stock.objects.create(
#         ticker="RELIANCE.NS", name="Reliance Industries"
#     )
#     Stock.objects.create(
#         ticker="TCS.NS", name="Tata Consultancy Services"
#     )
#
#     # Use the namespace and name defined in core/urls.py
#     url = reverse("core:stock-list-api")
#     response = api_client.get(url)
#
#     assert response.status_code == status.HTTP_200_OK
#     # Check if we got at least the stocks we created
#     assert len(response.data) >= 2
#
#     # Check if one of the created stock tickers is present in the response data
#     tickers_in_response = [item['ticker'] for item in response.data]
#     assert "RELIANCE.NS" in tickers_in_response
#     assert "TCS.NS" in tickers_in_response
#
#     # Optionally check structure of one item
#     first_stock = response.data[0]
#     assert 'id' in first_stock
#     assert 'ticker' in first_stock
#     assert 'name' in first_stock


# --- Basic View Test ---
@pytest.fixture
def client():
    return Client()


def test_heatmap_page_view(client):
    """Test that the heatmap page loads and contains the chart div."""
    url = reverse("core:heatmap-page")
    response = client.get(url)
    assert response.status_code == 200
    assert "heatmapDiv" in str(response.content)
    # We could also test that the figure_json is in the context
    assert "figure_json" in response.context
    # Test if the JSON is valid (basic check)
    try:
        import json

        json.loads(response.context["figure_json"])
        valid_json = True
    except json.JSONDecodeError:
        valid_json = False
    assert valid_json is True


# Add more tests here later, e.g.:
# - Test view context with different data
# - Test HTMX partial responses
