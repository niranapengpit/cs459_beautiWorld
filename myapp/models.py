from django.db import models

# Create your models here.	
class BeautyProduct(models.Model):
	CATEGORY = (
        ('SKINCARE', 'Skincare'),
        ('CLEANSING', 'Cleansing'),
        ('MAKEUP', 'Makeup'),
				('VITAMIN', 'Vitamin')
    )
	name = models.CharField(max_length=128)
	producticon = models.ImageField(upload_to = 'images/', default='images/out.png',height_field='image_height',width_field='image_width')
	stock = models.IntegerField(default=0)
	price = models.IntegerField(default=0)
	image_height = models.PositiveIntegerField(100)
	image_width = models.PositiveIntegerField(100)
	category = models.CharField(max_length=10, choices=CATEGORY,default = "SKINCARE")
	def __str__(self):
		return str(self.producticon)