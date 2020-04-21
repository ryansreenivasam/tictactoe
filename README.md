# Tic Tac Toe

This game of tic tac toe is composed of a Vue frontend and a Django backend that are completely separated.  The frontend and backend communicate via API.

The Vue frontend only displays the contents of the game board and makes API requests when the player makes a move.  

To run the Vue app you will need npm installed.

### Install Vue dependencies
```
npm install
```

### Start development server
```
npm run serve
```

The django backend handles API requests from the frontend and computes the AI opponent's next move.

To run the Django app you will need pip installed.

### Install Django dependencies
```
pip install -r requirements.txt
```

### Start development server
```
python manage.py makemigration
python manage.py migrate
python manage.py runserver
```

