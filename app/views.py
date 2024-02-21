from django.shortcuts import render

# Create your views here.
def jinga_printing(request):
    d={'data':'teja reddy'}#we send data to frontend in the form of dictonary,key-value pairs
    return render(request,'jinga_printing.html',context=d)#we use key to collect the data in front end

    '''
    context is not mandatory
    return render(request,'jinga_printing.html',d)
    '''

def jinja_opertaional(request):
    d={'data':[1,'',3,'',5,''],'names':['teja','sai','triandh','bhanu']}
    return render(request,'jinja_opertaional.html',d)

