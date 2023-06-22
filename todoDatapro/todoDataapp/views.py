from django.shortcuts import render,redirect
from.models import todoData

def mainview(request):
    data=todoData.objects.all()
    return render(request,'main.html',{'data':data})

def formview(request):
    if request.method=='GET':
        return render(request,'form.html')
    else:
        todoData(
        task_title=request.POST['task_title'],
        task_description=request.POST['task_description'],
        date=request.POST['date']
        ).save()
        return redirect(mainview)

def updatedata(request,id):
    data=todoData.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update.html',{'data':data})
    else:
        data.task_title=request.POST['task_title']
        data.task_description=request.POST['task_description']
        data.date=request.POST['date']
        data.save()
        return redirect(mainview)
def delete(request,id):
    data=todoData.objects.get(id=id)
    data.delete()
    return redirect(mainview)
