from django.shortcuts import render

# Create your views here.
def bootstrap_specific(request):
    return render(request,'bootstrap_specific.html')