from rest_framework import generics
from .models import Stock
from .serializers import StockSerializer

# Create your views here.

# Standard Django view (can be added later for HTML pages)
# def heatmap_page(request):
#     return render(request, 'core/heatmap_page.html')

# --- API Views ---


class StockListAPIView(generics.ListAPIView):
    """API endpoint that allows stocks to be viewed."""

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # Add pagination later if needed
    # from rest_framework.pagination import PageNumberPagination
    # pagination_class = PageNumberPagination
