# EventConnect

EventConnect is a  platform that brings event organizers and students together. Organizers can easily create and manage their events, and students can find and register for those events with just a few clicks. It is simple, fast, and secure.

# 🚀 Deployment

We use modern cloud tools to keep the project fast and reliable:

* **Frontend:** Hosted on **Vercel** so the website loads very fast for everyone.
* **Backend:** Hosted on **Render** to run our server smoothly.
* **Database & Images:** Powered by **Supabase**. We use it to store our data safely and to save user and event images.

---

# 💻 Frontend 





### `Home_Page_2.html`
**Purpose:** The main welcome page of our website.<br> 
**Features:** 
* **Navigation Bar:** Has easy-to-click buttons to "Log in" or "Register" at the very top.
* **Welcome Banner:** A large, beautiful area that grabs attention and tells visitors what EventConnect is all about.
* **Counter Box:** Shows real-time statistics (like the total number of events, users, or successful registrations).
* **Latest Event Details:** A special section that highlights the newest, most popular, or upcoming events.
* **Why EventConnect:** A text section explaining the goals, mission, and benefits of using the platform.
* **Developer Info / Footer:** A bottom section that provides links to the team, contact info, and social media pages.

### `Login_2.html`
**Purpose:** The page where users sign in securely.<br> 
**Features:**
* **Login Form:** Clean input boxes to type in your email and password.
* **Toggle Switch:** A button that lets you easily switch back and forth between "Student Login" and "Organizer Login".
* **Remember Me:** A small checkbox option to keep you logged in on your device.
* **Forgot Password Link:** A text link that takes you to a secure password recovery screen.
* **OTP Verification:** A special feature that sends a secret code to your email and provides a box to safely type it in and reset your password.

### `Events_Page.html`
**Purpose:** The place to discover new events.<br>
**Features:**
- **Search Bar:** A large text box where you can type things to search for specific event names.
* **Filter Options:** Dropdown menus or buttons that let you sort events by specific dates, categories, or by the organizer's name.
* **Event Cards:** Displays all upcoming events in a nice, organized grid. Each card shows the event image, title, date, and location.
* **View Details Button:** A clear button on every single event card that takes you to the full description page.

### `Event_Details.html`
**Purpose:** The page that shows everything about one specific event.<br>
**Features:**
* **Big Banner Picture:** Displays the main promotional image for the event at the very top of the page.
* **Information Section:** Clearly shows the event date, start time, physical venue/location, and a very detailed text description.
* **Rules & Guidelines:** A specific text box explaining what to bring or what is not allowed at the event.
* **Registration Stats Box:** Shows how many seats are left before the event is completely full.
* **Register Now Button:** A large, highly visible button for students to instantly join the event.

### `Developer_Details.html`
**Purpose:** A page showing the team who built this project.<br>
**Features:**
* **Glass-Style Cards:** Beautiful, modern cards for each team member.
* **Profile Pictures:** Shows the faces of the developers who built the project.
* **Contact Information:** Clearly lists the email addresses and roles for the team.
* **Social Links:** Interactive buttons that link directly to GitHub, LinkedIn, or other social media websites.

---
## 🏢 Organizer Portal

### `Organizer_Registration.html`
**Purpose:** The sign-up page for people who want to host events.<br>
**Features:**
* **Organization Form:** Input boxes for the company or organizer name, official physical address, and phone number.
* **Official Email Input:** Requires a real email to ensure the organizer is a real business or person.
* **Password Creator:** Secure fields to create and verify a strong password.

### `Organizer_Dashboard.html`
**Purpose:** The main control center for event organizers.<br>
**Features:**
* **Welcome Banner:** A personalized greeting recognizing the organizer.
* **Counter Boxes:** Large statistic numbers proudly showing "Total Events Created" and "Total Participants Registered".
* **Recent Events List:** A quick preview list of the last few events they created.
* **Shortcut Buttons:** Large colorful buttons providing instant access to "Create New Event", "View Participant Lists", and "Edit Profile".

### `Create_Event.html`
**Purpose:** The tool to make a new event.<br>
**Features:**
* **Event Details Form:** Input boxes to type in the new event title, event category, and precise date/time.
* **Capacity Box:** A number input to set a strict limit on how many students are allowed to join.
* **Description Area:** A very large text box to write out the rules, guidelines, and main event description.
* **Banner Upload Button:** A file chooser button to upload the main promotional image for the event directly to the cloud.
* **Submit Button:** A final "Create Event" button to save the entire form to the database.

### `Organizer_MyEvents.html`
**Purpose:** A list of all events managed by the organizer.<br>
**Features:**
* **Events Grid/List:** Displays a catalog of all the events the organizer has ever created.
* **Status Labels:** Shows if each event is currently accepting registrations, closed, or passed.
* **Action Buttons:** Every single event has clear buttons attached to it that let the organizer "Edit Event", "View Participants", or "Delete Event" securely.

