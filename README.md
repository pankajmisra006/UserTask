# UserTask
Short project where user can ADD,UPDATE and DELETE task

1. Please set the database properties to your own Database credentials.....
add this in settings.py of your project

DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'usersTask',
        'USER': 'root',
        'PASSWORD': 'messithegoat',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

2. Run the project and hit this URL to open login/ register Page:
http://127.0.0.1:8000/taskdetails/

3. Register a user and then try to login;
4. select the available users a to see the task in the datatable( Task Displayed according to task created order by lastest one on top!).

5. Add the task for a user.
6. Again select the user to see the task details in datatable.
7. Update( Select a row from datatable and click update task button to update)
8. Delete(select a row u want to delete and click delete button)
