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
    Then the API should return status code 200
    And an authentication token should be returned

  @negative @allure.label.story:Login_Failed @allure.severity:normal
  Scenario Outline: Login failures due to invalid credentials
    When I authenticate with email "<email>" and user "<user>" and password "<password>"
    Then the API should return status code <status_code>
    Examples:
      | email                                   | user           | password      | status_code |
      | qa.automation.aos01@gmail.com           | qa_auto_user01 | wrong_pass    | 403         |
      | qa.automation.aos01@gmail.com           | qa_wrong_user  | Test@1234     | 403         |
      | invalid_user@mail.com                   | qa_auto_user01 | Test@1234     | 403         |
      | <empty>                                 | qa_auto_user01 | changeme      | 403         |
      | qa.automation.aos01@gmail.com           | <empty>        | Test@1234     | 403         |
      | qa.automation.aos01@gmail.com           | qa_auto_user01 | <empty>       | 403         |
