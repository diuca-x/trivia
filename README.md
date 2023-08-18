# Trivia Game



This is a trivia game where you are given one option and have to choose the correct answer among three. The game is made with Flask-SQLAlchemy in the backend, Poetry as the package manager and React and vite in the frontend. 


Getting Started
To get started, you will need to have Python 3.8+ installed. You can install the dependencies by running the following commands:

```cd back```

```poetry install```

```poetry shell```

This will install all the dependencies in the poetry.lock file and create a virtual environment.

Then for starting the backend 

```python app.py```

Once the dependencies are installed, you can start the front by running the following commands:

```cd trivia-front```

```npm install```

```npm run dev```

create a .env file int the root with the variable SQLALCHEMY_DATABASE_URI="your database url"  and another one inside the trivia-front folder with the name VITE_BACKEND_URL="the url of your backend"
  
Then for setting up the db

```flask db init```

```flask db migrate```

```flask db upgrade```

Features
The trivia game has the following features:

A variety of trivia questions
Three answer choices for each question
A scorecard to track your progress
A leaderboard to see how you compare to other players
To-Do
The following are some things that I plan to add to the trivia game in the future:

More trivia questions
Different difficulty levels
The ability to create custom trivia questions
The ability to share your score with friends
