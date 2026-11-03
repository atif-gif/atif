"""Simple command-line calculator.

Supports two modes:

* Interactive REPL: ``python calculator.py``
* One-shot evaluation: ``python calculator.py 2 + 3``
"""

from __future__ import annotations

import argparse
import operator
import re
import sys
from typing import Callable

OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

# Matches "2 + 3", "2+3", "-1.5 * 4" and similar single-operation expressions.
_EXPRESSION_RE = re.compile(
    r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$"
)


class CalculatorError(ValueError):
    """Raised when an expression cannot be parsed or evaluated."""


def calculate(left: float, op: str, right: float) -> float:
    """Apply ``op`` to ``left`` and ``right``.

    Raises:
        CalculatorError: if the operator is unsupported or division by zero
            is attempted.
    """
    if op not in OPERATIONS:
        raise CalculatorError(f"Unsupported operator: {op!r}. Use one of + - * /.")
    if op == "/" and right == 0:
        raise CalculatorError("Division by zero is not allowed.")
    return OPERATIONS[op](left, right)


def parse_expression(expression: str) -> tuple[float, str, float]:
    """Parse a single-operation expression into ``(left, op, right)``.

    Raises:
        CalculatorError: if the expression does not match the expected form.
    """
    match = _EXPRESSION_RE.match(expression)
    if match is None:
        raise CalculatorError(
            f"Invalid expression: {expression!r}. Expected form: <number> <op> <number>."
        )
    left, op, right = match.groups()
    return float(left), op, float(right)


def format_result(value: float) -> str:
    """Render a result without a trailing ``.0`` for whole numbers."""
    if value.is_integer():
        return str(int(value))
    return f"{value:g}"


def evaluate(expression: str) -> str:
    """Parse and evaluate ``expression``, returning the formatted result."""
    left, op, right = parse_expression(expression)
    return format_result(calculate(left, op, right))


def run_repl() -> int:
    """Run the interactive calculator loop until the user exits."""
    print("Simple calculator. Enter expressions like '2 + 3'. Type 'quit' to exit.")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not line:
            continue
        if line.lower() in {"quit", "exit"}:
            return 0

        try:
            print(evaluate(line))
        except CalculatorError as exc:
            print(f"Error: {exc}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns a process exit code."""
    parser = argparse.ArgumentParser(description="Simple CLI calculator.")
    parser.add_argument(
        "expression",
        nargs="*",
        help="Expression to evaluate, e.g. 2 + 3. Omit to start the REPL.",
    )
    args = parser.parse_args(argv)

    if not args.expression:
        return run_repl()

    try:
        print(evaluate(" ".join(args.expression)))
    except CalculatorError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
