@mi_primer_test
Feature: User Login
  As a user, I want to log in to the application so that I can access my account.

  Scenario Outline: Navigate to login page and authenticate
    Given the user navigates to the login page
    When the user enters username "<user>"
    And the user enters password "<pass>"
    Then the user should be logged in successfully

    Examples:
      | user        | pass     |  |
      | genesis0243 | gene2025 |  |
