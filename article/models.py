from django.db import models
# from django.db.models.deletion import CASCADE

from account.models import Account
    
class Posts(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.user.__str__() + ' on ' + self.time.__str__()

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'The posts'

