from django.shortcuts import render

# Create your views here.

def test_t(request):
    return render(request, 'webBoard/index.html')