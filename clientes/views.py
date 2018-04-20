from django.shortcuts import render

# Create your views here.
def persons_list(request):
    return request(request,'pessoa.html')