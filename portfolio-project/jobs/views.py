from django.shortcuts import render
from jobs.models import Job

# Create your views here.
def homepage(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})