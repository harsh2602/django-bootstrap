from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.

def home(request):

    if request.user.is_authenticated():
        title = "Welcome %s" %(request.user)
    else:
        title = "Welcome"

    # Add a form here
    #if request.method == "POST":
     #   print request.POST

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form":form
    }

    if form.is_valid():
        instance = form.save(commit=False) #Save the form but do not commit
        #if not instance.full_name:
         #   instance.full_name = "Maverick"
        #instance.save()

        #print instance.email
        #print instance.timestamp

        # Another method ti save data using form cleaned data method
        full_name =form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New empty full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank You"
        }


    #return render(request,"home.html",{})
    return render(request,"home.html",context)
    #return render(request,"base.html",context)

def contact(request):
    title = "Contact Us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():

        form_email =  form.cleaned_data.get("email")
        form_full_name = form.cleaned_data.get("full_name")
        form_message = form.cleaned_data.get("message")
       # print email,full_name,message

     #   for key in form.cleaned_data:
      #      print key
       #     print form.cleaned_data.get(key)

        #for key,value in form.cleaned_data.iteritems():
         #   print key,value
        subject = 'Django Triggered Email'
        message = "%s %s via %s" %(form_full_name, form_message, form_email)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,'harshkhandelwal110@gmail.com']
        mail_html_message = """
        <h1>Django Triggered HTML Mail
        """

        send_mail(subject,
                  message,
                  from_email,
                  to_email,
                  html_message = mail_html_message,
                  fail_silently=False)

    context = {
        "form":form,
        "title":title,
        "title_align_center":title_align_center
    }
    return render(request,"forms.html",context)