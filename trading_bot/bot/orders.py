from trading_bot.bot.client import BinanceFuturesClient
from trading_bot.bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from trading_bot.bot.logging_config import setup_logger

logger = setup_logger()

client = BinanceFuturesClient()


def place_order(symbol, side, order_type, quantity, price=None):
    """
    Validate inputs and place an order
    """

    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        logger.info("Validated user inputs")

        # Place order
        response = client.create_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        return response

    except Exception as e:
        logger.error(f"Order placement failed: {e}")
        raise