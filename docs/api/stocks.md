# Stocks
Buying/Selling Stocks, and retrieve Stock Details owned by User

## Buy Stock

**Request**:

`POST` `/api/v1/stocks/buy/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
stock_symbol | string | Yes      | The stock symbol you will buy (i.e. JFC)
quantity     | integer| Yes      | How many stocks to buy.

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "stock_symbol": "JFC",
  "quantity": 1
}
```

## Sell Stock

**Request**:

`POST` `/api/v1/stocks/sell/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
stock_symbol | string | Yes      | The stock symbol you will sell (i.e. JFC)
quantity     | integer| Yes      | How many stocks to sell.

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "stock_symbol": "JFC",
  "quantity": 1
}
```


## List Owned Stocks

**Request**:

`GET` `/api/v1/stocks/`

Parameters:


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 Ok

[
    {
        "stock_symbol": "JFC",
        "price": 10.4,
        "quantity": 6,
        "total_value": 62.400000000000006
    }
]
```


## Get Owned Stock Details

**Request**:

`GET` `/api/v1/stocks/:stock_symbol/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
stock_symbol | string | Yes      | The stock symbol you will sell (i.e. JFC)


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 Ok

{
    "stock_symbol": "JFC",
    "price": 10.4,
    "quantity": 6,
    "total_value": 62.400000000000006
}
```