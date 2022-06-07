from statistics import mean
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .forms import CalculateForm

## calculates mean out of the input_numbers and stores it in the session and sends feedback to the user (success and error messages). ##

def calculate_mean(request):
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            input_numbers = form.cleaned_data['input_numbers']
            ## if input is only one number convert it to list
            if(isinstance(input_numbers,int)):
                input_numbers=[input_numbers]

            ##init average if no value is stored in cash
            if(request.session.get('average','First Calcualtion')=='First Calcualtion'):
                request.session['input_numbers']=input_numbers
                request.session['average'] = mean(input_numbers)
            else:            
                new_numbers=input_numbers
                old_numbers=request.session['input_numbers']
                request.session['input_numbers']=old_numbers+new_numbers
                request.session['average'] = mean(new_numbers+old_numbers)
            output = {
                'type': 'success'
                }
            messages.success(request, JsonResponse(output).content)

        else:
            messages.error(request, JsonResponse(form.errors, status=400).content)
    else:
        form = CalculateForm()
    return render(request, 'calculation/index.html', {'form': form})


## reset stored mean value ##

def reset_session(request):
    try:
        del request.session['average']
        del request.session['input_numbers']
    except KeyError:
         pass
    messages.success(request, "Value reset is done.")

    return HttpResponseRedirect(reverse('calculation:index'))


