# features/homepage.feature

Feature: Home page smoke checks
  As as visitor
  I want the home page to load and show important elements

  @smoke
  Scenario: Verify that the Home page loads and shows header
    Given the user is on the automation testing practice home page
    Then the page title should be "Automation Testing Practice"
    And the main header "Automation Testing Practice" should be visible

#  Scenario: Verify that the Udemy Courses menu present and redirect to SDET - QA page
#    Given the user is on the automation testing practice home page
#    Then the "Udemy Courses" link menu text should present
#    Then the user click on the "Udemy Courses" link menu text
#    Then the user should redirect to "https://www.pavanonlinetrainings.com/p/udemy-courses.html"
#    And the page title should be "SDET - QA"