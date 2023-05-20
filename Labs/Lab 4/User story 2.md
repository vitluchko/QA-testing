<h1>Boundary Value Analysis</h1>

User Story: As an online shopper, I want to be able to track the status of my order so that I can know when to expect its delivery.

Scenario: Track Order Status

Given I am a logged-in user <br />
And I am on the order tracking page <br />
When I enter my order number and email address <br />
Then I can view the current status of my order <br />
And I can see the estimated delivery date <br />
And I receive notifications or updates if there are any changes to the status or delivery date of my order <br />

===================================================================================

* 1. Test Case: Minimum order number and email address

Input: Order number = 1, Email address = "a@a.com"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 2. Test Case: Maximum order number and email address

Input: Order number = 999999, Email address = "z@z.com"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 3. Test Case: Order number at the lower boundary and valid email address

Input: Order number = 1, Email address = "test@example.com"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 4. Test Case: Order number at the upper boundary and valid email address

Input: Order number = 999999, Email address = "test@example.com"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 5. Test Case: Order number below the lower boundary and valid email address

Input: Order number = 0, Email address = "test@example.com"<br />
Expected Output: Display an error message stating that the order number is invalid

* 6. Test Case: Order number above the upper boundary and valid email address

Input: Order number = 1000000, Email address = "test@example.com"<br />
Expected Output: Display an error message stating that the order number is invalid

* 7. Test Case: Valid order number and email address with minimum length

Input: Order number = 123456, Email address = "a@a.com"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 8. Test Case: Valid order number and email address with maximum length

Input: Order number = 654321, Email address = "z@z.com"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 9. Test Case: Valid order number and invalid email address

Input: Order number = 123456, Email address = "invalid_email"<br />
Expected Output: Display an error message stating that the email address is invalid

* 10. Test Case: Valid order number and email address with special characters

Input: Order number = 123456, Email address = "test@example.com!#"<br />
Expected Output: Display the current status and estimated delivery date of the order

* 11. Test Case: Valid order number and email address with leading/trailing spaces

Input: Order number = 123456, Email address = " test@example.com "<br />
Expected Output: Display the current status and estimated delivery date of the order

* 12. Test Case: Order number and email address with valid format but not associated with any order

Input: Order number = 987654, Email address = "test@example.com"<br />
Expected Output: Display an error message stating that the order details are not found

* 13. Test Case: Order number and email address with valid format but order is canceled

Input: Order number = 123456, Email address = "test@example.com"<br />
Expected Output: Display the current status as "Canceled" and estimated delivery date as "N/A"
