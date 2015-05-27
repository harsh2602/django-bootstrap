from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
    # Display additional fields on right of first field defined by __unicode_ in models.py
    list_display = ["__unicode__","full_name","timestamp","updated"]
   # class Meta:
    #    model = SignUp
    form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

