from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import ImageUploadForm, ParametersForm
import base64
from PIL import Image
import numpy as np
from io import BytesIO

# default home page view
def home(response):
    return render(response, 'analysis/home.html')

# view for about page


def about(response):
    return render(response, 'analysis/about.html')

# view for form and results


def analysis(request):
    # if this is a POST response we need to process the form data
    if request.method == 'POST':
        #print(request.POST)
        #print(request.FILES)
        try:
            image = request.FILES.get('image')
            b64_img = base64.b64encode(image.file.read())
            base64_image = str(b64_img)[2:-1]
            
            # default parameters
            name = 'initial'
        except:
            base64_image = request.POST.get('base64_image')
            name = request.POST.get('name')
        
        # prefilling form with base64 image
        data = {
            'name':name,
            'base64_image':base64_image
        }
        form = ParametersForm(data)

        # convert base64 image to PIL Image object
        im = Image.open(BytesIO(base64.b64decode(base64_image)))
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
            'base64_image':base64_image,
            'plot': plt_div,
            'form': form 
        }
        return render(request, 'analysis/output.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImageUploadForm()
        context = {
            'form': form
        }

        return render(request, 'analysis/form.html', context)
