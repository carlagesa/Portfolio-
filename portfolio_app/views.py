from django.shortcuts import render
from portfolio_app.models import PreviousWork
from . import forms
from portfolio_app.forms import NewContact
# Create your views here.


def index(request):
    index = NewContact()

    if request.method == 'POST':
        index = NewContact(request.POST)

        if index.is_valid():
            index.save(commit=True)
            # return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'index.html', {'form': index})


def index(request):
        work_list = PreviousWork.objects.all()
        context = {
            'work_list': work_list
        }
        # print(work_list)
        return render(request, 'index.html', context)