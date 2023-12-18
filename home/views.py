from django.shortcuts import render
from .forms import contactForm
from django.contrib import messages

# Create your views here.
def index (request):
    return render ( request, 'index.html')

def contact (request):
    if request.method == 'POST' :
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,' ✅your message has been sent!')
        else:
            messages.error(request, ' ⚠  Please fill in the form correctly!.')

    else:
        form =  contactForm()       
    
    return render ( request, 'contact.html', {'form':form})

