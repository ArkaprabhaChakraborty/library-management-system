from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core.validators import EmailValidator #new


# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    student_id=models.OneToOneField(User,on_delete=models.CASCADE)
    # email = models.CharField(max_length=100, validators=[EmailValidator()]) #new
    
    #new_addition

    def custom_button(self):
        return format_html(
            '<button type="submit" onclick="this.innerHTML = \'Notification sent\';" class="button">Send notification</button>'
        )
    custom_button.short_description = 'Action'
    custom_button.allow_tags = True
    
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        if request.POST.get('action') == 'notification_changed':
            # If the user clicked the custom button, set the button text to "Notification changed"
            initial['custom_button'] = 'Notification changed'
        return initial
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if request.method == 'POST' and request.POST.get('action') == 'notification_changed':
            # If the user clicked the custom button, redirect back to the change form with a success message
            self.message_user(request, 'Notification changed successfully.')
            return HttpResponseRedirect(reverse('admin:yourapp_student_change', args=[object_id]))
        return super().changeform_view(request, object_id, form_url, extra_context)
   
    #new_addition

    def __str__(self):
        last_4_digits=self.student_id.username[-4:]
        return "{}_{}-{}".format(self.first_name,last_4_digits,self.department)
    

    