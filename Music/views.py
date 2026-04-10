import os
from django.shortcuts import render

# Create your views here.
def index(request):
    google_client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
    return render(request, "index.html", {"google_client_id": google_client_id})
