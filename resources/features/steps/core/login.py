from behave import given, when, then
from assertpy import assert_that


@given("the Fake Store API is available")
def step_impl(context):
    print("OK! The Fake Store API is available.")

@when("I authenticate with valid credentials")
def step_login_valid(context):
    context.response = context.auth_service.login_valid_user()


@when('I authenticate with email "{email}" and user "{user}" and password "{password}"')
def step_login_with_parameters(context, email, user, password):
    email = context.normalize(email)
    user = context.normalize(user)
    password = context.normalize(password)
    context.response = context.auth_service.login(email, user, password)


@then("the API should return status code {status_code:d}")
def step_validate_status_code(context, status_code):
    assert_that(context.response.status_code).is_equal_to(status_code)


@then("an authentication token should be returned")
def step_validate_token(context):
    body = context.response.json()

    assert_that(body).contains_key("statusMessage")
    assert_that(body["statusMessage"]).is_not_empty()
    assert_that(body["statusMessage"]).contains_key("success")
    assert_that(body["statusMessage"]["success"]).is_instance_of(bool)
    assert_that(body["statusMessage"]).contains_key("userId")
    assert_that(body["statusMessage"]["userId"]).is_instance_of(int)
    assert_that(body["statusMessage"]).contains_key("reason")
    assert_that(body["statusMessage"]["reason"]).is_not_empty()
    assert_that(body["statusMessage"]).contains_key("token")
    assert_that(body["statusMessage"]["token"]).is_not_empty()
    assert_that(body["statusMessage"]).contains_key("sessionId")
    assert_that(body["statusMessage"]["sessionId"]).is_not_empty()

