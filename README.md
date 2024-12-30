# Birdclopedia : An Entry Gate to the Avian World
#### Video Demo:  <[YT](https://youtu.be/9XTBNnywM28)>
#### Description:
Birdclopedia is a Flask-based web application designed to serve as a general digital encyclopedia dedicated to the avian species. The website aims to offer an engaging and educational experience for bird enthusiasts, students, and anyone curious, around the world. The application organizes bird species into five primary groups: Birds of Prey, Waterbirds, Songbirds, Shorebirds, and Game Birds. Each group showcases distinctive members, complete with detailed descriptions, unique characteristics, and fascinating fun facts.
As of right now, the website features birds such as:
- Owls and Eagles for Birds of Prey
- Gulls and Ducks for Waterbirds
- Robins and Hummingbirds for Songbirds
- Pheasants and Turkeys for Game Birds
- Sandpipers and Plovers for Shorebirds
At its core, Birdclopedia aims to blend simplicity and functionality. For this project, i used Flask for backend operations, SQL as the database engine, and Tailwind CSS for a clean and modern design. The navigation is served through a tree-like structure of the website, allowing users to easily explore bird families and their members, while also providing basic backend features such as user registration, login, and profile management.
Beyond serving as a digital reference, Birdclopedia was designed targeting a sense of community among bird enthusiasts by enabling users to customize their profiles and giving them an accessible "Wiki" that can even be introduced to kids and young people as a gateway to learn about the avian families. The web is very much designed for users to return, explore, and contribute to the growing database of avian knowledge.
The website offers these as the key features:
- Dynamically structured page for exploring detailed pages for each bird family and their members, including high-quality images, fun facts, and characteristics. Usage of Jinja and HTML templating can make development of further species easy, allowing expansion of the encyclopedia
- Flask and JS is used to make sure users can login and have secure accounts (albeit, admittedly, cybersecurity measures aren't very much checked right now :grin)
- Users can create profiles, add a personal bio, and mark favorite bird families.
- Tree structure allows easy navigation across bird groups and subcategories.
- Using Tailwind CSS, the website adapts seamlessly to various devices, so users can access it through almost anything.

#### Project Structure

1. app.py
Acts as the main backend driver of the application. App.py itself manages all routing operations, including home, login, registration, profile, and bird family pages using Flask. This file also handles user authentication, profile updates, and database interactions.
Routes include:
/ – Home page
/tree – Overview of bird groups (characteristic-based)
/tree/<family> – Detailed pages for each bird family, 5 right now
/register – User registration
/login – User login
/profile – User profile management / customization
/logout – Logout functionality

2. templates/
This directory, following CS50's recommendations, contains HTML templates for rendering pages using Flask's Jinja2 templating feature.
For this project, the key templates include:
index.html – Homepage layout.
tree.html – Overview of bird families.
family.html – Dynamic page for bird families (e.g., Birds of Prey).
register.html – User registration form.
login.html – User login form.
profile.html – User profile management page.

3. static/
Static contains assets regarding styles and images that are used for customizing the page's visuals. This mainly deals with CSS and PNGs / JPGs
style.css – Contains Tailwind CSS customizations.
Images for different bird groups and logos.

4. users.db
SQLite database file.
Contains tables for user authentication (users) and profile data (bio, favorites).

5. README.md

This documentation file, providing insights into the project structure, features, and design choices.

#### Design Choices

Database Design
SQLite was chosen due to its simplicity and integration with Flask. The users table includes essential fields like id, username, password, bio, and favorites.

Passwords are currently stored in plain text (could be enhanced with hashing mechanisms like bcrypt).

Styling with Tailwind CSS
Tailwind CSS was selected for its flexibility and utility-first approach. It also allows rapid prototyping and consistent design across all pages. As compared to Bootstrap, i simply picked Tailwind because it is more commonly used around me (Jakarta)

User Experience
Simple navigation structure ensures users can easily move between families, profiles, and other pages. Interactive elements, like clicking on bird family cards, make exploration intuitive.

Error Handling
Here, simple flash messages are used for notifying users of errors, warnings, or successes. Form validations ensure no critical fields are left empty.

#### Further Development

For the future of this project, i plan to add a couple things to encourage and ease expansion. Such as a page editor to help users not familiar with programming expand the pages available, a feature for adding friends / other users, and a more consistent styling on the website (maybe using Figma?), but as of right now, the project hopefully already shows the vision i'm aiming for.