from django.shortcuts import render
from django.http import HttpResponse
from .models import Analysis, AnalysisForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import os


# Create your views here.


def index(request):
    if request.method == "POST":
        form = AnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            # https://stackoverflow.com/questions/11336548/django-taking-values-from-post-request
            saved = form.save()
            id = saved.unique_id
            # TOD o  insert script call
            # Where your script runs
            # list of output filenames
            # {filename}-1.txt => make this a list with the correct path
            # Loop through these in your template using an anchor tag
            input_file_path = os.path.join(os.getcwd(), "media", saved.file.name)
            print(input_file_path)

            upload_to_display = Analysis.objects.get(
                unique_id=id)  # selecting the first object
            context = {
                'title': 'Outputs',
                'upload': upload_to_display,
            }
            return render(request, 'pycellfit/output.html', context)

    else:
        form = AnalysisForm()
        context = {
            'title': 'Upload Form',
            'form': form
        }
        return render(request, 'pycellfit/upload_form.html', context)


def about(request):
    return render(request, 'pycellfit/about.html')
