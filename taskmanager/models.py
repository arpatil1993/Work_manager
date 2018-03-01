from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=15, verbose_name="name")
    login = models.CharField(max_length=20, verbose_name="login")
    password = models.CharField(max_length=20, verbose_name="password")
    phone = models.CharField(max_length=10, verbose_name="phone", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="born_date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="date of last connection", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="email")
    years_seniority =models.IntegerField(verbose_name="senerioity")
    date_created = models.DateField(verbose_name="user_created_date", auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    description = models.CharField(max_length=1000, verbose_name="description")
    client = models.CharField(max_length=100, verbose_name="client_name")

    def __str__(self):
        return self.title

    def get_json(self):
        result = {}
        result["title"] = self.title
        result["description"] = self.description
        result["client"] = self.client
        return result

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.CharField(max_length=1000, verbose_name="description")
    time_elasped = models.IntegerField(verbose_name="time_elasped", null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="importance")
    project = models.ForeignKey(Project, verbose_name="project",null=True, default=None, blank=True, on_delete=models.CASCADE)
    developer = models.ManyToManyField('Developer', verbose_name="developer")

    def __str__(self):
        return self.title

class Supervisor(UserProfile):
    specialization = models.CharField(max_length=50, verbose_name="specialization")

class Developer(UserProfile):
    supervisor1 = models.ForeignKey('Supervisor', verbose_name="supervisor", on_delete=models.CASCADE, null=True)

# class DeveloperWorkTask(models.Model):
#     developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     time_elasped_dev = models.IntegerField(verbose_name="time_elasped",null=True,default=None,blank=True)




