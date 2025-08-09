Feature: First

Scenario Outline: Navegate for page
    Given user accesses the page
    And user enter user <user>
    And user enter pass <pass>
    Examples:
        | user | pass |

   