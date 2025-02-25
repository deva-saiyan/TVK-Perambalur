from django import forms
from .models import Register_Model , Slider_Model ,Feature_Model,Feedback_Model



class Register_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    conform_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Register_Model
        fields = ['photo', 'name','gender', 'DOB','place','ward', 'address', 'contact', 'email', 'id_num', 'id_photo', 'password', 'conform_password']
        
        widgets = {  
            'photo': forms.FileInput(attrs={'class': 'form-control'}),  
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),  
            'gender': forms.Select(attrs={'class': 'form-control'}),  
            'DOB': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your place'}),  
            'ward': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter ward number'}),  
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'rows': 3}),  
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),  
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),  
            'aadhar_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Aadhar ID number'}),  
            'id_photo': forms.FileInput(attrs={'class': 'form-control'}),  
        }  

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        conform_password = cleaned_data.get("conform_password")

        if  password != conform_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    



class Login_Form(forms.Form):
    username = forms.CharField(max_length=20 )
    password = forms.CharField(widget=forms.PasswordInput)


class Slider_Form(forms.ModelForm):
    
    class Meta:
        model = Slider_Model
        fields = ['slider1' , 'slider2' , 'slider3' , 'status' , 'trending']

        widgets = {
            'slider1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'slider2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'slider3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trending': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }




class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature_Model
        fields = ['img1', 'img2', 'img3', 'title', 'description', 'status' , 'trending']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Description'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trending': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }


class Feedback_Form(forms.ModelForm):
    class Meta:
        model = Feedback_Model

        fields =['name' , 'contact' ,  'address' , 'problem']

        widgets = {  
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),  
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),  
            
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address','rows':1 }),  
            'problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the problem', 'rows':1}),  
        } 
