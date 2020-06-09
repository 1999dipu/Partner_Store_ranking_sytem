# PARTNER/STORE RANKING SYSTEM- ACMS PROJECT

## PROJECT DESCRIPTION:

The system is to rank the Access Point Stores based on factors like Distance from the Customers, Store availability, Throughput, New Launch, etc. to provide the closest and most reliable store at the top to the customer as well as distributing the order traffic at the same time.

The whole system will consist of 2 portals. The first one to onboard the stores through the portal and another one to search the stores. Searching will return the numerous stores ranked by the Ranking system in the backend. The Ranking system will rank the stores by keeping the weightage to the factors and calculate a normalized score to rank the locations.

## PREREQUISITES TO EXECUTE THE CODE:

In addition to basic Python3 you need:
```
- Django==3.0.5

- Djangorestframework==3.11.0

- django-cors-headers

- SQLite studio (to have a look at the database)
```
## STEPS TO INSTALL THESE REQUIREMENTS:
```
-pip install django==3.0.5

-pip install djangorestframework==3.11.0

-pip install Django-cors-headers
```
## STEPS TO EXECUTE THE CODE: (as per Windows)
```
1.Open command prompt in your system.

2.Create an empty directory on your system.

3.Create a virtual environment inside this directory as follows:

             -python -m venv venv // virtual env created

             -venv\Scripts\activate.bat //venv activated

             -Install all the dependencies as given above

4.Clone the project into the directory created in Step 2 (git clone “address of project”)

5.Make sure your virtual env is active and you’re inside the project directory (leadmanager)  
  and start your Django server by executing the following command:
         
             -python manage.py runserver 

             -Copy the address and paste it in your web browser

6.You can start using the project now.

7.In case you wish to access the admin panel to check the various tables in the system then open
  the django admin panel by:

             -Append “/admin” in the server address (Step 5)

             -In case you’re a new user, create a superuser to enter into the panel by executing the  
              following command in your command prompt(make sure that your virtual env is active and 
              you’re inside the project directory leadmanager):
              
                            	python manage.py createsuperuser

                            	Enter all the information being asked

                            	Go back to the admin panel and enter the username and password as created.

8.You now have access to all the functionalities in this project.
```
### GOOD LUCK!

