from django import views
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm
from django.views import View

# Create your views here.
class ViewData(View):
    def get(self,request):
        form = StudentForm()
        data = Student.objects.all()
        return render(request, 'core/addandshow.html', {'form': form, 'data': data})

    def post(self,request):
        data = StudentForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
        return redirect('/')

class ViewDelete(View):
    def  post(self,request,id):
        data = Student.objects.get(id=id)
        data.delete()
        return redirect('/')


class ViewUpdate(View):
    def  post(self,request,id):
        data=Student.objects.get(id=id)
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('/')
    def  get(self,request,id):
        # data get bhayo thau ma means click garda defaut get hunxa
        data=Student.objects.get(id=id)
        form=StudentForm(instance=data)
    
        return render(request, 'core/update.html',{'form':form})


# def getdata(request):
#     if request.method=='GET':
#         form = StudentForm()
#         data = Student.objects.all()
#         return render(request, 'core/addandshow.html', {'form': form, 'data': data})
#     if request.method=='POST':
#         data = StudentForm(request.POST, request.FILES)
#         if data.is_valid():
#             data.save()
#         return redirect('/')

# def delete(request, id):
#     data = Student.objects.get(id=id)
#     data.delete()
#     return redirect('/')

# def update(request,id):
#     if request.method=='POST':
#         data=Student.objects.get(id=id)
#         form=StudentForm(request.POST,instance=data)
#         if form.is_valid():
#             form.save()
#         redirect('/')
#     else:
#         # data get bhayo thau ma means click garda defaut get hunxa
#         data=Student.objects.get(id=id)
#         form=StudentForm(instance=data)
    
#     return render(request, 'core/update.html',{'form':form})
