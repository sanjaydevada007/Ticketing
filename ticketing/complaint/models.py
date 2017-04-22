from django.db import models
from django.core.urlresolvers import reverse


dev_type= (
    ('Phone', 'Phone'),
    ('Tablet', 'Tablet'),
    ('Laptop', 'Laptop'),
    
)

stat_type= (
    ('Open', 'Open'),
    ('Close', 'Close'),
    ('Assigned', 'Assigned'),
    
)


class Ticket(models.Model):
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	device=models.CharField(max_length=30,choices=dev_type)
	status=models.CharField(max_length=30,choices=stat_type,default='Open')


	def get_absolute_url(self):
		return reverse('complaint:detail')
