from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Review)
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
class PurchaseModelAdmin(admin.ModelAdmin):
    list_display=['user','mango','date','order_status']
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.order_status == "pending":
            subject="Your order is Placed"
            body=render_to_string('order_placed_mail.html',{"user":obj})
            email=EmailMultiAlternatives(subject,'',to=[obj.user.email])
            email.attach_alternative(body,'text/html')
            email.send()
        if obj.order_status == "runnig":
            subject="Your order is Runnig"
            body=render_to_string('order_runnig_mail.html',{"user":obj})
            email=EmailMultiAlternatives(subject,'',to=[obj.user.email])
            email.attach_alternative(body,'text/html')
            email.send()
        elif obj.order_status =='completed':
            subject="Your order is Completed"
            body=render_to_string('order_completed.html',{"user":obj})
            email=EmailMultiAlternatives(subject,'',to=[obj.user.email])
            email.attach_alternative(body,'text/html')
            email.send()
        elif obj.order_status =="cancelled":
           mango=models.MangoModel.objects.get(id=obj.mango.id)
           mango.weight+=obj.quantity
           mango.save()
           subject="Your order is Cancelled"
           body=render_to_string('order_cancelled_mail.html',{"user":obj})
           email=EmailMultiAlternatives(subject,'',to=[obj.user.email])
           email.attach_alternative(body,'text/html')
           email.send()
           


            
admin.site.register(models.AddressModel)

admin.site.register(models.PurchaseModel,PurchaseModelAdmin)