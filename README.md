# Simple CLI Calculator

A small command-line calculator written in Python. It supports the four basic
arithmetic operations (`+`, `-`, `*`, `/`) in two modes: an interactive REPL and
one-shot evaluation.

## Requirements

- Python 3.10 or newer (uses `from __future__ import annotations` and modern type hints).

## Usage

### One-shot evaluation

```bash
python calculator.py 2 + 3
# 5

python calculator.py 7 / 2
# 3.5
```

### Interactive REPL

```bash
python calculator.py
# Simple calculator. Enter expressions like '2 + 3'. Type 'quit' to exit.
# > 10 * 4
# 40
# > quit
```

## Running the tests

```bash
python -m unittest test_calculator.py
```

## Project layout

| File | Purpose |
|---|---|
| `calculator.py` | Calculator implementation and CLI entry point. |
| `test_calculator.py` | Unit tests for parsing, evaluation, and formatting. |

## Error handling

- Division by zero raises `CalculatorError`.
- Unsupported operators raise `CalculatorError`.
- Malformed expressions raise `CalculatorError` with a helpful message.
