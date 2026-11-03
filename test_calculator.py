"""Unit tests for calculator.py."""

from __future__ import annotations

import unittest

from calculator import (
    CalculatorError,
    calculate,
    evaluate,
    format_result,
    parse_expression,
)


class CalculateTests(unittest.TestCase):
    def test_addition(self) -> None:
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self) -> None:
        self.assertEqual(calculate(2, "-", 3), -1)

    def test_multiplication(self) -> None:
        self.assertEqual(calculate(2, "*", 3), 6)

    def test_division(self) -> None:
        self.assertEqual(calculate(6, "/", 3), 2)

    def test_division_by_zero_raises(self) -> None:
        with self.assertRaises(CalculatorError):
            calculate(1, "/", 0)

    def test_unsupported_operator_raises(self) -> None:
        with self.assertRaises(CalculatorError):
            calculate(1, "%", 2)


class ParseExpressionTests(unittest.TestCase):
    def test_spaced_expression(self) -> None:
        self.assertEqual(parse_expression("2 + 3"), (2.0, "+", 3.0))

    def test_compact_expression(self) -> None:
        self.assertEqual(parse_expression("2+3"), (2.0, "+", 3.0))

    def test_negative_operands(self) -> None:
        self.assertEqual(parse_expression("-1.5 * -4"), (-1.5, "*", -4.0))

    def test_invalid_expression_raises(self) -> None:
        with self.assertRaises(CalculatorError):
            parse_expression("2 +")

    def test_extra_tokens_raise(self) -> None:
        with self.assertRaises(CalculatorError):
            parse_expression("2 + 3 + 4")


class FormatResultTests(unittest.TestCase):
    def test_whole_number_has_no_decimal(self) -> None:
        self.assertEqual(format_result(4.0), "4")

    def test_fraction_is_preserved(self) -> None:
        self.assertEqual(format_result(2.5), "2.5")


class EvaluateTests(unittest.TestCase):
    def test_evaluate_returns_formatted_string(self) -> None:
        self.assertEqual(evaluate("7 / 2"), "3.5")

    def test_evaluate_propagates_errors(self) -> None:
        with self.assertRaises(CalculatorError):
            evaluate("1 / 0")


if __name__ == "__main__":
    unittest.main()
