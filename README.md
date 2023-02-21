![Logo](assets/images/logo.JPG)

<h1>Overview</h1>
Travelbooka is an program using "do it yourself" philosophy to create user's own travel package based on
parameters stored in Google sheets. In real world this could be used by a travel agency to allow user to 
mix and match flight and hotel offers to create their own unique bookings. <br>

[View live website here](https://travelbooka.herokuapp.com/)
[View Google sheet with data here](https://docs.google.com/spreadsheets/d/1dK4-eRQH35rCdli_3GxEjlyvN_XVsrNil5q2Ew-VxaM/edit?usp=sharing)

<h1>User experience</h1>
<h2>Goals</h2>
<ul>
<li>The program should be intuitive to navigate</li>
<li>The information that appears on the screen should be relevant for each step</li>
<li>Instructions should appear to guide the user what values to enter</li>
<li>The important information should be highlighted to offer a better user experience</li>
<li>The program should access the right datasheet for every step</li>
<li>The program should update the data sheet with the right values</li>
<li>Selected choices should be displayed back to the user</li>
</ul>
<h2>User Stories</h2>
<ul>
<li>As a user, I want to be able to enter custom parameters like trip date, number of people, target budget</li>
<li>As a user, I want to see information about offered package components</li>
<li>As a user, I want to be able to create my own custom package</li>
<li>As a user, I want to see the content of my choices</li>
<li>As a user, I want to be able to choose the trip type, duration, location</li>
<li>As a user, I want to see information about the total price of the package</li>
<li>As a user, I want to receive package reference number to user for actual booking</li>
</ul>
<h2>User interactions</h2>
<li>Data from spreadsheet with trip componets to be displayed to the user in tables</li>
<li>User options displayed on screen</li>
<li>Prompts guiding user to the next step</li>
<li>Wrong input messages displayed to user in red</li>
<li>Confirmation of selected choice displayed back to user</li>
<li>Reference number for the ready package that the user can use to buy the trip</li>

<h1>Design</h1>
<h2>Program flow</h2>
<h3>General chart</h3>
The general program flow is picrured on the below chart.

![Flowchart](assets/images/travelbooka_chart.JPG)

<h3>Error handling chart</h3>
To avoid cluttering the main chart, error handling logic is shown on a separate chart below.
The following input criteria are applied for non empty input:
<ol>
<li>Date</li>
Needs to be in YYYY-MM-DD format, has to be 3 days from now and withing 1 year from now
<li>Number of people</li>
Needs to be an integer between 1 - 10
<li>Budget</li>
From 230 up
<li>Holiday type</li>
Needs to be 1 or 2 or 3 (as available in table)
<li>Package selection</li>
Needs to be and integer selected from available range displayed in table
</ol>

![Error chart](assets/images/error_handling_chart.JPG)

<h2>Visuals</h2>
<h3>ASCII</h3>
<ul>
<li>pyfiglet standard font</li>
Used to make the logo stand out
<li>pyfiglet bubble font</li>
Used to make booking reference number stand out
</ul>
<h3>Colors</h3>
Colorama colors were applied to make some text stand out in the terminal
<ul>
<li>Logo caption - red, magenta, cyan, yellow</li>
<li>Error messages - red</li>
<li>Correct user input confirmation - green</li>
<li>Free extras message - green, yellow, cyan</li>
<li>Final message - green, yellow</li>
</ul> 
<h3>Table format display</h3>
Table format is used to present data to user - fancy grid from tabulate

<h1>Features</h1>
<h3>Logo and welcome message</h3>

User is shown program logo with caption and instructions how to use the program.<br>
![Welcome](assets/images/welcomemsg.JPG)

<h3>Date input</h3>

User is asked to enter the date they want to travel. Their input is stored through the booking process
and is currently used to differentiate between winter and summer holidays, if the selected type is Active holidays.<br>
![Date input](assets/images/dateprompt.JPG)

<h3>People count input</h3>

User is asked to enter number of people the package is built for. The value is used in the package calculation to
multiply flight & hotel daily rate by number of people.<br>
![People input](assets/images/people_input.JPG)

<h3>Budget input</h3>

User is asked to enter their target budget for the trip. The value is used to select packages with total price within
the budget. If no package is available during the package calculation step, user is asked to try again with different parameters.<br>
![Budget input](assets/images/budget_input.JPG)

Here is an example of completed intro inputs.
![Intro inputs](assets/images/intro_inputs.JPG)

<h3>Holiday type table</h3>

When intro inputs are completed successfully user is shown holiday type table with 3 different types: short city break with predetermined
duration of 3 days, beach holidays, active holidays. User needs to choose from numbers 1, 2, 3 as displayed in the table next to relevant
holiday type. Table data are pulled from Google sheet.<br>
![Holiday type](assets/images/holiday_type_table.JPG)

<h3>Duration</h3>

Duration is predetermined for package 1 (City Break). If user chooses Beach holidays or Active holidays, they're asked to choose duration
from 3, 5 or 7 days. <br>
![Duration](assets/images/duration.JPG)

<h3>Package selection</h3>

Next, user is shown a confirmation of which type and duration they chose. If Active holidays type was selected, program also chooses between Summer
and Winter Active holidays based on the month from the user entered date.
Next, a table with packages withing user entered budget range is displayed with a request to choose one. Table is built from data stored in Google sheet,
based on parameters entered by user.<br>
If there's no package available within that range, error message is displayed (see Error messages below).
![Package selection](assets/images/package_selection.JPG)

<h3>Selected package information</h3>

Next, selected package number is displayed along with the single table row with chosen package contents.<br>
![Selected package](assets/images/selected_package_info.JPG)

<h3>Random extras</h3>

Random free extra is added to show appreciation for using the program and to be used if package is purchased.<br>
![Selected package](assets/images/random_extra.JPG)

<h3>Booking reference and final message</h3>

Unique booking reference number is generated and displayed to user with a request to call to purchase.
Behind the scenes, selected package along with allocated random extra is added to Google sheet with the respective
booking reference, so the travel company can then locate the created package, when user calls to book. Class of Booking
is used to create each booking. <br>
![Booking ref](assets/images/booking_reference.JPG)

<h3>Error messages</h3>
Error messages are displayed in red in the below scenarios:
<ul>
<li>Enter pressed without input</li>

![Empty error](assets/images/emptydate_error.JPG)

<li>Input does not meet requested parameters (see Error handling chart section for parameter description)</li>

![Daterange error](assets/images/daterange_error.JPG)

<li>No available package in the budget</li>

![Budgetrange error](assets/images/budgetrange_error.JPG)
</ul>

<h3>Future features</h3>
<ul>
<li>Adding flight upgrade option</li>
<li>Adding hotel upgrade option</li>
<li>Adding paid extras selection option</li>
</ul>

<h1>Technologies</h1>
Program was written in Python and is using customer Code Institute template with precoded html & js to run on Heroku.<br>
<h2>Used libraries</h2>
<h3>Built in libraries</h3>
<ul>
<li>os</li>
Used to clear the terminal
<li>random</li>
Used to generate random choice for free extras
<li>ast</li>
Literal_eval used to convert string lists to integer lists
<li>datetime
<ul>
<li>datetime module</li>
Used to convert input string to date format
<li>timedelta module</li>
Used to add date input restriction from 3 days ahead to within 1 year  
</ul>
</li>
</ul>
<h3>Installed libraries</h3>
<ul>
<li>google drive api and google sheets</li>
gspread, google.oauth2.service_account and Credentials<br>
Used to link the program to Travelbooka google sheet
<li>pyfiglet</li>
To create Travelbooka logo and booking reference number in ASCII
<li>colorama</li>
To use colors in the terminal for prompts, errors, return information
<li>tabulate</li>
To display data to user in neat tables in the terminal
</ul>
<h2>Other</h2>
<li>Google sheets on Google Drive</li>
To create and store Travelbooka sheet with program data
<li>Lucid charts</li>
To create flow charts
<li>Gitpod - template by Code Institute</li>
Code was written in run.py file in Gitpod and some testing done in
Gitpod terminal. The template with remaining files needed for the program
to run on Heroku was precoded by Code Institute.
<li>Heroku</li>
See deployment for more details


<h1>Testing</h1>
<h2>Functional testing</h2>
Functional testing of completed project is documented below.

![Test sheet 1](assets/images/testing1.JPG)
![Test sheet 2](assets/images/testing2.JPG)
[Test sheet can be viewed here](https://docs.google.com/spreadsheets/d/167-864up_5QZCAV0YeJn6JvQkENTWiXnJxntSCRleYs/edit?usp=sharing)

<h2>Validator testing</h2>

Project had been regularly checked with [CI Python Linter](http://pep8ci.herokuapp.com/), which showed some lines were too long. This had been corrected
and finalized project shows no linter errors. 

![Linter](assets/images/linter.JPG)

<h2>Bugs during creation</h2>

<ol>
<li>Validation issues</li>
The original code created for input validation with try/except would stop program from running and return error message with instructions
how to repeat step, but if empty input or string input were submitted the ValueError caused the program to exit/crash.
This was fixed by moving input request inside try statement and combining other try parameters.
<li>Eval</li>
Initially eval method was used to convert string list to integer list. While this didn't come up as error in CI linter and was only highlighted as
warning and not error in Gitpod, upon further reading it turned out eval poses valid safety concern. Eval was then replaced with literal_eval
from ast module. Testing showed that program functions as designed after this change.
<li>Terminal width after deployment</li>
Upon testing after deployment, it turned out that terminal is too narrow and package table design is distorted because of this. To remedy this,
table column width was decreased where possible and terminal width was changed from 80 to 100 in the index.html file. 
<li>Colors after deployment</li>
Colors in the deployed terminal are darker than displayed in Gitpod, which caused some bits to be less visible than intended. This was fixed by
changing random extra color from magenta to cyan and call us message to yellow. Font was made bolder to make booking reference and call us message
stand out more.
</ol>

<h1>Deployment</h1>
## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

<h1>Credits</h1>


