# NAJPROSTSZY MOŻLIWY PRZYKŁAD
# Żeby zrozumieć podstawy - jeden scenariusz, jeden krok

Feature: Hello World
  My first BDD test
  
  Scenario: Say hello
    Given I have a name "World"
    When I say hello
    Then I should get "Hello, World!"
