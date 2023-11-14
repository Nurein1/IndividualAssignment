from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return render(request, 'main.html')


def sgs(request):
    return render(request, 'sgs.html')


def security(request):
    return render(request, 'security.html')