from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField(max_length=10, default="")
    instructor_name = models.CharField(max_length=50, default="")
    duration = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")

    objects = models.Manager()
    '''displays saved record as the name of the provided title'''
    def __str__(self):
        return self.title
