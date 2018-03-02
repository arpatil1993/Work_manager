from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from django.http import JsonResponse
import json, datetime
from django.utils import timezone
from .models import Project, Supervisor, Developer, Task
from .epoch_functions import *
# Create your views here.

def IndexView(request):
    return HttpResponse("Hello, world!")

def create_project_object(request):
    params = json.loads(request.body.decode('utf-8'))
    try:
        title = params.get('title')
        description = params.get("description")
        client = params.get("client")

        project_obj = Project.objects.create(title = title, description = description, client = client)
        if project_obj.id:
            return JsonResponse({"validation": "project object created", "status": True})
        else:
            return JsonResponse({"validation": "project object creation failed", "status": False})

    except Exception as e:
        print(e)
        return JsonResponse({"status": False})

def get_project_object(request):

    project_object = Project.objects.get(title="Mahoo")
    data = project_object.get_json()
    # data = []
    # for project in project_object:
    #     data.append(project.get_json())
    return JsonResponse({"Data": data})

def save_task_object(request):
    params = json.loads(request.body.decode('utf-8'))
    print params
    try:
        with transaction.atomic():
            status, task_id, supervisor_id = create_task_object(params)

            if status:
                print status
                developers = params.get("developers")
            task_obj = Task.objects.get(id = task_id)
            
            for developer in developers:
                new_developer = Developer.objects.create(
                    name = developer["name"],
                    login = developer["login"],
                    password = developer["password"],
                    phone = developer["phone"],
                    born_date = convert_epoch_to_date(developer["born_date"]),
                    email = developer["email"],
                    years_seniority = developer["years_seniority"],
                    supervisor1 = Supervisor.objects.get(id=supervisor_id)
                )
                
                task_obj.developer.add(new_developer)
            
            return JsonResponse({"validation": "Task_pbject created successfully"})


    except Exception as e:
        print(e)
        return JsonResponse({"validation": "Task creation Failed"})

def create_task_object(params):
    #params = json.loads(request.body.decode('utf-8'))

    #saving a new supervisor
    new_supervisor = Supervisor.objects.create(
        name = params.get("name"),
        login = params.get("login"),
        password = params.get("password"),
        phone = params.get("phone"),
        born_date = convert_epoch_to_date(params.get("born_date")),
        last_connection = timezone.now(),
        email =  params.get("email"),
        years_seniority = params.get("years_seniority"),
        date_created = datetime.datetime.today().date(),
        specialization= params.get("specialization")
    )
    #project to link
    project_to_link = Project.objects.get(title="Mahoo")

    #saving a new task
    new_task = Task.objects.create(
        title = params.get("title"),
        description = params.get("description"),
        time_elasped = params.get("time_elasped"),
        importance = params.get("importance"),
        project = project_to_link
    )
    if new_task.id:
        # return JsonResponse({"status": True, "id" = new_task.id})
        return True, new_task.id, new_supervisor.id
        print new_task.id




















