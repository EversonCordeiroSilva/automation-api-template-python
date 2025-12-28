@allure.label.epic:Autenticacao
@api @auth
Feature: User authentication via Fake Store API
  """
    As a registered user
    I want to authenticate using my credentials
    So that I can access protected resources
  """

  Background:
    Given the Fake Store API is available

  @smoke @positive @allure.label.story:Login_Sucess @allure.severity:critical
  Scenario: Successful login with valid credentials
    When I authenticate with valid credentials
    Then the API should return status code 201
    And an authentication token should be returned

  @negative @allure.label.story:Login_Failed @allure.severity:minor
  Scenario Outline: Login failures due to invalid credentials
    When I authenticate with email "<email>" and password "<password>"
    Then the API should return status code <status_code>
    Examples:
      | email                   | password      | status_code |
      | john@mail.com           | wrong_pass    | 401         |
      | invalid_user@mail.com   | changeme      | 401         |
      | <empty>                 | changeme      | 401         |
      | john@mail.com           | <empty>       | 401         |
