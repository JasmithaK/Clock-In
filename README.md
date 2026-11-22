**1. Project Overview:**
Clock In is a web-based study tracking application developed using Python, Flask, and SQLite. The purpose of the project is to help students manage their study schedules, record the time they spend working on different courses, and better understand their study habits.

The application allows users to create and organize courses, record individual study sessions, add optional notes, and review their previous study activities. It also provides basic statistics, such as total study time and the amount of time spent on each course.

The project combines several important areas of software development, including web application development, database management, CRUD (Create, Read, Update, Delete) operations, user input validation, and basic data analysis.


**2. Project Objectives:**
The main objective of Clock In is to create a simple and practical tool that encourages students to become more organized and aware of how they spend their study time.

The specific objectives include:
  1. Developing a functional web application using Flask and Python.
  2. Allowing users to create and manage courses.
  3. Providing a way to record study sessions with dates, durations, and optional notes.
  4. Storing information in an SQLite database.
  5. Allowing users to view, edit, and delete previous study sessions.
  6. Calculating total study time and generating course-specific statistics.
  7. Creating a clean, organized, and user-friendly interface.
  8. Practicing version control and software development using Git and GitHub.


**3. Development Process:**
The development of Clock In follows a step-by-step approach, beginning with planning and database design before moving into application development, testing, and documentation.

The project is divided into several stages to make development more manageable and ensure that the essential features work before additional features are introduced.

The first stage involves identifying the application's requirements and determining which features are necessary for the minimum viable product (MVP). The next stage focuses on designing the database structure and building the basic Flask application.

After establishing the foundation, individual features are developed and connected to the database. These include course management, study-session recording, session history, editing and deletion, and study-time calculations.

The final stages focus on improving the user interface, testing functionality, fixing errors, organizing the source code, and preparing project documentation.


**4. Technical Methods & Tools:**
Clock In uses a simple three-part architecture consisting of the frontend, backend, and database.

*Backend – Python and Flask*
- Python is used as the primary programming language, while Flask provides the framework for handling         application routes, processing user requests, and communicating with the database.
- Flask connects the different pages of the application and determines what information should be displayed   or processed when a user interacts with the website.

*Frontend – HTML, CSS, and JavaScript*
- HTML is used to structure the application's pages, including the dashboard, course list, study-session      form, and session history.
- CSS is used to create a consistent appearance, improve readability, and make the application easier to      navigate. JavaScript provides additional client-side functionality where needed.

*Database – SQLite*
SQLite is used to store course information and individual study sessions.

The database consists primarily of two tables:

  -Courses: Stores course information, including a unique course ID and course name.

  -Study Sessions: Stores individual study records, including a session ID, associated course ID, study        date, duration in minutes, and optional notes.

The two tables are connected through a foreign key relationship. This allows each study session to be associated with a specific course.


**5. Application Features & Functionalities:**
Clock In is designed around three main areas: course management, study-session management, and study statistics.

- Course Management
  Users can create courses and view their existing course list. Each course acts as a category for            organizing study sessions. Users can also delete courses when they are no longer needed.

- Study-Session Management
  Users can create individual study-session records by selecting a course, entering the study date,           providing the amount of time studied in minutes, and optionally adding notes. The application also allows   users to review previous sessions, edit existing records, and delete sessions they no longer need.

- Study History and Filtering
  The session history page displays previously recorded study activities. Filtering functionality allows      users to narrow their results by course or date, making it easier to review specific periods of studying.

- Dashboard and Statistics
  The dashboard summarizes the user's study activity by calculating total study time and time spent on        individual courses.
