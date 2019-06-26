from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

#練習します
class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4)
    diagnosis_name = models.CharField(max_length=150, null=True)
    filler = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)

    def __str__(self):
        #return '&lt;id:' + str(self.id) + '[' + self.diagnosis_name + '_' + str(self.diller) + '_' + str(self.date) + ']&gt;'
        return self.id

class Prac_icf(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    body = models.TextField(max_length=1000, null=True)
    activity = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.id

class Prac_MMT_shoulder_right(models.Model):
    id=models.CharField(max_length=100, primary_key=True)
    flexion=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    extension=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    abduction=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    adduction=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    lateral_rotation=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    medial_rotation=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.id

class Prac_MMT_shoulder_left(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    flexion=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    extension=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    abduction=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    adduction=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    lateral_rotation=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )
    medial_rotation=models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.id
