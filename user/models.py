from django.db.models import Model, CharField, IntegerField

# Create your models here.

class User(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    company_name = CharField(max_length=50)
    age = IntegerField()
    city = CharField(max_length=50)
    state = CharField(max_length=50)
    zip = IntegerField()
    email = CharField(max_length=100)
    web = CharField(max_length=100)
