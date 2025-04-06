from django.db import models
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

import markdown


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    summary = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    image = models.URLField(
        blank=True, null=True, help_text="URL de la imagen para RRSS"
    )
    published = models.BooleanField(
        default=False, help_text="Los posts no publicados no se muestran en la página."
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return f"/blog/{self.created_at.year}/{self.slug}/"

    def __str__(self):
        return self.title

    @property
    def summary_text(self):
        if self.summary:
            return strip_tags(
                markdown.markdown(
                    self.summary, extensions=["fenced_code"], output_format="html5"
                )
            )

    @property
    def content_md(self):
        return mark_safe(
            markdown.markdown(
                self.content, extensions=["fenced_code"], output_format="html5"
            )
        )
