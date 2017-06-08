from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    location = models.CharField(max_length=38)
    state = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "id: " + str(self.id) + ", location: " + self.location + ", state: " + self.state

class Instructor(models.Model):
    first_name = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dojo = models.ForeignKey(Dojo, related_name="Instructors")

    def __unicode__(self):
        return "id: " + str(self.id) + ", first_name: " + self.first_name + ", dojo_id: " + str(self.dojo.id) + "dojo_location: " + self.dojo. location

class DryEraseMarker(models.Model):
    color = models.CharField(max_length=39)
    instructor = models.ForeignKey(Instructor, related_name ="dryerasemarkers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.color
