from django.db import models

# Create your models here.
class Tasks(models.Model):
    Title = models.CharField("Title",max_length=500)   
    BookedByUser = models.CharField("Booked By", max_length=500)
    UploadDate = models.DateTimeField("Uploaded At")
    isDeleted = models.BooleanField("Is Deleted", default=False)

    def __str__(self):
        return self.Title
    
class TasksZipFile(models.Model):
    Title = models.ForeignKey(Tasks, on_delete=models.CASCADE)    
    ZIPFile = models.FileField("File Name", upload_to='ZIPFiles/%Y-%m')