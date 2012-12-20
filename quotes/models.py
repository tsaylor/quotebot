from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    speaker = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.quote
