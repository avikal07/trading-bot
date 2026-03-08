import argparse
from trading_bot.bot.orders import place_order
from trading_bot.bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument(
    "--symbol",
    required=True,
    help="Trading symbol (example: BTCUSDT)"
)

parser.add_argument(
    "--side",
    required=True,
    choices=["BUY", "SELL"],
    help="Order side"
)

parser.add_argument(
    "--type",
    required=True,
    choices=["MARKET", "LIMIT"],
    help="Order type"
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Required for LIMIT orders"
)
    args = parser.parse_args()

    try:
        print("\n===== ORDER REQUEST SUMMARY =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")
        print("=================================\n")

        response = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")
        print("===========================\n")

        print("✅ Order placed successfully!")

    except Exception as e:
        logger.error(f"CLI error: {e}")
        print(f"❌ Order failed: {e}")


if __name__ == "__main__":
    main()