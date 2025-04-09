from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # API URLs removed for now
    # path(
    #     "api/stocks/",
    #     views.StockListAPIView.as_view(),
    #     name="stock-list-api"
    # ),
    # Add other API endpoints here later
    # Standard Django view URLs (if any)
    path("", views.heatmap_page, name="heatmap-page"),
]
