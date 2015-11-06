from django.shortcuts import render
from trips.models import Trip, Experience, Picture
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import models

# Create your views here.
@login_required
def my_trips(request):
    trip_list = Trip.objects.all().filter(user = request.user).order_by('-year', 'title')
    context = {'trips': trip_list}
    return render(request, 'trips/my_trips.html', context)

from trips.forms import TripForm

@login_required
def add_trip(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = TripForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            trip = form.save(commit=False)
            trip.user = request.user  # The logged-in user
            trip.lat_lng = trip.country
            trip.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return my_trips(request)
        else:
        # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = TripForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'trips/add_trip.html', {'form': form})

@login_required 
def view_my_trip(request, trip_title_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        trip = Trip.objects.get(slug=trip_title_slug, user = request.user)
        context_dict['trip_title'] = trip.title

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        experiences = Experience.objects.filter(trip=trip)

        # Adds our results list to the template context under name pages.
        context_dict['experiences'] = experiences
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['trip'] = trip
        context_dict['trip_title_slug'] = trip_title_slug
        context_dict['username'] = request.user.username
    except Trip.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'trips/view_my_trip.html', context_dict)

from trips.forms import ExperienceForm

@login_required
def add_experience(request, trip_title_slug):
    
    try:
        trip = Trip.objects.get(slug=trip_title_slug, user = request.user)
    except Trip.DoesNotExist:
                trip = None
                
    # A HTTP POST?
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        
        if form.is_valid():
            if trip:
                experience = form.save(commit=False)
                experience.trip = trip
                experience.save()
                # probably better to use a redirect here.
                
                experience_id = Experience.objects.latest('id')
                return view_my_trip(request, trip_title_slug)
        else:
        # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = ExperienceForm()
        context_dict = {'form':form, 'trip': trip}
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'trips/add_experience.html', context_dict)

@login_required
def view_experience(request, trip_title_slug, experience_id):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        experience = Experience.objects.get(id=experience_id)
        
        context_dict['experience_title'] = experience.title
        context_dict['experience_description'] = experience.description
        context_dict['trip_title_slug'] = trip_title_slug
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        #experiences = Experience.objects.filter(trip=trip)
        
        images = Picture.objects.filter(experience=experience)
        context_dict['images'] = images
        # Adds our results list to the template context under name pages.
        #context_dict['experiences'] = experiences
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['experience'] = experience
        context_dict['experience_id'] = experience_id
    except Experience.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'trips/view_experience.html', context_dict)


@login_required
def edit_experience(request,trip_title_slug, experience_id):
    
    try:
        trip = Trip.objects.get(slug=trip_title_slug, user = request.user)
    except Trip.DoesNotExist:
                trip = None
                
    try:
        experience = Experience.objects.get(id = experience_id)
    except Experience.DoesNotExist:
                experience = None
                
    # A HTTP POST?
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance = experience)
        
        if form.is_valid():
            if trip:
                experience = form.save(commit=False)
                experience.trip = trip
                experience.save()
                # probably better to use a redirect here.
                
                experience_id = Experience.objects.latest('id')
                return view_my_trip(request, trip_title_slug)
        else:
        # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = ExperienceForm(instance = experience)
        context_dict = {'form':form, 'experience': experience, 'trip_title_slug':trip_title_slug, 'experience_id':experience_id}
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'trips/edit_experience.html', context_dict)

@login_required
def delete_experience(request, trip_title_slug, experience_id):
    
    try:
        trip = Trip.objects.get(slug=trip_title_slug, user = request.user)
    except Trip.DoesNotExist:
                trip = None
    try:
        experience = Experience.objects.get(id = experience_id)
    except Experience.DoesNotExist:
                experience = None
    
    if trip:
        experience.delete()
        return view_my_trip(request, trip_title_slug)
   
from trips.forms import PictureForm

@login_required
def add_image(request, trip_title_slug, experience_id):
    
    try:
        experience = Experience.objects.get(id=experience_id)
    except Experience.DoesNotExist:
                experience = None
    try:
        images = Picture.objects.filter(experience=experience)
    except Picture.DoesNotExist:
                images = None
                
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        image_form = PictureForm(data=request.POST)

        # If the two forms are valid...
        if image_form.is_valid():
            if experience:
                image = image_form.save(commit=False)
                image.experience = experience

                if 'picture' in request.FILES:
                    image.picture = request.FILES['picture']
                    image.picture_big = request.FILES['picture']
                    image.picture_small = request.FILES['picture']
                image.save()
        else:
            print (image_form.errors)
    else:
        image_form = PictureForm()

    return render(request,
            'trips/add_image.html',
            {'experience': experience, 'images': images, 'image_form': image_form, 'trip_title_slug': trip_title_slug, 'experience_id': experience_id} )
 
#public views
def homepage(request):
    import random    
    object_list = list(Picture.objects.all()[:100])
    random.shuffle(object_list)
    #images = Image.objects.all()
    return render(request, 'trips/homepage.html', {'images': object_list})
 
def users(request):
    group = models.Group.objects.get(name='tripper')
    users = group.user_set.all()

    context = {'users': users}
    return render(request, 'trips/users.html', context)
    
def index(request, user_username):
    
    context_dict = {}
    
    context_dict['username'] = user_username
    
    user = User.objects.get(username=user_username)
    trip_list = Trip.objects.all().filter(user = user).order_by('-year', 'title')[:3]
    country_list = Trip.objects.all().filter(user = user)
    context_dict['countries'] = country_list
    count = trip_list.count()
    context_dict['count'] = count
    context_dict['trips'] = trip_list
    context_dict['user_number_of_trips'] = user.count_number_of_trips()
    
    try:
        all_images = Picture.objects.filter(experience__trip__user = user)
        context_dict['all_images'] = all_images
        
    except Picture.DoesNotExist:
        pass
    
    try:
        user_profile_pic = user.profile.picture
        context_dict['user_profile_pic'] = user_profile_pic
    except AttributeError:
        pass
    
    return render(request, 'trips/index.html', context_dict)
    
def view_trip(request, user_username, trip_title_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        trip = Trip.objects.get(slug=trip_title_slug)
        context_dict['trip'] = trip
        context_dict['trip_title_slug'] = trip_title_slug
        context_dict['trip_title'] = trip.title

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        experiences = Experience.objects.filter(trip=trip).prefetch_related('image_set').all()
            
        # Adds our results list to the template context under name pages.
        context_dict['experiences'] = experiences
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        
    except Trip.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'trips/view_trip.html', context_dict)
