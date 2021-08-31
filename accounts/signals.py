from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from accounts.models import Customer

def create_customer_profile(sender,instance,created,**kwargs):
    if created :
         # add customer gp as default
          gp=Group.objects.get(name="customer")
          instance.groups.add(gp)
          #create customer profile for user
          Customer.objects.create(user=instance,email=instance.email)


post_save.connect(create_customer_profile,sender=User)