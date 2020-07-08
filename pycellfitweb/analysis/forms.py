from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class ParametersForm(forms.Form):
    name = forms.CharField(max_length=100)
    # Image
    base64_image = forms.CharField(max_length=100000000, widget=forms.HiddenInput())
    # Mesh Generation
    avg_num_nodes_per_edge = forms.IntegerField(min_value=2, max_value=20)
    TANGENT_CHOICES = [
        ('circle', 'Circle Fit'),
        ('nearest_segment', 'Nearest Segment'),
        ('chord', 'Chord')
    ]
    # CellFIT Formulation
    tangent_vector_method = forms.ChoiceField(label='Method for calculating tangent vector',choices=TANGENT_CHOICES)
    # CellFIT Solver
    tensions = forms.BooleanField(required=False) 
    pressures = forms.BooleanField(required=False) 
    condition_numbers = forms.BooleanField(required=False) 
    standard_errors = forms.BooleanField(required=False) 
    residuals = forms.BooleanField(required=False) 
    exclude_short_edges = forms.BooleanField(required=False) 
    exclude_outside_edges = forms.BooleanField(required=False) 
    # Display
    segmented_image = forms.BooleanField(required=False) 
    mesh = forms.BooleanField(required=False) 
    tangent_vectors = forms.BooleanField(required=False) 
    circle_fit_arcs = forms.BooleanField(required=False) 
    tensions = forms.BooleanField(required=False) 
    pressures = forms.BooleanField(required=False) 
    residual_vectors = forms.BooleanField(required=False) 
    nodes = forms.BooleanField(required=False) 
    edge_ids = forms.BooleanField(required=False) 
    cell_ids = forms.BooleanField(required=False) 
    junction_ids = forms.BooleanField(required=False) 


