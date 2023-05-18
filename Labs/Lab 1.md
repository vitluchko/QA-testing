User Story: As a registered user, I want to be able to reset my password so that I can access my account if I forget my password.

Scenario: Reset Password

Given I am a registered user
And I am on the login page
When I click on the "Forgot Password" link
And I enter my email address
Then I receive an email with a link to reset my password
And I am able to successfully reset my password

============================================================================================

User Story: As an online shopper, I want to be able to track the status of my order so that I can know when to expect its delivery.

Scenario: Track Order Status

Given I am a logged-in user
And I am on the order tracking page
When I enter my order number and email address
Then I can view the current status of my order
And I can see the estimated delivery date
And I receive notifications or updates if there are any changes to the status or delivery date of my order

============================================================================================

User Story: As a mobile app user, I want to be able to customize my notification preferences so that I can control the types of notifications I receive.

Scenario: Customize Notification Preferences

Given I am a registered user
And I am logged in to the mobile app
When I navigate to the notification settings page
Then I can select the types of notifications I want to receive (e.g., promotions, order updates, new features)
And I can choose the preferred method of receiving notifications (e.g., push notifications, email, SMS)
And I can save my preferences
And I receive notifications based on the customized preferences I have set.