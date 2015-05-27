from django.shortcuts import render
from django.shortcuts import render_to_response

def about(request):
    #render(request,"about.html",{})
    return render_to_response("about.html")