# Ebba's Hair

Ebba's Hair is a website for a hair salon called "Ebba's Hair". It has a page where the user can read more about the stylists who are available for bookings and the different services they offer. There user is also able to find information about where the salon is located, their phonenumber and their email-address. The user is also able to book an appointment online.

Ebba's Hair is not a real salon so the contact information and the stylists are fictional and just for the sake of this website.

## The website on different screensizes

![The website on different screensizes](documentation/homepage-responsive.png)

Since I have used Bootstrap container, rows and collumns, an expandable navbar and % width on images the website adapts beautifully to different screensizes.

## The Color Scheme

![The color scheme](documentation/ebbas-hair-color.png)

For this project I choose five shades of a brownish grey color that I used across the whole website.

## The Font

I used the Google Font "Comfortaa" for all the text found on the website. It suited my vision best.
## Features

### Favicon

In the tab for the website there is a custom made favicon with the same font and color scheme as the rest of the website. ![Favicon](documentation/favicon-screenshot.PNG)

### Navigation Bar

The navigationbar contains links to all the different pages depending on if you are authorized or not. When the screen width is under 992px the unorderd list becomes a dropdown menu with a toggle button to the right of the header. 

There are bootstrap classes called 'nav-link' and 'active'(if the url is active) on all the links in the navigationbar that increases the opasity of the color of the text when hovering over and for when a page is active.


The navbar on different devices when the user is not authorized.
![Navbar big screen(unautorized)](documentation/navbar-wide-loggedout.PNG)
![Navbar small screen](documentation/navbar-small.PNG)

![Navbar dropdown menu(unautorized)](documentation/navbar-dropdown-loggedout.PNG)

The navbar on different devices when the user is authorized.
![Navbar big screen(authorized)](documentation/navbar-wide-loggedin.PNG)
![Navbar small screen](documentation/navbar-small.PNG)

![Navbar dropdown menu(authorized)](documentation/navbar-dropdown-loggedin.PNG)

A gif that shows how the navbar reacts to the user hovering over the page links.

![Navbar text change color](documentation/navbar-hover.gif)
 

### Header

The header of the page is only visible on the homepage and the aboutpage. This is purely for aestetich reasons.

![Header homepage](documentation/header-homepage.PNG)
![Header aboutpage](documentation/header-aboutpage.PNG)

### Homepage

The homepage contains a welcoming message that tells the user to come in and relax. The user can also see their opening hours and their contact information. The address for the salon is a link to the address on Google Maps.

![Homepage big screen](documentation/homepage-wide.PNG)
![Homepage small screen](documentation/homepage-small.PNG)

### Aboutpage

On the aboutpage the user can read more about the salons different stylists. They can also see the stylists speciality and their price. The data for the aboutpage comes from the custom model called StylistList. The stylists are added to the page using a for loop in the template. This for loop is inspired by the 'Thorin and his company' flask walkthrough project. The admin can add new stylists or mark stylists as inactive using the django admin page to hide them from the aboutpage. 

![Aboutpage big screen](documentation/aboutpage-big.gif)
![Aboutpage small screen](documentation/aboutpage-small.gif)

### Register

The register page is a allauth django model, form and template. The user is asked to fill in their email address, the username they want and a password that fullfills the criteria stated. The user is then asked to repeat the password to confirm it before they will click on the submit button bellow to register as a user.

Bellow the form there is a paragraph saying that if they already have an account they can follow the link in "Sign in here!" to get to the log in page.

![Register big screen](documentation/register-big.PNG)
![Register small screen](documentation/register-small.PNG)

If the user where to forget to fill out a field they will get an alert that tells them that they need to fill out for example the email address field. The user will also get an alert if they enter an email address without an @ in it.

![Register fill out the field](documentation/email-fillin.PNG)
![Register not an email](documentation/email-include.PNG)

If the user tries to register with an email thats already connected or a username that is already taken they will be informed of this and asked to change it.

![Register email and username taken](documentation/register-unavailable.PNG)

