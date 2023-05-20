<h1>Pairwise Testing</h1>

Use Case 1: Logging In to a Web Application

* Use Case: User Login<br />
* Actor: User<br />
* Use Case Overview: This use case describes the process of a user logging in to a web application.<br />
* Subject Area: Web Application Authentication<br />
* Actor(s): User<br />
* Trigger: The user navigates to the web application and wants to access their account.<br />
* Preconditions: The user must have a valid account registered with the web application.<br />

===================================================================================

To generate pairwise test cases for the use case "User Login," we need to identify the<br />
different input parameters that can affect the login process. Here are four key parameters<br />
for testing:
 1. Username<br />
 2. Password<br />
 3. Browser Type<br />
 4. Operating System<br />
 
We will create pairwise test cases to cover all possible combinations of these parameters.<br />
Pairwise testing helps reduce the number of test cases needed while ensuring<br />
comprehensive coverage.

Test Case 1:<br />
* Username: JohnDoe<br />
* Password: Password123<br />
* Browser Type: Chrome<br />
* Operating System: Windows<br />

Test Case 2:<br />
* Username: JaneSmith<br />
* Password: P@ssw0rd<br />
* Browser Type: Firefox<br />
* Operating System: macOS<br />

Test Case 3:<br />
* Username: admin<br />
* Password: admin123<br />
* Browser Type: Safari<br />
* Operating System: iOS<br />

Test Case 4:<br />
* Username: user1<br />
* Password: mypassword<br />
* Browser Type: Chrome<br />
* Operating System: Linux<br />

Test Case 5:<br />
* Username: JohnDoe<br />
* Password: P@ssw0rd<br />
* Browser Type: Safari<br />
* Operating System: Windows<br />

Test Case 6:<br />
* Username: JaneSmith<br />
* Password: Password123<br />
* Browser Type: Chrome<br />
* Operating System: macOS<br />

Test Case 7:<br />
* Username: admin<br />
* Password: mypassword<br />
* Browser Type: Firefox<br />
* Operating System: Linux<br />

Test Case 8:<br />
* Username: user1<br />
* Password: admin123<br />
* Browser Type: Safari<br />
* Operating System: iOS<br />

These eight test cases cover all possible combinations of the given parameters. By testing<br />
different combinations, we ensure that we have covered potential variations that users may<br />
encounter while logging in to the web application.
