from enum import unique
from time import timezone
from django.db import models
from django.utils.html import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Banners(models.Model) :
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    class Meta :
        verbose_name_plural = 'Banners'

    def __str__(self) :
        return self.alt_text

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


class Services(models.Model) :
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img = models.ImageField(upload_to="services/", null=True)

    def __str__(self) :
        return self.title

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))

class Gallery(models.Model) :
    text_alt = models.TextField()
    img = models.ImageField(upload_to="gallery/", null=True)

    def __str__(self) :
        return self.text_alt

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    massege = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.full_name
    

class Custamer(models.Model) :
    custamer_name = models.CharField(max_length=150)
    reviwe = models.CharField(max_length=200)
    img = models.ImageField(upload_to="Custamer_imgs/", null=True)
    def __str__(self) :
        return self.custamer_name

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


class Prudect(models.Model) :
    p_name = models.CharField(max_length=150)
    details = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    img = models.ImageField(upload_to="Prudect_imgs/", null=True)
    alt_text = models.CharField(max_length=20)



class SocialLink(models.Model):
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    twiter = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)

    def __str__(self) :
        return self.facebook
    
    def __str__(self) :
        return self.instagram
    
    def __str__(self) :
        return self.twiter
    
    def __str__(self) :
        return self.whatsapp