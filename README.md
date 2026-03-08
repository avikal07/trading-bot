# Binance Futures Testnet Trading Bot

A simplified **Python-based trading bot** that interacts with the **Binance Futures Testnet (USDT-M)**.
This project demonstrates how to place **MARKET** and **LIMIT** orders using a clean, modular architecture with proper **logging, validation, and error handling**.

This project was developed as part of a **technical assignment for an internship**, focusing on code quality, structure, and maintainability.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Support for **BUY** and **SELL**
* Command Line Interface (CLI) using `argparse`
* Input validation for order parameters
* Structured project architecture
* Logging of API requests, responses, and errors
* Error handling for invalid inputs, API errors, and network failures

---

## Project Structure

```
trading-bot/
│
├── trading_bot/
│   ├── cli.py                # CLI entry point
│   │
│   └── bot/
│       ├── __init__.py
│       ├── client.py         # Binance Futures API wrapper
│       ├── orders.py         # Order placement logic
│       ├── validators.py     # Input validation
│       └── logging_config.py # Logging setup
│
├── logs/
│   └── trading_bot.log       # Log output
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Requirements

* Python **3.8+**
* Binance Futures **Testnet API credentials**

Libraries used:

* `python-binance`
* `python-dotenv`
* `requests`

Install dependencies using:

```
pip install -r requirements.txt
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/avikal07/trading-bot.git
cd trading-bot
```

---

### 2. Create Virtual Environment

```
python3 -m venv venv
```

Activate the environment:

**Linux / macOS**

```
source venv/bin/activate
```

**Windows**

```
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
```

API credentials should be generated from the **Binance Futures Testnet**.

---

## Usage

The bot accepts order parameters via the command line.

### Example: MARKET Order

```
python -m trading_bot.cli \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.001
```

Example output:

```
===== ORDER REQUEST SUMMARY =====
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001
Price: None

===== ORDER RESPONSE =====
Order ID: 123456
Status: FILLED
Executed Quantity: 0.001
Average Price: 67250

Order placed successfully
```

---

### Example: LIMIT Order

```
python -m trading_bot.cli \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.001 \
--price 90000
```

---

## Logging

All API interactions and errors are logged to:

```
logs/trading_bot.log
```

Example log entries:

```
2026-03-08 04:05:32 | INFO | Sending order | symbol=BTCUSDT side=BUY type=MARKET qty=0.001
2026-03-08 04:05:33 | INFO | Order response | orderId=123456 status=FILLED executedQty=0.001 avgPrice=67250

2026-03-08 04:07:12 | INFO | Sending order | symbol=BTCUSDT side=SELL type=LIMIT qty=0.001 price=90000
2026-03-08 04:07:13 | INFO | Order response | orderId=123457 status=NEW executedQty=0 avgPrice=0
```

---

## Error Handling

The application handles the following errors gracefully:

* Invalid user inputs
* Missing parameters
* Binance API errors
* Network failures

All errors are logged and displayed clearly to the user.

---

## Assumptions

* Only **USDT-M Futures trading pairs** are supported.
* Only **MARKET** and **LIMIT** order types are implemented.
* The bot is designed to work with the **Binance Futures Testnet**.

---

## Evaluation Criteria Coverage

| Requirement        | Implementation            |
| ------------------ | ------------------------- |
| Market Orders      | Implemented               |
| Limit Orders       | Implemented               |
| BUY / SELL Support | Implemented               |
| CLI Input          | argparse-based CLI        |
| Input Validation   | validators.py             |
| Logging            | logging_config.py         |
| Error Handling     | try/except across modules |
| Structured Code    | modular architecture      |
| Documentation      | detailed README           |

---

## Author

**Avikal Singh**

Developed as part of a **technical internship assignment** demonstrating API integration, clean software architecture, and error handling in Python.

GitHub:
https://github.com/avikal07
