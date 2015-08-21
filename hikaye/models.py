from django.db import models
from django.conf import settings


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='stories')
    parent = models.ForeignKey("self", related_name='children', null=True, blank=True)
    score = models.PositiveIntegerField(default=0)
    is_reported = models.BooleanField(default=False)

    def save(self, **kwargs):
        if not self.title and not self.parent:
            self.title = self.content[:20]

        super(Story, self).save(**kwargs)


    def __str__(self):
        return '< {t:.10} - {c:.20} >'.format(t=self.title, c=self.content)

    @property
    def title_or_parent(self):
        return self.title or 'Parent: ' + self.parent.title

