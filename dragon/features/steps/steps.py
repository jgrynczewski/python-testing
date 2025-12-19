from behave import given, when, then

from src.game import Dragon


@given('Dragon does not exist')
def step_dragon_not_exist(context):
    context.dragon = None

@when('Dragon is created with name "{name}"')
def step_create_dragon_with_name(context, name):
    context.dragon = Dragon(name)


@then('Dragon exists')
def step_dragon_exists_check(context):
    assert context.dragon is not None, "Dragon should exists"


@then('Name is "{expected_name}"')
def step_name_is(context, expected_name):
    assert context.dragon.name == expected_name, \
        f"Expected name '{expected_name}', got {context.dragon.name}"