### `Organizer_EditEvent.html`
**Purpose:** The page to change details of an existing event.<br>
**Features:**
* **Pre-filled Form:** Automatically fills all the input boxes with the old event information so you don't have to retype anything.
* **Text Editors:** Easy ways to safely change the text schedule, rules, or description.
* **Image Replacement Button:** A button to upload a brand new banner image which will automatically override and delete the old one.
* **Save Changes Button:** A big button to apply the updates immediately.

### `Organizer_Participants.html`
**Purpose:** The page to manage the students who signed up.<br>
**Features:**
* **Search Bar:** Lets the organizer quickly type and find a specific student's name or college ID.
* **Filter Tools:** Dropdown boxes to sort and organize the long list of registered students easily.
* **Participant Table:** A large, clean data grid showing the names, emails, and details of everyone who joined.
* **Export Data Button:** Allows the organizer to download the list of students to use for door check-ins or paper reports.

### `Organizer_Profile_2.html`
**Purpose:** The organizer's personal settings page.<br>
**Features:**
* **Profile Picture Display:** Shows the company's logo or the organizer's photo.
* **Update Form:** Input boxes to change the organization's public name, phone, and contact details.
* **Upload New Logo Button:** A button to pick and update their main profile picture.
* **Change Password Section:** Boxes to securely type and verify a completely new password.

---

## 🎓 Student Portal

### `Student_Registration.html`
**Purpose:** The sign-up page for new students.<br>
**Features:**
* **Sign-up Form:** Input boxes asking for the student's name, official email, and phone number.
* **College Details:** Specific boxes to type out your university name and your official student ID.
* **Password Creator:** Secure boxes to create and confirm a strong password.
* **Back to Login:** A quick link button at the bottom just in case you already have an account.

### `Student_Dashboard.html`
**Purpose:** The main home screen for a logged-in student.<br>
**Features:**
* **Welcome Banner:** A personalized greeting message displaying the student's name.
* **Quick Stats Box:** Shows counter numbers, like how many total events you have joined so far.
* **Recent Activity Section:** Shows a small, quick list of upcoming events you are participating in.
* **Quick Action Buttons:** Large, colorful shortcut buttons to edit your profile, discover new events, or view your past registration history.

### `Student_Event_Registrations.html`
**Purpose:** A history of the student's events.<br>
**Features:**
* **Registration List:** A clean table or list showing every single event the student has signed up for.
* **Status Indicators:** Small colored badges showing if the registration event is "Upcoming", "Active", or "Completed".
* **Event Dates:** Clearly keeps track of when each event will happen so you do not forget.
* **View Event Links:** A button next to each registration to quickly jump back to the event's detailed information page.

### `Student_Profile_2.html`
**Purpose:** The student's personal settings page.<br>
**Features:**
* **Profile Picture Display:** Shows your currently saved profile photo.
* **Image Upload Button:** Lets you pick a new picture from your computer/device to save directly to the Supabase cloud.
* **Personal Info Form:** Input boxes to change your name, phone number, or college details at any time.
* **Security Section:** A specific area with a "Change Password" button to update your login securely.
* **Save Changes Button:** A big button that updates everything in the database safely at once.

---


# Backend API Overview

How our server logic is built using **FastAPI** to connect the website correctly with our database.

## 📁 Core Files

### `main.py`
**Purpose:** The starting engine of our FastAPI server.<br>
**Key Responsibilities:**
* Turns on the FastAPI server instance.
* Allows the frontend website to communicate with it safely.
* Connects all the different web link routes (students, organizers, events) together.

### `database.py`
**Purpose:** The bridge to our database.<br>
**Key Responsibilities:**
* Connects our app to the Supabase database.
* Manages the connections so we can save and read information safely.
* Maps python objects to database tables securely.

### `models.py`
**Purpose:** The blueprint for our database tables.<br>
**Key Responsibilities:**
* Tells the database exactly how to organize our data.
* Sets up the tables for "Student", "Organizer", "Event", and "Registration".
* Links these tables together correctly so data is organized.

### `schemas.py`
**Purpose:** The security guard for our data.<br>
**Key Responsibilities:**
* Checks all the data coming in (like form inputs) to make sure it is correct.
* Ensures bad data is rejected before saving it to the database.
* Sets the rule for how data is sent back to the website.

---

##  API Routers (`/routers`)

### `student_module.py`
**Purpose:** Handles everything a student can do in the app.<br>
**Key Responsibilities:**
* Controls student login, forgot password features, and account creation.
* Fetches the data needed to show on the student's dashboard.
* Handles updating profiles and saving profile pictures.

### `organizer.py`
**Purpose:** Handles everything related to event organizers.<br>
**Key Responsibilities:**
* Controls the unique organizer login process.
* Creates new organizer accounts.
* Securely updates their company profile and passwords.

### `events.py`
**Purpose:** The main system that handles the events.<br>
**Key Responsibilities:**
* Lets organizers create, edit, or delete events and upload banners.
* Lets students register for events and makes sure the event is not full.
* Helps display the correct and filtered events perfectly on the public pages.
* Gives organizers the list of students who registered for their events.
