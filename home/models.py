from django.db import models


# makemigrations - create changes and store in a file
# migrate - apply the pending changes in the file created by makemigrations

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=122, null=False)
    email = models.CharField(max_length=122, null=False)
    phone = models.CharField(max_length=12, null=False)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class snp(models.Model):
    name = models.CharField(max_length=122, unique=False)
    email = models.CharField(max_length=122, unique=True)
    phno = models.CharField(max_length=122, unique=True)
    pswd = models.CharField(max_length=122, unique=False)
    fltn = models.CharField(max_length=50, null=True)
    priv = models.IntegerField(null=True, default=0)
    def __str__(self):
        return self.name

class forum(models.Model):
    mail = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    cata = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    def __str__(self):
        return self.name


class prk(models.Model):
    fltn = models.CharField(max_length=50)
    prkno = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    emp = models.BooleanField(default=False)
    d_in = models.CharField(max_length=100)
    d_out = models.CharField(max_length=100)
    dist = models.CharField(max_length=50)
    wing = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class event(models.Model):
    head = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    month = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    email = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.head

class trck(models.Model):
    name = models.CharField(max_length=122,null=True)
    fltn = models.CharField(max_length=122,null=True)
    wi = models.CharField(null=True)
    altp = models.CharField(null=True) #estimated time to spend
    alotpark = models.CharField(null=True)
    intime = models.DateTimeField(null=True)
    outtime = models.DateTimeField(null=True)
    phno = models.CharField(max_length=122, null=True)
    res = models.BooleanField(null=True)
    def __str__(self):
        return self.fltn

class alert(models.Model):
    topic = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    body = models.CharField(max_length=1000)
    disp = models.BooleanField(null=True, default=False)
    def __str__(self):
        return self.topic