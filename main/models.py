from django.db import models
from django.template.defaultfilters import truncatechars
from multiselectfield import MultiSelectField
# Create your models here.
class Photo(models.Model):
	CHOICES = (
	('Feautured', 'Featured'),
	('People', 'People'),
	('Travel', 'Travel'),
	('Nature', 'Nature'),
	('Animal', 'Animal')
	)
	photo = models.ImageField()
	description = models.TextField()
	tag = MultiSelectField(choices = CHOICES)
	author = models.CharField(max_length = 15, default = "Arthur Rose")
	
	@property
	def short_description(self):
		return truncatechars(self.description, 30)
	

	def __str__(self):
		return self.author