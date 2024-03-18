from django.shortcuts import render, redirect
from .models import Url  # Importing the Url model

# The main view for handling both URL shortening and displaying the form.
def index(request):
    if request.method == 'POST':  # If the form has been submitted
        long_url = request.POST.get('long_url')  # Get the long URL submitted
        url, created = Url.objects.get_or_create(long_url=long_url)  # Get or create a Url object
        # Render the index.html template, passing in the short URL
        return render(request, 'index.html', {'short_url': request.build_absolute_uri(url.short_url)})

    # If the method is GET, render the form
    return render(request, 'index.html')

# A view to handle the redirection from the short URL to the long URL.
def redirect_view(request, short_url):
    url = Url.objects.filter(short_url=short_url).first()  # Find the Url object with the given short_url
    if url:
        return redirect(url.long_url)  # Redirect to the original long URL

    # If the short URL is not found, display an error on the index page.
    return render(request, 'index.html', {'error': 'URL not found'})

