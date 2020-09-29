from django.contrib.auth.decorators import permission_required
#from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import animalabuse


import csv, io
from django.shortcuts import render
from django.contrib import messages

from datetime import datetime
from .filters import UserFilter
from .forms import SubmitForm

from django.http import HttpResponseRedirect

# Create your views here.
def product_detail_view(request):
	
	return render()

# Create your views here.
# one parameter named request
@permission_required('admin.can_add_log_entry')
def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = animalabuse.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, data of birth, age, county, offense, conviction date, expiration date, image',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line 
    #we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = animalabuse.objects.update_or_create(
                name=column[1],
                DOB=column[2],
                Age=int(column[3]),
                county=column[4],
                #Address=column[5],
                Offense=column[5],
                convictiondate=datetime.strptime(column[6], "%m/%d/%y"),
                expirationdate=datetime.strptime(column[7], "%m/%d/%y"),
                image=column[8]
            )
    context = {}
    return render(request, template, context)


def search(request):
    user_list = animalabuse.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search_list.html', {'filter': user_filter})

#@require_http_methods(["GET"])
def user_profile_view(request, user_id):
    """User profile page."""
    user = get_object_or_404(animalabuse, id=user_id)
    context = {'user': user,
               'title': f'{user.name}\'s Profile',
               'path': request.path}
    return render(request, 'profile.html', context)

def submitnew(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = SubmitForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        name = form.cleaned_data['name']
        Age = form.cleaned_data['Age']
        county = form.cleaned_data['county']
        Offense = form.cleaned_data['Offense']
        convictiondate = form.cleaned_data['convictiondate']
        p = animalabuse(name=name, Age=Age, county=county, Offense=Offense,convictiondate = convictiondate)
        p.save()
        #messages.success(request,u"Thank you for your submission !")
        # redirect to a new URL:
        return HttpResponseRedirect('/success/')
  # if a GET (or any other method) we'll create a blank form    
  else: 
    form = SubmitForm()

  return render(request, 'submitform.html', {'form': form})

def success(request):
    return render(request, "success.html")
