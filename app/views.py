from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'arjun','naveen':'RAM CHARAN'}
    return render(request,'first.html',context=d)