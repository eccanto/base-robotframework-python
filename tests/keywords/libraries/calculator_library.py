from assertpy import assert_that
from robot.api.deco import keyword, library

from tests.keywords.elements.calculator import Calculator


@library(scope='GLOBAL')
class CalculatorLibrary:
    @keyword('open calculator')
    def open_calculator(self) -> None:
        self.calculator = Calculator()

        # import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()

    @keyword('close calculator')
    def close_calculator(self) -> None:
        self.calculator.close()

    @keyword('the calculator is open')
    def is_open(self) -> None:
        assert_that(self.calculator.running).is_true()

    @keyword('the expression "${expression}" is entered')
    def enter_expression(self, expression: str) -> None:
        self.calculator.enter(expression)

    @keyword('I press the calculate button')
    def calculate(self) -> None:
        self.calculator.calculate()

    @keyword('the result shown is "${result}"')
    def check_result(self, result: str) -> None:
        assert_that(self.calculator.result).is_equal_to(result)

    @keyword('clean result')
    def clean_result(self) -> None:
        self.calculator.enter('C')
