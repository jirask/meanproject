from statistics import mean
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .forms import CalculateForm


def calculate_mean(request):
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            input_numbers = form.cleaned_data['input_numbers']
            if(isinstance(input_numbers,int)):
                request.session['average'] = input_numbers
            else :
                request.session['average'] = mean(input_numbers)
            output = {
                'type': 'success'
                }
            messages.success(request, JsonResponse(output).content)

        else:
            messages.error(request, JsonResponse(form.errors, status=400).content)
    else:
        form = CalculateForm()
    return render(request, 'calculation/index.html', {'form': form})


def reset_session(request):
    try:
        del request.session['average']
    except KeyError:
         pass
    messages.success(request, "Value reset is done.")

    return HttpResponseRedirect(reverse('calculation:index'))


