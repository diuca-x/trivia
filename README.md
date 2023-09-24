# Trivia Game



This is a trivia game where you are given one option and have to choose the correct answer among three. The game is made with Flask-SQLAlchemy in the backend, Poetry as the package manager and React and vite in the frontend. 


## Getting Started ##
To get started, you will need to have Python 3.8+ installed. You can install the dependencies by running the following commands:

```cd trivia-front/back```

```poetry install```

```poetry shell```

This will install all the dependencies in the poetry.lock file and create a virtual environment.

Then for starting the backend 

```python app.py```

Once the dependencies are installed, you can start the front by running the following commands:

```cd trivia-front```

```npm install```

```npm run dev```

create a .env file in the trivia-front folder with the variable SQLALCHEMY_DATABASE_URI="your database url"  and another one with the name VITE_BACKEND_URL="the url of your backend"
  
Then for setting up the db (inside the poetry shell)

```flask db init```

```flask db migrate```

```flask db upgrade```

## Features ##
The trivia game has the following features:

- you can load the questions either by making a call to the api with an app like postman or by using the /auth routes that make an admin interface using the back-end URL.
-  First you would need to create an admin user using the /auth/signup url, but since it's protected you could either remove the jwt_required line to create the user or you could create it from within the database. (i suggest the first one since the password will be encrypted, if you create it from the db you would need to put the encryption not the password)
-  Then in the admin interface you can upload an excel file with the questions and options to put in the db
The file needs to have the next structure:
. 1st row: question, answer, options, date.
   the answer must not be in the options and there must be at least two options, and the date must be in the format
   dd-mm-yyyy or dd/mm/yyyy
. 2nd and next rows the questions, answer options(separated by a ,) and date themselves
- Now once started, the game always loads 10 questions from the db with todays date

In the game itself you will see

. Three answer choices for each question

. A scorecard to track your progress

. A clock to track how much time it takes to answer all 10 questions

. A hint option to remove one incorrect answer

## To-Do ##

The following are some things that I plan to add to the trivia game in the future:

More trivia questions
Different difficulty levels
The ability to create custom trivia questions
The ability to share your score with friends
A leaderboard to see how you compare to other players
