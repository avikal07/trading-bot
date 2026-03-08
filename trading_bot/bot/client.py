from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
import os
from dotenv import load_dotenv
from trading_bot.bot.logging_config import setup_logger

load_dotenv()

logger = setup_logger()


class BinanceFuturesClient:
    """
    Wrapper around Binance Futures Testnet API
    """

    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("API keys not found. Please set BINANCE_API_KEY and BINANCE_SECRET_KEY")

        self.client = Client(api_key, api_secret)

        # connect to futures testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Connected to Binance Futures Testnet")

    def create_order(self, symbol, side, order_type, quantity, price=None):
        """
        Place an order on Binance Futures Testnet
        """

        try:
            logger.info(
                f"Sending order | symbol={symbol} side={side} type={order_type} qty={quantity} price={price}"
            )

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logger.info(f"Order response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Network error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise