from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=100, null=True)
    des = models.TextField()


    def __str__(self):
        return self.name


class Taglag(models.Model):
    pro_lang = models.CharField(max_length=50)


    def __str__(self):
        return self.pro_lang


class Tag_level(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Tagjob(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Dev(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    Describe_yourself = models.TextField(max_length=500)
    location = models.CharField(max_length=250)
    profile_pic = models.FileField(upload_to='images/')
    lang = models.ManyToManyField(Taglag)
    other_lang = models.CharField(max_length=50, default="new")
    level = models.ManyToManyField(Tag_level )#default="midlevel"
    job = models.ManyToManyField(Tagjob, default="fulltime")

    def __str__(self):
        return self.name
