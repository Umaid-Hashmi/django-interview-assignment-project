Basic Installations :
The first step to start up the project is to install python by downloading python using the url https://www.python.org/downloads/.
Make sure you have added the path variable of python to the systems properties enviornment variables .
The next step is to install django by running the command pip install django in the command prompt.

Starting the Project:
Now, change the current directory to desktop or any other desired location to save the django project by running the command cd Desktop or likewise.
Then run the command django-admin startproject name_of_the_project(which in my case was pustakaalay_project)
Now run the command cd name_of_the_project, to change the current directory to the project .
From now onwards, the command line utility for the project work will have python3 for ios, python or py for windows.I am using py because I have windows system. So choose accordingly
Now run the command py manage.py startapp name_of_the_app(which in my case was pustakaalay_app).

Working on the Project:-

Now open up the project in an IDE like Pycharm or any code editor like VS Code.
Now Create the virtual enviornment by either using the base system's python interpreter or customizing it to your own requirement.
Make Sure You have installed django, djangorestframework, djangorestframework-simplejwt in the IDE/VS Code.Just run pip install django, pip install djangorestframework, pip install djangorestframework-simplejwt one by one.
You can run the project to see if it is working by running the command py maange.py runserver in the terminal.

models.py and serializers.py:-

Create the Model Classes of the User and Book by using the models.Model class in models.py. Add the required fields(Ex: username, password, roll_no,etc.,) to the respective User and Book Class.
Now we have to serialize the models.For this, we need to create a new python file called serializers in the app(in my case pustakaalay_app).
Now, firs things first import the following things in serializers.py -  
from rest_framework import serializers
from .models import User 
from .models import Book
Now create the serializers classes by inheriting the serializers.ModelSerializer and giving the name of the classes as UserSerializer and BookSerializer.
Create a Meta Class in both the Seializer Classes and the respective model to the meta class by assigning the model = User and model = Book to the respective classes.
Add the fields by assigning the fields variable to '__all__' for adding the fields from the model.If you want to hide any field just assign exclude = ["name_of_the_field"].

views.py:-

Now Add the Serializers in the views classes by creating classes named as UserDetailAPI and BookDetailAPI inherited from APIView. 
Make Sure import all the models, serializers; Response, JsonResponse, JsonParser, APIView from rest_framework; JWTAuthentication and IsAuthenticated from rest_framework_simplejwt_authentication & rest_framework_simplejwt_permissions.
Add the authenticated and permission instances to the UserDetailAPI and BookDetailAPI classes. Authenticate the request and check the request type(get,post,put,delete) and return the required response.

urls.py(project level):-

Import the following in the urls.py file 
from django.urls import include, path
from rest_framework.authtoken import views
from pustakaalay_app import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)
from django.contrib import admin
Add the redirecting path to the apps url by adding path('', include('pustakaalay_app.urls))(or whatever the name of the app is)
Add the following urlpatterns :-
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
Make sure to add admin.site.urls to the urlpatterns.

Running the project:-

Run the following three commands in the terminal of the IDE/VS Code one-by-one:-
py manage.py makemigrations
py manage.py migrate
py manage.py runserver

Your project should be running. If any issue arises then check whether all the models and serializers are matched properly.And follow the proper APIView Class instructions in the views.py.
For the reference use the official documentations:
https://www.python.org/doc/
https://docs.djangoproject.com/en/4.1/intro/tutorial01/
https://www.django-rest-framework.org/tutorial/quickstart/
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

For the help from the developers community always use Stackoverflow and Github.
