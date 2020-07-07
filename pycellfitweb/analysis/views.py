from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import AnalysisForm
import base64
from PIL import Image
import numpy as np


# default home page view
def home(request):
    return render(request, 'analysis/home.html')

# view for about page
def about(request):
    return render(request, 'analysis/about.html')

# view for form and results
def analysis(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnalysisForm(request.POST, request.FILES)
        
        # validate form
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data)
        
            # extract input parameters from form
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']


            # convert uploaded image to np array
            im = Image.open(image)
            img_array = np.array(im)

            # plot np array using plotly
            import plotly.express as px
            from plotly.offline import plot
        
            fig = px.imshow(img_array)
            config = {
                'scrollZoom': False,
                'displayModeBar': True,
                'showLink':False,
                'displaylogo': False
            }
            plt_div = plot(fig, output_type='div', include_plotlyjs=False, show_link=False, link_text="", config=config)

            # send all form, information, and plot to html template
            context = {
                'name': name,
                'form': form,
                'plot': plt_div
            }
            return render(request, 'analysis/output.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        print('get, loading form')
        form = AnalysisForm()
        context = {
            'form': form
        }
        
        return render(request, 'analysis/form.html', context)