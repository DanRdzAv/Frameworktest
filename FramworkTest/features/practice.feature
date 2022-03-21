Feature: Search

    Scenario: Search mexico
        Given I load the page
        When I put for "Me"
        And I select "Mexico"
        Then I view "Mexico"

    Scenario: Verify money back
        Given I load the page
        When I click on Switch Window Example
        Then I see the the expected message

    Scenario: DropDown selection
        Given I load the page
        When I select in the dropdown "option2"
        And I select in the dropdown "option3"
        Then I see the "option3"

    Scenario: Verify new tab
        Given I load the page
        When I click on open tab
        Then I verify the bottom

    Scenario: Verify alert
        Given I load the page
        When I send the name of alert "Stori Card"
        Then I click on alert

    Scenario: Verify confirm
        Given I load the page
        When I send the name of alert "Stori Card"
        Then I click on confirm