"""EUR/BRL currency conversion using a public exchange-rate endpoint."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

import requests


@dataclass(frozen=True)
class ExchangeRate:
    base: str
    target: str
    bid: Decimal


class CurrencyConverter:
    API_URL = "https://economia.awesomeapi.com.br/last"

    def __init__(self, timeout: float = 10.0) -> None:
        self.timeout = timeout

    def get_exchange_rate(self, base: str, target: str) -> ExchangeRate:
        pair = f"{base.upper()}-{target.upper()}"
        response = requests.get(f"{self.API_URL}/{pair}", timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        quote = data[f"{base.upper()}{target.upper()}"]
        return ExchangeRate(base.upper(), target.upper(), Decimal(str(quote["bid"])))

    @staticmethod
    def convert(amount: Decimal, rate: ExchangeRate) -> Decimal:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * rate.bid


def main() -> None:
    converter = CurrencyConverter()
    try:
        rate = converter.get_exchange_rate("EUR", "BRL")
        raw_amount = input("Amount in EUR: ").strip().replace(",", ".")
        amount = Decimal(raw_amount)
        result = converter.convert(amount, rate)
        print(f"1 {rate.base} = {rate.bid:.4f} {rate.target}")
        print(f"Converted amount: {result:.2f} {rate.target}")
    except (InvalidOperation, ValueError) as exc:
        print(f"Invalid input: {exc}")
    except requests.RequestException as exc:
        print(f"Exchange-rate service unavailable: {exc}")


if __name__ == "__main__":
    main()
