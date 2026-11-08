"""Print a summary of the configured Alpaca paper-trading account."""

import os

from alpaca.trading.client import TradingClient
from dotenv import load_dotenv


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing {name}. Copy .env.example to .env and add your paper key.")
    return value


def main() -> None:
    load_dotenv()
    client = TradingClient(
        required_env("ALPACA_API_KEY"),
        required_env("ALPACA_SECRET_KEY"),
        paper=os.getenv("ALPACA_PAPER", "true").lower() == "true",
    )
    account = client.get_account()
    print(f"Status: {account.status}")
    print(f"Portfolio value: ${float(account.portfolio_value):,.2f}")
    print(f"Cash: ${float(account.cash):,.2f}")
    print(f"Buying power: ${float(account.buying_power):,.2f}")


if __name__ == "__main__":
    main()
