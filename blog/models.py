from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.id)])
