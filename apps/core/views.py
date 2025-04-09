from django.shortcuts import render
from .models import Stock  # Removed unused Serializer import
import json  # For dumping context data
import plotly  # For plot generation
import plotly.graph_objs as go  # For plot generation

# Create your views here.


# Standard Django view for the heatmap page
def heatmap_page(request):
    """Renders the main heatmap visualization page."""

    # Fetch data (example: all stocks for now)
    stocks = Stock.objects.all()

    # Prepare data for Plotly Treemap trace
    if stocks:
        labels = [f"{s.name} ({s.ticker})" for s in stocks]
        parents = ["Stocks"] * len(stocks)  # All belong to a root "Stocks" node
        values = [10] * len(stocks)  # Dummy size value - USE POSITIVE FIXED VALUE
        # Dummy color value (Needs real data later)
        # Example: color based on some metric (e.g., positive/negative)
        colors = [1 if i % 2 == 0 else -1 for i, _ in enumerate(stocks)]

        trace = {
            "type": "treemap",
            "labels": ["Stocks", *labels],  # Include root node
            "parents": ["", *parents],  # Root has no parent
            "values": [0, *values],  # Prepend 0 for root node value AGAIN
            "marker": {
                "colors": [0, *colors],  # Provide colors for ALL nodes (length N+1)
                "colorscale": "RdYlGn",
                "cmin": -2,
                "cmax": 2,
            },
            "textinfo": "label",
            "pathbar": {"visible": True},
        }
        figure_data = [trace]
    else:
        figure_data = []

    layout = {
        "title": "Stock Market Overview (Treemap)",
        "margin": {"l": 0, "r": 0, "b": 0, "t": 30},  # Adjust margins
    }

    # Combine trace and layout into figure JSON for Plotly.js
    figure_json = json.dumps(
        {"data": figure_data, "layout": layout}, cls=plotly.utils.PlotlyJSONEncoder
    )

    context = {"figure_json": figure_json}
    return render(request, "core/heatmap_page.html", context)


# --- API Views Section Removed ---
