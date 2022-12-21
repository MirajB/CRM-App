## CRM application.

This project is a prototype of CRM appications in which we can create and assign leads to our agents.


This project is developed in Python 3.8. You can find the list of dependencies in requirements.txt file.

Pease run beow command to install dependencies:

> pip install -r requirements.txt

Pease run below command to run project.

> python manage.py runserver

Django Admin credentials:

> email: geek@geek.com

> pwd: geek123


This project takes follwoing functionalities of Django implemented. 

1. Base User class Abstraction : Insted of default User class of Django, we are using our custom User class defined in leads/models.py.
2. Mixins: For code reusability, implemented the concept of Mixins. Mixins are used in leads/models.py -> lead class.
3. Django Forms: Used in-built form functionality of Django for Create/update model classes. Refer leads/forms.py.
4. Django Unit test cases: Django unit test cases are added for model and form validations.
