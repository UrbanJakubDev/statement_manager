from django.db import models


class Base(models.Model):

	# ID and timestamps are automatically created
	id = models.AutoField(primary_key=True)

	# server generated timestamps
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_archived = models.BooleanField(default=False)

	class Meta:
		abstract = True
	
class Unit(Base):
	idf = models.CharField(max_length=255)
	ean = models.CharField(max_length=255)

	# Initialize unit
	def __init__(self, idf, ean):
		self.idf = idf
		self.ean = ean

	def __str__(self):
		return 

	def __unicode__(self):
		return 


	# Methods to get single Unit
	@staticmethod
	def get_by_id(id):
		return Unit.objects.get(id=id)

	@staticmethod
	def get_by_idf(idf):
		return Unit.objects.get(idf=idf)

	@staticmethod
	def get_by_ean(ean):
		return Unit.objects.get(ean=ean)

	# Methods to get multiple Units
	@staticmethod
	def get_all():
		return Unit.objects.all()