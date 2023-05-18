* User Story: As a registered user, I want to be able to reset my password so that I can access my account if I forget my password.

Scenario: Reset Password

Given I am a registered user <br />
And I am on the login page <br />
When I click on the "Forgot Password" link <br />
And I enter my email address <br />
Then I receive an email with a link to reset my password <br />
And I am able to successfully reset my password <br />

============================================================================================

* User Story: As an online shopper, I want to be able to track the status of my order so that I can know when to expect its delivery.

Scenario: Track Order Status

Given I am a logged-in user <br />
And I am on the order tracking page <br />
When I enter my order number and email address <br />
Then I can view the current status of my order <br />
And I can see the estimated delivery date <br />
And I receive notifications or updates if there are any changes to the status or delivery date of my order <br />

============================================================================================

* User Story: As a mobile app user, I want to be able to customize my notification preferences so that I can control the types of notifications I receive.

Scenario: Customize Notification Preferences

Given I am a registered user <br />
And I am logged in to the mobile app <br />
When I navigate to the notification settings page <br />
Then I can select the types of notifications I want to receive (e.g., promotions, order updates, new features) <br />
And I can choose the preferred method of receiving notifications (e.g., push notifications, email, SMS) <br />
And I can save my preferences <br />
And I receive notifications based on the customized preferences I have set. <br />
