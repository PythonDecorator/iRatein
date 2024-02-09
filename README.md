# **iRatein chat app**

---

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)

The iRatein chat app is an application that allows users to communicate with each other in 
real time using text, images, emojis, or other media.

**Purpose of iRatein chat app**

- Connecting people who share common interests, hobbies, or passions.
- Enabling collaboration and teamwork among remote workers, students, or professionals.
- Enhancing customer service and support by allowing instant feedback and resolution.
- Facilitating social networking and community building by creating a sense of belonging and engagement.

<br />

> Features:
- ✅ `Server` Django, DRF, redis, Channels, websocket
- ✅ `Up-to-date dependencies`
- ✅ `Swagger` Api Documentation
- ✅ `DB Tools`: Django Models, `Django Migrations` (schema migrations),
- ✅ `Authentication`: Session Based, Auth Token
- ✅ `Deployment`: Google Cloud, Docker, Kubernetes

<br />

## Table of Contents
* [Get The Code](#get-the-code)
* [Docker Support](#docker-support)
* [Live App and Usage](#live-app)
* [Technical Support or Questions](#technical-support-or-questions)
* [Licensing](#licensing)

<br />

## Get The Code

> Get the code

```bash
$ git clone https://github.com/PythonDecorator/iRatein.git
$ cd iRatein
```

<br />

## Docker Support

> Run command to build Docker image
```bash
$ docker build .
```

> start server
```bash
$ docker-compose up
```

> other commands...

```
docker-compose run --rm server sh -c "python manage.py test"   # run tests
docker-compose run --rm server sh -c "flake8"   # run lint
docker-compose run --rm server sh -c "python manage.py makemigrations"
docker-compose run --rm server sh -c "python manage.py wait_for_db && python manage.py migrate"
docker volume ls # to see all the volume active
docker volume rm volume name # to remove a volume

docker-compose up # start server
docker-compose down # stop server
docker-compose run --rm server sh -c "python manage.py createsuperuser"

```

Visit `http://localhost:8000` in your browser. The app should be up & running.

<br />

## Manual Build

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working
> directory, with product source code.

### 👉 Set Up for `Unix`, `MacOS`

> Install modules via `VENV`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

### 👉 Set Up for `Windows`

> Install modules via `VENV` (windows)

```
$ virtualenv venv
$ .\venv\Scripts\activate
$ pip install -r requirements.txt
```

## Live App

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, etc.)
- Internet connection

### How to Use the app

1. Create Accounts:
Open the chat app in one browser window.
Click on the "Register" button and create two user accounts.

2. Login:
After creating accounts, log in to the chat app using the provided credentials.
you will bw redirected to the home page. Create a chat room eg: hello, and start chatting

3. Open Private Windows:
Open a new private or incognito window in your browser.
Navigate to http://35.233.182.253:8000/

4. Log in with Different Accounts:
In the new private window, log in with the second user account you created.

5. Start Chatting:
Enter the name of the chat room you created eg: hello
In one window, initiate a chat by selecting the second user from the user list.
Switch to the other window and respond to the chat.

**Notes:**
- Ensure that both accounts are logged in on separate browser windows for an interactive experience.
- Ensure the chat room is the same.

- Click the link below to use the app.
### 👉 [iRatein Chat App](http://35.233.182.253:8000/)

<br />

## Technical Support or Questions
Feel free to reach out `okpeamos.ao@gmail.com` if you encounter any issues or have question.

<br />

## Licensing

- Copyright 2024 - present [PythonDecorator](https://github.com/PythonDecorator)

<br />

## Social Media

- Twitter: <https://twitter.com/AmosBrymo67154>
- Instagram: <https://www.instagram.com/pythondecorator>

<br />

---
Provided by PythonDecorator
