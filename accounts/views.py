from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import models
from accounts.models import UserProfile

# Create your views here.
def index(request):
    
    context = {}
    try:
        profile_pic = UserProfile.objects.get(user=request.user)
        context['profile_pic'] = profile_pic
    except UserProfile.DoesNotExist:
        pass

    context['user'] = request.user
    return render(request, 'accounts/index.html', context)

from accounts.forms import UserProfileForm

def add_profile_pic(request):

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if profile_form.is_valid():

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = request.user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'accounts/add_profile_pic.html',
            {'profile_form': profile_form,} )