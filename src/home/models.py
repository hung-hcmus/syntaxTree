from django.db import models

import numpy as np


# Create your models here.
class input_text(models.Model):
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

# arr = [j for j in range(10)]
# print(arr)