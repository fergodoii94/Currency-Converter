# Currency Converter

A focused Python CLI for EUR/BRL conversion using a public exchange-rate API.

## Features

- Live quote retrieval from the configured API
- HTTP timeout and status validation
- `Decimal` for monetary calculations
- Explicit handling of invalid input and network failures
- Small service class that is easy to extend and test

## Run

```bash
pip install requests
python main.py
```

The application currently demonstrates EUR → BRL conversion. The service class can be extended to support additional currency pairs.

## Architecture

`CurrencyConverter` handles external API communication and conversion logic. `main()` is responsible only for the CLI interaction and user-facing error handling.

## Stack

Python · Requests · Decimal · Dataclasses

## Roadmap

- Automated tests
- Configurable API provider
- Multi-pair CLI selection
- API/web interface
- Rate caching and resilience policies
