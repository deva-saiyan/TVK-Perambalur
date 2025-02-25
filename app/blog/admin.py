
# Register your models here.
from django.contrib import admin
from .models import Register_Model , Slider_Model ,Feature_Model,Feedback_Model

admin.site.register(Register_Model)
admin.site.register(Slider_Model)
admin.site.register(Feature_Model)
admin.site.register(Feedback_Model)