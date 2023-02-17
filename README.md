![Logo](assets/images/logo.JPG)

<h1>Overview</h1>
Travelbooka is an program using "do it yourself" philosophy to create user's own travel package based on
parameters stored in Google sheets. In real world this could be used by a travel agency to allow user to 
mix and match flight and hotel offers to create their own unique bookings. 
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
<h1>Features</h1>
<h1>Technologies</h1>
<h1>Testing</h1>
<h1>Deployment</h1>
## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

<h1>Credits</h1>


