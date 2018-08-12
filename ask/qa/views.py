from django.shortcuts import render, HttpResponse

# Create your views here.


def test_it(request, *args, **kwargs):
    return HttpResponse('OK')