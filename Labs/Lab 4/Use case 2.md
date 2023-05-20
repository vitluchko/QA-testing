<h1>Error Guessing</h1>

Use Case 2: Updating User Profile Information

* Use Case: Update User Profile<br />
* Actor: User<br />
* Use Case Overview: This use case describes the process of a user updating their profile information in a web application.<br />
* Subject Area: User Management<br />
* Actor(s): User<br />
* Trigger: The user wants to modify their personal information or preferences in the web application.<br />
* Preconditions: The user must be logged in to their account.<br />

===================================================================================

<h4>Test Case 1:</h4>

* Title: Valid Profile Update<br />
* Description: The user updates their profile information with valid data.<br />
* Test Steps:

 1. Log in to the web application with valid credentials.
 2. Navigate to the user profile section.
 3. Modify one or more fields (e.g., name, email, phone number) with valid information.
 4. Click on the "Save" or "Update" button.
 5. Verify that the changes are successfully saved.
* Expected Result: The user's profile information is updated successfully without any errors.<br /><br />

<h4>Test Case 2:</h4>

* Title: Invalid Email Format<br />
* Description: The user tries to update their profile with an invalid email format.<br />
* Test Steps:

 1. Log in to the web application with valid credentials.
 2. Navigate to the user profile section.
 3. Modify the email field with an invalid email format (e.g., "example.com").
 4. Click on the "Save" or "Update" button.
 5. Verify the error message displayed regarding the invalid email format.
* Expected Result: The web application should display an error message indicating that the email format is invalid and should prompt the user to correct it.<br /><br />

<h4>Test Case 3:</h4>

* Title: Empty Required Fields<br />
* Description: The user tries to update their profile with empty required fields.<br />
* Test Steps:

 1. Log in to the web application with valid credentials.
 2. Navigate to the user profile section.
 3. Leave one or more required fields (e.g., name, email) empty.
 4. Click on the "Save" or "Update" button.
 5. Verify the error message displayed indicating the required fields that need to be filled.
* Expected Result: The web application should display an error message indicating the required fields that need to be filled and should prompt the user to complete them.<br /><br />

<h4>Test Case 4:</h4>

* Title: Phone Number Length Exceeded<br />
* Description: The user tries to update their profile with a phone number exceeding the maximum allowed length.<br />
* Test Steps:

 1. Log in to the web application with valid credentials.
 2. Navigate to the user profile section.
 3. Modify the phone number field with a value longer than the maximum allowed length (e.g., 15 digits).
 4. Click on the "Save" or "Update" button.
 5. Verify the error message displayed indicating the maximum length exceeded for the phone number.
* Expected Result: The web application should display an error message indicating that the phone number has exceeded the maximum allowed length and should prompt the user to enter a valid phone number.<br /><br />

<h4>Test Case 5:</h4>

* Title: Cancel Profile Update<br />
* Description: The user cancels the profile update process.<br />
* Test Steps:

 1. Log in to the web application with valid credentials.
 2. Navigate to the user profile section.
 3. Modify one or more fields.
 4. Click on the "Cancel" or "Discard Changes" button.
 5. Verify that the changes are not saved, and the user is returned to the previous profile view without any updates.
* Expected Result: The web application should discard the changes made by the user and return them to the previous profile view without saving any modifications.
