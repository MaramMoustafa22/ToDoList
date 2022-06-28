from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)


    def __str__(self):
    
        return self.title
        

class TodoItem(models.Model):
    title = models.CharField(max_length=500)
    todo = models.ForeignKey(Todo,related_name='topics',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


