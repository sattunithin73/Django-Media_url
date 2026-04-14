from django.shortcuts import render
from .models import student

# Create your views here.
def  home(request):
    data = student.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        simage = request.FILES.get('pic') #return pic else none
        student.objects.create(
            name = name,
            course = course,
            simage = simage if simage else 'Default.webp'
        )
    return render(request,'home.html',{'data': data})