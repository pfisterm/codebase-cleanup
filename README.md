# codebase-cleanup-template

To get started with the ["Codebase Cleanup" Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/README.md).

## Setup

Create virtual environment:

```sh
conda create -n cleanup-env python=3.8
```

```sh
conda activate cleanup-env
```

Install packages:

```sh
pip install -r requirements.txt
```


## Configuration

Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).
 


Set environment variables using a ".env" file approach:

```sh
ALPHAVANTAGE_API_KEY="..."

```

## Tests

To test functions contained in the file utils.py:

```sh
pytest tests/test_utils.py
```

To test functions contained in the file game.py:

```sh
pytest tests/test_game.py
```

## Usage

Run the game:

```sh
python app/game.py
```

Run the inventory report:

```sh
python -m app.groceries
```

Run the stocks report:

``` sh
python -m app.stocks
```

Run the crypto report:

``` sh
python -m app.crypto
```
