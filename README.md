# Introduction <br>
## The Email Generator

This application is used to help generate emails with a style of the user's choice. Whether it be sending an email to your professor requesting an extension for that project worth half your grade, or emailing a childhood friend to catch up, this generator has got you covered:
1. User picks a tone (or tells our Gemini API a tone) for the email. 
2. The Gemini API generates a personalized email for the user.
3. The user is then prompted to modify the email with the recipient's and sender's details, and then hits "send" for it to arrive to the recipient's inbox.


For more details, please view our project proposal [here](https://docs.google.com/document/d/1HD8HK9ETS648CsefJGBGJE0E4yZjM3jkYPysLFYLPHQ/edit?usp=sharing).

# Technical Architecture
<img width="1416" height="1054" alt="image" src="https://github.com/user-attachments/assets/8bd4eeef-2e74-42a1-b98d-af73e650723d" />




# Developers
Chandini Chennakesavan: Integrating the Gemini API with the email wrapper for UX.  <br>
Mahnoor Aetzaz: Created email templates, added text options and email recipient/sending.<br>
Meera Aleem:  Integrated light and dark mode for UI, saving email drafts, and improving upon email clarity. <br>
Moukthika Nellutla: Integrating email-sending feature to mentioned recipient(s), modifying email structure for UX. 


# Environment Setup
## Cloning the Repository
Make sure to have python already installed on your machine:
```bash
-pip install python
```

Navigate to your source directory, and clone the repository:
```bash
git clone https://github.com/CS222-UIUC/fa25-fa25-team019-CM3.git
```


# Project Instructions
Go into the backend directory of the project:
```bash
cd backend
```

Then, run the following command to load the webpage and click on the link:
```bash
python app.py
```
Follow the instructions on the website accordingly.





