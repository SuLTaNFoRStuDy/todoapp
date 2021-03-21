from django.db import models

# Create your models here.
class Todo(models.Model):
    added_time=models.DateTimeField(auto_now=True)
    todo_text=models.CharField(max_length=500,null=False,default="N/A")
    todo_title=models.CharField(max_length=200,null= False,default="N/A")
    todo_image=models.TextField(null=False)
    id=id

    def __str__(self):
        return self.todo_title