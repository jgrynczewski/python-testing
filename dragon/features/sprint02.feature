Feature: Dragon create

Scenario: Create Dragon without name (raise an error)
    Given Dragon does not exist
     When Dragon is created without name
     Then Raise an error with message
