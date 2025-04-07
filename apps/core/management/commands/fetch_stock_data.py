import yfinance as yf
from django.core.management.base import BaseCommand
from apps.core.models import Stock

# from tqdm import tqdm  # Optional: for progress bar

# TODO: Consider fetching the list of Nifty 500 tickers dynamically or from a
# reliable source. This is a small, static subset for demonstration purposes.
NIFTY_500_TICKERS = [
    "RELIANCE.NS",
    "TCS.NS",
    "HDFCBANK.NS",
    "INFY.NS",
    "HINDUNILVR.NS",
    "ICICIBANK.NS",
    "BHARTIARTL.NS",
    "SBIN.NS",
    "BAJFINANCE.NS",
    "KOTAKBANK.NS",
    # Add more tickers as needed...
]


class Command(BaseCommand):
    help = (
        "Fetches stock information from Yahoo Finance for a predefined list "
        "of tickers (e.g., Nifty 500 subset) and populates the Stock model."
    )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting stock data fetch..."))

        # Optional: Get or create a default Index if needed, or handle index
        # assignment differently
        # nifty_500_index, created = Index.objects.get_or_create(
        #     name="Nifty 500"
        # )
        # if created:
        #     self.stdout.write(
        #         self.style.SUCCESS('Created Index: Nifty 500')
        #     )

        stocks_created = 0
        stocks_updated = 0
        errors_occurred = 0

        # Use tqdm for a progress bar if installed and desired
        # for ticker_symbol in tqdm(NIFTY_500_TICKERS, desc="Fetching Stocks"):
        for ticker_symbol in NIFTY_500_TICKERS:
            try:
                ticker_data = yf.Ticker(ticker_symbol)
                info = ticker_data.info

                # Check if essential data exists
                if not info or not info.get("symbol"):
                    self.stderr.write(
                        self.style.WARNING(
                            f"Skipping {ticker_symbol}: No data/symbol found."
                        )
                    )
                    errors_occurred += 1
                    continue

                stock_name = info.get("longName", info.get("shortName", ticker_symbol))

                stock, created = Stock.objects.update_or_create(
                    ticker=ticker_symbol,
                    defaults={
                        "name": stock_name,
                        # 'index': nifty_500_index, # Uncomment if assigning
                        # Add other fields from 'info' if needed, e.g.:
                        # 'sector': info.get('sector'),
                        # 'industry': info.get('industry'),
                        # 'market_cap': info.get('marketCap'),
                    },
                )

                if created:
                    stocks_created += 1
                    # self.stdout.write(
                    #     f"Created: {stock_name} ({ticker_symbol})"
                    # )
                else:
                    stocks_updated += 1
                    # self.stdout.write(
                    #     f"Updated: {stock_name} ({ticker_symbol})"
                    # )

            except Exception as e:
                self.stderr.write(
                    self.style.ERROR(f"Error fetching data for {ticker_symbol}: {e}")
                )
                errors_occurred += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Finished fetching data. Created: {stocks_created}, "
                f"Updated: {stocks_updated}, Errors: {errors_occurred}"
            )
        )
