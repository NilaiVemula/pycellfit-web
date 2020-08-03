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
        # print(request.POST)
        # print(request.FILES)
        try:
            image = request.FILES.get('image')
            b64_img = base64.b64encode(image.file.read())
            base64_image = str(b64_img)[2:-1]
            # TODO: pass the mesh object
            # default parameters
            name = 'initial'

            # prefilling form with base64 image
            data = {
                # Image
                'name': name,
                'base64_image': base64_image,
                # Mesh Generation
                'avg_num_nodes_per_edge': 4,
                # CellFIT Formulation
                'tangent_vector_method': 'circle',
                # CellFIT Solver
                'tensions': True,
                'pressures': False,
                'condition_numbers': False,
                'standard_errors': False,
                'residuals': False,
                'exclude_short_edges': False,
                'exclude_outside_edges': True,
                # Display
                'segmented_image': True,
                'mesh': True,
                'tangent_vectors': False,
                'circle_fit_arcs': False,
                'tensions': False,
                'pressures': False,
                'residual_vectors': False,
                'nodes': False,
                'edge_ids': False,
                'cell_ids': False,
                'junction_ids': False
            }
            form = ParametersForm(initial=data)

        except:
            # In this case, the user is updating results
            form = ParametersForm(request.POST)
            data = request.POST

        # convert base64 image to PIL Image object
        im = Image.open(BytesIO(base64.b64decode(data['base64_image'])))
        img_array = np.array(im)

        # plot np array using plotly
        import plotly.express as px
        from plotly.offline import plot

        fig = px.imshow(img_array)
        config = {
            'scrollZoom': False,
            'displayModeBar': True,
            'showLink': False,
            'displaylogo': False
        }
        plt_div = plot(fig, output_type='div', include_plotlyjs=False,
                       show_link=False, link_text="", config=config)

        # send all form, information, and plot to html template
        context = {
            'name': data['name'],
            'base64_image': data['base64_image'],
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

        return render(request, 'analysis/upload_form.html', context)