Bellow you can see a register form filled out successfully. The user is redirected to the homepage and notice how the navbar changes due to the user being authorized.

![Register successfully](documentation/register-success.gif)

### Log in page

The log in page is just like the register page a allauth django model, form and template. At the top of the page there is a message that explains that the user needs to be authorized for them to be able to book an appointment. There is also a link to the register page if the user does not have an account yet. 

The form contains a field for the username and a password field. The user can also check the box asking to be remembered. 

![Log in page big screen](documentation/login-wide.PNG)
![Log in page small screen](documentation/login-small.PNG)

If the user enters the wrong username or password they get a message telling them that it was incorrect. Notice that the username field is case sensetive as the username we registered with is "Frida123" and not "frida123" as in the picture bellow.

![Log in unsuccessfull](documentation/login-wrong.PNG)

When the username and the password is correctly entered the user is redirected to the homepage and they get a Bootstrap toastmaker message to the top right saying that they are succesfully logged in as, in this case, Frida123.

![Log in successfull](documentation/login-success.gif)

### Booking page

The booking page is a custom django model, form and view. The user needs to choose which stylist they want to meet at what day and what time. The user is also able to attach a comment to their booking if there is something the stylist need to know ahead of the appointment but this textfield is optional. 

![Booking page big screen](documentation/booking-wide.PNG)
![Booking page small screen](documentation/booking-small.PNG)

The stylist list contains all the active stylists.

![Stylist list](documentation/booking-select-stylist.PNG)

The date field shows as a calendar where the user can pick the day they want to visit the salon. The appointment can not be booked in the past or on a weekend.

![Calendar](documentation/booking-select-day.PNG)

The time field contains a list of time choices to stop the user from booking an appointment at a weird time or a time outside of the salons opening hours. This field is also checked so that it is not in the past.
![Time list](documentation/booking-select-time.PNG)

The comment field is as previously stated optional to fill out.
![Comment field](documentation/booking-comment.PNG)

If the user missed to choose a stylist or if they chose a day in the past or a time slot that is already taken with that stylist they will get a toast message to the top right explaining why they can not book the requested appointment. When the form is filled out correctly and the user chooses a time slot that is available they get a toast message that the appintment has been booked and they are redirected to "My page".

In the gif bellow you can see this in action.

![Booking process](documentation/booking.gif)

### My page

My page is the page where the user can change their email address and see and change their appointments. This page contains two divs containing forms. 

![My page big screen](documentation/mypage-wide.PNG)
![My page small screen](documentation/mypage-small.PNG)

The custom EmailUpdateForm form gets the email from the django User model so the user can see their current email and there is a email field where the user can change their email address.

![Update email form](documentation/mypage-emailfield.PNG)

The booking form only shows up if the user has a booking in the future. The user sees the date, time and selected stylist of their current booking and then there is a date field and a time field so the user can make changes to their booking if they would need to. They can also delete their booking if they want to. The forms are rendered using a for loop so if a customer has multiple bookings they will all show up.

![My page booking form](documentation/mypage-booking.PNG)

If there is an issue when the user tries to change their appointment, maybe the stylist is taken that time or they try to make the new booking on a weekend the user will get a toat message explaining the problem. 

![Changing a booking process](documentation/change-booking.gif)

### Log out page

The log out page is an allauth django model etc just like the register and log in page. Here the user is asked if they are sure they want to log out and then there is a submit button they can click if they are sure. After they click 'log out' they are redirected to the homepage and get a toast message that they have signed out.

![Log out page](documentation/logout-form.PNG)
![Toast message](documentation/logout-success.PNG)

### Bootstrap Toasts

In the base.html template there is a div that with the help of some javascript and a if statement and a for loop displays error and success messages in the top right corner. 

![Multiple toast messages](documentation/toastmessages.gif)

### Footer
At the bottom of all the pages there is a footer containing links in the form of fontawesome icons. The links open in a new page. Bellow the links the creator of the website is stated.

![Footer](documentation/footer.PNG)