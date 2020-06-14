from django.db import models
import markdown


class Page(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    markdown = models.TextField()
    html = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='pages', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        """
        Use the `markdown` library to create a html representation of the markdown
        """
        self.html = markdown.markdown(self.markdown)
        super(Page, self).save(*args, **kwargs)
