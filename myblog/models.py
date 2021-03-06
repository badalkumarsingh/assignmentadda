from django.db import models
# Create your models here.
class Myblog(models.Model):
    img = models.ImageField(upload_to='pics', blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'blogs'
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Myblog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)