from django.shortcuts import render
def index(request):
    context={
        'title':'POS',
        'head':'POINT_OF_SALES',
    }
    return render(request, 'index.html', context)
# Create your views here.
