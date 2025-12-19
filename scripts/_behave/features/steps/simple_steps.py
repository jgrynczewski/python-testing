from behave import given, when, then


# ARRANGE
@given('I have a name "{name}"')
def step_given_name(context, name):
    context.name = name


# ACT
@when('I say hello')
def step_when_say_hello(context):
    context.greeting = f"Hello, {context.name}!+++"


# ASSERT
@then('I should get "{expected}"')
def step_then_check_greeting(context, expected):
    assert context.greeting == expected, f"Expected {expected}, got '{context.greeting}'"
