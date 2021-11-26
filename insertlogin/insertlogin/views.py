# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from django.http import HttpResponse
from insertlogin.models import EmpInsert
from django.contrib import messages
# from .forms import Formregister

def insertrecord(request):
    # return HttpResponse("<h1>Hello Muralidharan...</h1>")
    # return render(request,'login.html')
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            saverecord = EmpInsert()
            saverecord.email = request.POST.get('email')
            saverecord.password = request.POST.get('password')
            saverecord.save()
            messages.success(request,'record saved....')
            return render(request,'./login.html')
    else:
            return render(request,'./login.html')
        


# def insertrecord(request):
#     form = Formregister(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {'Formregister':Formregister}
#     return render(request,'login.html',context)