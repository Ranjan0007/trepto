from django.db import models

class SGXNifty(models.Model):
    last_trade = models.CharField(max_length=100)
    change = models.CharField(max_length=100)
    change_percent = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_trade} - {self.timestamp}"