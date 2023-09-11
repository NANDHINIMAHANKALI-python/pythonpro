import requests

def get_exchange_rates(base_currency):
    url = f'https://api.apilayer.com/exchangerates_data/latest?base={base_currency}'
    api_key = 'YOUR_API_KEY'  
    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        print("Failed to fetch exchange rates.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)

    if rates is not None and to_currency in rates:
        converted_amount = amount * rates[to_currency]
        return converted_amount
    else:
        return None


def main():
    print("Currency Converter")
    from_currency = input("Convert from (e.g., USD): ").upper()
    to_currency = input("Convert to (e.g., EUR): ").upper()
    amount = float(input("Amount to convert: "))

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency code(s) or conversion not supported.")

if __name__ == "__main__":
    main()
