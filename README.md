# Real-Time Stock Market Price Checking App Built Using Django, Celery, Django-Channels, WebSockets.

![Made with love in India](https://madewithlove.now.sh/in?heart=true&colorA=%232543d4&colorB=%23f58f00&template=for-the-badge)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## About Project 📄
This Real-Time Stock Market Price Checking App Built Using Django, where user can select the one or multiple stocks from the list and can check their price in Real-time which updates frequently. It Store the User Session ID in the database on temporary basis. Session ids are further used to send data to user.

## Project Functionalities ⚙
  - No Login/Signup required.
  - Select the Stocks to Watch for.
  - Click on `Submit` button to see their Real-time prices.
  - Click on `View Details` button to see more details of the given Stock.
  - `Django-Sessions` to track the User Selected Stocks on a temporary basis.

## Technologies Used 👨‍💻
- `Django` - For Coding Backend of Application.
- `Django-Celery` - To Add the tasks in the Queue.
- `Celery-beat` - To add tasks to Queue
- `Memurai/Redis` - It is used as a Message Broker & For Adding a Django Channel Layer in Backend.
- `Django-Channels` - For using `WebScokets` to establish Real-time Communication, to update the Stock Price Regularly.
- `SQLite` - Used this Default DataBase for Storing Data on temporary basis.
- `DTL` - Django Template Language for Building Dynamic Pages.
- `JavaScript` - For Integrating Additional functionalities in Project.
- `Bootstrap 5` - For UI Development of Project.
- `FontAwesome` - For embedding icons in Project.
- `HTML/CSS` - For Coding Basic Templates of Project.

## Demo Of Application
To Watch the Live Demo Of Application click on the Below Given Link.
[View Demo](https://www.linkedin.com/posts/chinmayagrawal775_python-django-djangodeveloper-activity-7055530943628947456-CglY) 🚀.

### Here Are Some ScreenShots of The Application

<img src="https://user-images.githubusercontent.com/62383314/233631641-bc0fb6ed-f63a-4a24-ac22-2818f2e26dc6.png" alt="drawing" width="49%"></img>
<img src="https://user-images.githubusercontent.com/62383314/233631648-7aa83b87-5dc6-4fdf-ba86-9496e6b309d0.png" alt="drawing" width="49%"></img>
<img src="https://user-images.githubusercontent.com/62383314/233631655-71a42866-53b3-483b-8c1b-41ccc5c4eb82.png" alt="drawing" width="49%"></img>
<img src="https://user-images.githubusercontent.com/62383314/233631633-606f18e3-eb78-400b-8a6b-600ef50aa017.png" alt="drawing" width="49%"></img>

## How to Run This Application on local Server
To run this application on your local development server you need to run the following commands. Run Each Command in the new Terminal. (These commands are for Windows OS)

To Run the Django Development Server :
```BASH
python manage.py runserver
```
To Start the Celery Worker :
```BASH
celery -A stockmarket.celery worker --pool=solo -l info
```
To Start the Celery Beat Scheduler :
```BASH
celery -A stockmarket beat -l INFO
```

> Note: In case if there are uncompleted tasks in left in the queue, due to which it is sending old details of stocks, then you need to clear the queue using the below command.
```BASH
celery -A stockmarket purge -f
```


## Note
If You are Learner, or Want to test this application, Then After Forking & Cloning, You Can use these `Test Credentials` for accessing the Admin Panel of Application to see how it stores `User Sessions` on temporary basis.

``` PYTHON
- #### FOR ADMIN LOGIN ####:
  - ID : admin
  - PASSWORD : admin
```