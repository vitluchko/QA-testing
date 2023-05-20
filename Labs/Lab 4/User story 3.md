<h1>State Transition</h1>

User Story: As a mobile app user, I want to be able to customize my notification preferences so that I can control the types of notifications I receive.

Scenario: Customize Notification Preferences

Given I am a registered user <br />
And I am logged in to the mobile app <br />
When I navigate to the notification settings page <br />
Then I can select the types of notifications I want to receive (e.g., promotions, order updates, new features) <br />
And I can choose the preferred method of receiving notifications (e.g., push notifications, email, SMS) <br />
And I can save my preferences <br />
And I receive notifications based on the customized preferences I have set. <br />

===================================================================================

<h4>Test Case 1:</h4>

1. Preconditions:
* User is a registered user.
* User is logged in to the mobile app.
2. Actions:
* Navigate to the notification settings page.
* Select the "Promotions" and "Order Updates" notification types.
* Choose the "Push Notifications" and "Email" methods.
* Save the preferences.
3. Expected Results:
* Preferences are saved successfully.
* User receives notifications for promotions and order updates through push notifications and email.
<br />

<h4>Test Case 2:</h4>

1. Preconditions:
* User is a registered user.
* User is logged in to the mobile app.
2. Actions:
* Navigate to the notification settings page.
* Select the "New Features" notification type.
* Choose the "SMS" method.
Save the preferences.
3. Expected Results:
* Preferences are saved successfully.
* User receives notifications for new features through SMS.
<br />

<h4>Test Case 3:</h4>

1. Preconditions:
* User is a registered user.
* User is logged in to the mobile app.
2. Actions:
* Navigate to the notification settings page.
* Deselect all notification types.
* Choose the "Push Notifications" method.
* Save the preferences.
3. Expected Results:
* Preferences are saved successfully.
* User does not receive any notifications.
<br />

<h4>Test Case 4:</h4>

1. Preconditions:
* User is a registered user.
* User is logged in to the mobile app.
2. Actions:
* Navigate to the notification settings page.
* Select the "Promotions" and "Order Updates" notification types.
* Choose the "Push Notifications" and "Email" methods.
* Save the preferences.
* Navigate to the notification settings page again.
* Deselect the "Promotions" notification type.
* Save the preferences.
3. Expected Results:
* Preferences are saved successfully.
* User receives notifications for order updates through push notifications and email.
* User does not receive notifications for promotions.
<br />

<h4>Test Case 5:</h4>

1. Preconditions:
* User is a registered user.
* User is logged in to the mobile app.
2. Actions:
* Navigate to the notification settings page.
* Select the "Promotions" and "Order Updates" notification types.
* Choose the "Push Notifications" and "Email" methods.
* Save the preferences.
* Navigate to the notification settings page again.
* Deselect the "Push Notifications" method.
* Save the preferences.
3. Expected Results:
* Preferences are saved successfully.
* User receives notifications for promotions and order updates through email.
* User does not receive notifications through push notifications.
