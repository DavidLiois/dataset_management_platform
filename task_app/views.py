from task_app.models import Tasks, TasksZipFile
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.utils import timezone
from .forms import UploadFileForm
# for zipfile upload

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'task_app/task.html'
    context_object_name = "TaskList"
    
    def get_queryset(self):        
        return Tasks.objects.filter(isDeleted=False).order_by('UploadDate')

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Tasks
    template_name = "task_app/detail.html"

@login_required
def NewTask(request):
    form = UploadFileForm()
    context={'form':form}
    return render(request, 'task_app/new_task.html', context)

@login_required
def NewTaskUpload(request):    
    try:        
        Form = UploadFileForm(request.POST, request.FILES)
        if Form.is_valid():
            File = request.FILES['file']
            FileName = request.FILES['file'].name
            
            if FileName.endswith('.zip'):
                TaskTitle = request.POST['title']
                NewTask = Tasks(Title=TaskTitle, UploadDate=timezone.now(), isDeleted=False)
                NewTask.save()

                NewTaskZip = TasksZipFile(Title=NewTask, ZIPFile=File)
                NewTaskZip.save()
            else:
                return render(request, 'task_app/error_handler.html', {
                    "error_message": "You have to upload a zip file."
                })
    except (KeyError):
        return render(request, 'task_app/error_handler.html', {
            "error_message": "Error occured"
        })
    return render(request, 'task_app/error_handler.html', {
        "TaskTitle": TaskTitle, "Filename": FileName
    })

@login_required
def Booking(request, TaskId):
    try:        
        BookingTask = get_object_or_404(Tasks, pk=TaskId)
        if request.user.is_authenticated:
            Username = request.user.username
            BookingTask.BookedByUser = Username
            BookingTask.save()
            BookSuccess = True
    except (KeyError, Tasks.DoesNotExist):
        return render(request, 'task_app/error_handler.html', {
            "error_message": "Error occured"
        })
    return render(request, 'task_app/error_handler.html', {
        "Username": Username, "Booked": BookSuccess
    })

@login_required
def Revoke(request, TaskId):
    try:        
        RevokingTask = get_object_or_404(Tasks, pk=TaskId)
        if request.user.is_authenticated:
            Username = request.user.username
            if Username == RevokingTask.BookedByUser:
                RevokingTask.BookedByUser = ""
                RevokingTask.save()
                RevokeSuccess = True
            else:
                return render(request, 'task_app/error_handler.html', {
                    "error_message": "You don't have permission to revoke this task"
                })
    except (KeyError, Tasks.DoesNotExist):
        return render(request, 'task_app/error_handler.html', {
            "error_message": "Error occured"
        })
    return render(request, 'task_app/error_handler.html', {
        "Revoke" : RevokeSuccess
    })

@login_required
def Download(request, TaskId):
    try:        
        DownloadTask = get_object_or_404(Tasks, pk=TaskId)        
        if request.user.is_authenticated:
            Username = request.user.username

        if Username == DownloadTask.BookedByUser:        
            DownloadTaskFile = get_object_or_404(TasksZipFile, Title=DownloadTask)
            FilePath = DownloadTaskFile.ZIPFile.path
            Response = FileResponse(open(FilePath, 'rb'))
            return Response
        else:
            return render(request, 'task_app/error_handler.html', {
                "error_message": "You don't have permission to download this file."
            })
    except (KeyError, Tasks.DoesNotExist):
        return render(request, 'task_app/error_handler.html', {
            "error_message": "Error occured"
        })

@login_required
def Delete(request, TaskId):
    try:        
        DeleteTask = get_object_or_404(Tasks, pk=TaskId)
        if request.user.is_authenticated:
            Username = request.user.username

        if Username == DeleteTask.BookedByUser:
            DeleteTask.isDeleted = True
            DeleteTask.save()
            Deleted = True
        else:
            return render(request, 'task_app/error_handler.html', {
                "error_message": "You don't have permission to delete this task."
            })

    except (KeyError, Tasks.DoesNotExist):
        return render(request, 'task_app/error_handler.html', {
            "error_message": "Error occured"
        })
    return render(request, 'task_app/error_handler.html', {
        "Deleted": Deleted
    })
    