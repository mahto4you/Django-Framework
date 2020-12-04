from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request, 'fees/info.htm', {'nmf':'Django Fees'})