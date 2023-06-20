from django.db import models

#model to keep track of the number of visits of the site
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255)

    def __str__(self):
        return self.ip_address
