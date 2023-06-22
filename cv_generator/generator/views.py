from django.shortcuts import render
from .models import *


# Create your views here.
def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()

    return render(request, 'generator/accept.html')



def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    context = {
        'user_profile': user_profile,
    }

    return render(request, 'generator/cv.html', context)






