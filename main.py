import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://economia.awesomeapi.com.br/last/"

    def get_exchange_rate(self, base, target):
        try:
            response = requests.get(f"{self.api_url}{base}-{target}")
            response.raise_for_status()
            data = response.json()
            return float(data[f"{base}{target}"]['bid'])
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def convert(self, amount, rate):
        return amount * rate

def main():
    converter = CurrencyConverter()
    print("--- Professional Currency Converter (EUR <-> BRL) ---")
    try:
        rate = converter.get_exchange_rate("EUR", "BRL")
        if rate:
            print(f"Current Rate: 1 EUR = {rate:.4f} BRL")
            amount = float(input("Enter amount in EUR: "))
            result = converter.convert(amount, rate)
            print(f"Converted Amount: {result:.2f} BRL")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
