from django.db import models
from django.template.defaultfilters import slugify 

class Menu(models.Model):
    title = models.CharField(max_length=255)
    greeting = models.TextField()
    slug = models.SlugField('Slug', null=True, blank=True, max_length=255, help_text="if not supplied, slug will auto-generate from title.") # model slug (generated at save)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Menu,self).save(*args, **kwargs)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    menu = models.ForeignKey(Menu)
    slug = models.SlugField('Slug', null=True, blank=True, max_length=255, help_text="if not supplied, slug will auto-generate from title.") # model slug (generated at save)
    order = models.IntegerField('Order')

    class Meta:
        ordering = ['order']
        unique_together = (('menu','slug'),)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(MenuItem,self).save(*args, **kwargs)
