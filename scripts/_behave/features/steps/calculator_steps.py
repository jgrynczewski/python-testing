from behave import given, when, then

from src.calculator import Calculator


@given('I have a calculator')
def step_given_calculator(context):
    context.calculator = Calculator()


@when("I add {num1:d} and {num2:d}")
def step_when_add(context, num1, num2):
    context.calculator.add(num1, num2)


@then("the result should be {expected:d}")
def step_then_result(context, expected):
    assert context.calculator.result == expected, \
        f"Expected {expected} got {context.calcualtor.result}"
