import pandas as pd
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth, User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import *

#homePage display
def homepage(request):
    return render(request, "pages/login.html")

#user login..
def login(request):
    _message = ""
    _userList = {}
    if request.method == 'POST':
        _userName = request.POST['username']
        _password = request.POST['password']
        _user = Users.objects.filter(username=_userName, password=_password).values()
        if len(_user) != 0:
            _alluser = Users.objects.all().values()
            for _users in _alluser:
                _userList[_users['userID']] = _users['username']
            return render(request, "pages/welcome.html",
                          {'message': _user[0]['username'], 'id': _user[0]['userID'], 'userlist': _userList})
        else:
            _message = "Invalid Credentials";
            return render(request, "pages/login.html", {'message': _message})
    else:
        return redirect('/taskdetails/')


# Register...
def register(request):
    _message = ""
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
        _message = "user created succesfully"
        return render(request, "pages/login.html", {'message': _message})
    else:
        return redirect('/taskdetails/')


# load username...
def loadusername(request):
    _userList = {}
    print("coming")
    _alluser = Users.objects.all().values()
    for _users in _alluser:
        _userList[_users['userID']] = _users['username']
    return JsonResponse(_userList)


# Fetch task........
@csrf_exempt
def fetchtask(request):
    if request.method == 'GET':
        res = []
        _userId = request.GET['userid']
        _allTaskDetails = Task.objects.filter(userID_id=_userId).values()
        print(_allTaskDetails)
        for _task in _allTaskDetails:
            response_data = {}
            response_data['taskId'] = _task['taskId'],
            response_data['taskTitle'] = _task['taskTitle'],
            response_data['taskDescription'] = _task['taskDescription'],
            response_data['status'] = _task['status'],
            res.append(response_data)

        return JsonResponse(res, safe=False)

# add task........
@csrf_exempt
def addtask(request):
    _message = ""
    form = addTaskForm()
    if request.method == 'POST':
        form = addTaskForm(request.POST)
        if form.is_valid():
            form.save()
        _message = "Task created succesfully!"
        return JsonResponse(_message, safe=False)
    else:
        _message = "Failed to create task!"
        return JsonResponse(_message, safe=True)


# Update task....
@csrf_exempt
def updatetask(request):
    if request.method == 'POST':
        _taskId = request.POST['taskid']
        _title = request.POST['title']
        _taskdesc = request.POST['taskdesc']
        _status = request.POST['status']
        _taskuserid = request.POST['taskuserid']
        _updateTask = Task.objects.filter(userID_id=_taskuserid, taskId=_taskId).update(taskTitle=_title,
                                                                                        taskDescription=_taskdesc,
                                                                                        status=_status)
        _message = "succesfully updated!"
        return JsonResponse(_message, safe=False)


# delete task....
@csrf_exempt
def deletetask(request):
    if request.method == 'POST':
        _taskId = request.POST['taskid']
        _taskuserid = request.POST['taskuserid']
        _deletTask = Task.objects.filter(userID_id=_taskuserid, taskId=_taskId).delete()
        _message = "succesfully deleted!"
        return JsonResponse(_message, safe=False)

#diaplays welcome page
def welcome(request):
    return render(request, "pages/welcome.html")
