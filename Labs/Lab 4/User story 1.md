User Story: As a registered user, I want to be able to reset my password so that I can access my account if I forget my password.

Scenario: Reset Password

Given I am a registered user <br />
And I am on the login page <br />
When I click on the "Forgot Password" link <br />
And I enter my email address <br />
Then I receive an email with a link to reset my password <br />
And I am able to successfully reset my password <br />

===================================================================================

Test Case 1: Clicking on "Forgot Password" link<br />

* Preconditions:<br />
User is registered and on the login page.<br />
* Steps:<br />
User clicks on the "Forgot Password" link.<br />
* Expected Results:<br />
User is redirected to a page where they can enter their email address to reset the password.<br />

Test Case 2: Entering a valid email address<br />

* Preconditions:<br />
User is on the password reset page.<br />
* Steps:<br />
User enters a valid email address.<br />
User clicks on the "Reset Password" button.<br />
* Expected Results:<br />
User receives an email with a link to reset their password.<br />
User is notified on the page that an email has been sent.<br />

Test Case 3: Entering an invalid email address<br />

* Preconditions:<br />
User is on the password reset page.<br />
* Steps:<br />
User enters an invalid email address (e.g., without '@' symbol).<br />
User clicks on the "Reset Password" button.<br />
* Expected Results:<br />
User is prompted to enter a valid email address.<br />
User does not receive an email.<br />

Test Case 4: Resetting password with a valid password reset link<br />

* Preconditions:<br />
User has received the password reset email.<br />
User clicks on the password reset link provided in the email.<br />
* Steps:<br />
User is redirected to a page where they can enter a new password.<br />
User enters a new password and confirms it.<br />
User clicks on the "Reset Password" button.<br />
* Expected Results:<br />
User receives a confirmation message that their password has been successfully reset.<br />
User is able to log in with the new password.<br />

Test Case 5: Resetting password with an expired password reset link<br />

* Preconditions:<br />
User has received the password reset email.<br />
User waits for a significant amount of time (e.g., more than 24 hours) before clicking on the password reset link.<br />
* Steps:<br />
User clicks on the expired password reset link provided in the email.<br />
* Expected Results:<br />
User is notified that the password reset link has expired.<br />
User is prompted to initiate the password reset process again.<br />

Test Case 6: Resetting password with an invalid password confirmation<br />

* Preconditions:<br />
User has received the password reset email.<br />
User clicks on the password reset link provided in the email.<br />
User is on the page to enter a new password.<br />
* Steps:<br />
User enters a new password but provides a different value in the password confirmation field.<br />
User clicks on the "Reset Password" button.<br />
* Expected Results:<br />
User is prompted to ensure that the password and password confirmation fields match.<br />
User is unable to reset the password until a valid password confirmation is provided.
