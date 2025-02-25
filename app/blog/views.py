from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .form import Register_Form , Login_Form ,Slider_Form , FeatureForm , Feedback_Form
from .models import Register_Model , Slider_Model , Feature_Model , Feedback_Model




# home----------------------------------------------------------



def home(request):
    slider_img = Slider_Model.objects.filter(trending=True)  
    slider = slider_img.last() if slider_img.exists() else None

    feature_img = Feature_Model.objects.filter(trending=True)
    feedback = Feedback_Form()

    if request.method == 'POST':  
        feedback = Feedback_Form(request.POST)  
        if feedback.is_valid():
            feedback.save()
            messages.success(request, "Your message was sent successfully!")
            return redirect('home')  
        
    return render(request, "home.html", {'slider_img': slider_img, 'slider': slider, 'feature_img': feature_img, 'feedback': feedback})





# user register -----------------------------------------------------------------------------------

def user_register(request):
    if request.method == 'POST':
        register_form = Register_Form(request.POST, request.FILES)

        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            conform_password = request.POST.get('conform_password')  # Fix spelling

            if password == conform_password:
                if User.objects.filter(username=name).exists():
                    messages.warning(request, "Username already taken. Choose another one.")
                    return redirect('register')

                user = User.objects.create_user(username=name, email=email, password=password)
                user.is_staff = False
                user.is_superuser = False
                user.save()

                messages.success(request, "Registration successful!")
                return redirect('login')
            else:
                messages.warning(request, "Passwords do not match!")
                return redirect('register')

    else:
        register_form = Register_Form()

    return render(request, 'register_form.html', {'register_form': register_form})


# user login ----------------------------------------------------------------------------------------------


@csrf_exempt
def user_login(request):
    user_log = Login_Form()

    if request.method == 'POST':
        user_log = Login_Form(request.POST)
        
        if user_log.is_valid():
            username = user_log.cleaned_data['username']
            password = user_log.cleaned_data['password']
            user = authenticate(request, username=username ,password=password)

            if user is not None:
                auth_login(request , user)

                if user.is_staff or user.is_superuser:
                    return redirect ("profile")
                
                
                else:
                    return redirect ('home')
                
            else:
                messages.warning(request, "invalid ussername , password !..")


    return render(request , 'login_form.html' , {'login_form':user_log})


# user logout ----------------------------------------------------------------------------------------

def user_logout(request):
    auth_logout(request)
    return redirect('login')


# Slider ------------------------------------------------
def slider(request):
    
    slider_img = Slider_Model.objects.all()
    return render(request, "slider.html", {'sliders':slider_img})


def slider_form(request):
    slider_form = Slider_Form()
    if request.method=='POST':
        slider_form = Slider_Form(request.POST, request.FILES)

        if slider_form.is_valid():
            slider_form.save()

            messages.success(request, "Registration successful!")
            return redirect('slider')
        
    return render(request, 'slider_form.html' , {'slider_form':slider_form})

def update_slider(request, id):
    feature_data = Slider_Model.objects.get( id=id)
    feature_form = Slider_Form(instance=feature_data)

    if request.method=='POST':
        feature_form = Slider_Form(request.POST,instance=feature_data)
        if feature_form.is_valid():
            feature_form.save()
            messages.success(request, "Add new slider !..")
            return redirect('slider')
        

    return render(request, 'update_form_slider.html', {'update_form':feature_form})


def delete_slider(request, id):
    feature_data = Slider_Model.objects.get(id=id)
    feature_data.delete()
    messages.success(request, "Delete slider !..")
    return redirect('slider')


# feature-------------------------------------------------------
def feature(request):
    
    feature_img = Feature_Model.objects.all()
    return render(request, "feature.html", {'feature':feature_img})

def feature_view(request):
    
    feature_img = Feature_Model.objects.all()
    return render(request, "feature_view.html", {'feature':feature_img})

def feature_form(request):
    form = FeatureForm()

    if request.method == 'POST':
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Add new feature !..")
            return redirect('feature')
       
    
    
    return render(request, 'feature_form.html', {'feature_form': form})


def feature_open_view(request, id):
    feature_data = Feature_Model.objects.get(id=id)
    return render(request, "feature_open_view.html", {'feature': feature_data})  # Ensure context is a dictionary



def update_feature(request, id):
    feature_data = Feature_Model.objects.get( id=id)
    feature_form = FeatureForm(instance=feature_data)

    if request.method=='POST':
        feature_form = FeatureForm(request.POST,instance=feature_data)
        if feature_form.is_valid():
            feature_form.save()
            messages.success(request, "update feature  !..")
            return redirect('feature')
        

    return render(request, 'update_form.html', {'update_form':feature_form})


def delete_feature(request, id):
    feature_data = Feature_Model.objects.get(id=id)
    feature_data.delete()
    messages.success(request, "Delete Featurw , password !..")
    return redirect('feature')






# profile--------------------

@login_required
def user_profile(request):
    try:
        user_profile = Register_Model.objects.get(email=request.user.email)  # Fetch by email
    except Register_Model.DoesNotExist:
        user_profile = None  

    return render(request, 'profile.html', {'user': request.user, 'profile': user_profile})


def member(request):
    member_img=Register_Model.objects.all()
    return render(request , 'members.html', {'member':member_img} )


# admin------------------------------
def admin(request):

    return render(request ,'admin.html')


# user edit----------------------------------

def user_data(request):
    register  = Register_Form()
    register_data = Register_Model.objects.all()
    feedback_data = Feedback_Model.objects.all()
    
    
    return render (request , 'user.html' , {'register_form': register , 'register_data':register_data , 'feedback_data':feedback_data})
    

def user_view(request,id):
    
    register_data = Register_Model.objects.get(id=id)
    return render (request , 'user_view.html' , {'register_data':register_data })


def update_user(request, id):
    user_data = Register_Model.objects.get( id=id)
    user_form = Register_Form(instance=user_data)

    if request.method=='POST':
        user_form = Register_Form(request.POST,instance=user_data)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "update user  !..")
            return redirect('user-data')
        

    return render(request, 'user_update.html', {'update_form':user_form})



def delete_user(request, id):
    user_data = Register_Model.objects.get(id=id)
    user_data.delete()
    messages.success(request, "Delete Featurw , password !..")
    return redirect('user-data')

