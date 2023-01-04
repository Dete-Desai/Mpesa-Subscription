from django.db import models
import os
from binascii import hexlify

def _campaignId():
    return hexlify(os.urandom(8))

# Create your models here.

class Code(models.Model):
    msisdncode = models.CharField(max_length=32, primary_key=True, default=_campaignId)

    def __str__(self):
        return self.msisdncode