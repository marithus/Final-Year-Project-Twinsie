# Final Year Project
Twinsie is live.
http://twinsie-ac751fa5d700.herokuapp.com/

## Disclaimer:
To use the chat feature, you will need to change to Http in order to chat.

## Features :
<li>Sign Up, Login, OAuth 2.0(Google, Github) </li>
<li>Intuitive UI and UX design</li>
<li>reCaptcha v2</li>
<li>Logout, Forgot Password</li>
<li>Create, Edit, Delete Posts with customized text, pictures and links</li>
<li>Like, Comment / Reply, Save and Search Posts</li>
<li>Follow and Unfollow users to view their Content</li>
<li>Friend Request</li>
<li>Notifications</li>
<li>Chats</li>
<li>Video Calls using Agora</li>
<li>Public Profile view</li>


## Test user login:
<li>User1:Twinsie1</li>
<li>User2:Twinsie1</li>


## Installation Locally:
To run on your local machines, run these commands (Windows Only)
```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv) pip install -r requirements.txt
    (venv) cd Final-Project-Year-Twinsie
    (venv) python manage.py makemigrations
    (venv) python manage.py migrate
    (venv) python manage.py createsuperuser
    (venv) python manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```
