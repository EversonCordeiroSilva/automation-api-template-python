from behave import given, when, then
from assertpy import assert_that


@given("the Fake Store API is available")
def step_impl(context):
    print("OK! The Fake Store API is available.")

@when("I authenticate with valid credentials")
def step_login_valid(context):
    context.response = context.auth_service.login_valid_user()


@when('I authenticate with email "{email}" and password "{password}"')
def step_login_with_parameters(context, email, password):
    email = context.normalize(email)
    password = context.normalize(password)
    context.response = context.auth_service.login(email, password)


@then("the API should return status code {status_code:d}")
def step_validate_status_code(context, status_code):
    assert_that(context.response.status_code).is_equal_to(status_code)


@then("an authentication token should be returned")
def step_validate_token(context):
    body = context.response.json()

    assert_that(body).contains_key("access_token")
    assert_that(body["access_token"]).is_not_empty()

    assert_that(body).contains_key("refresh_token")
    assert_that(body["refresh_token"]).is_not_empty()

