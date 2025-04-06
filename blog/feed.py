from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from .models import Post


class BlogFeed(Feed):
    title = "Marco Richetta - Blog"
    link = "/blog/"
    feed_type = Atom1Feed
    description = "My latest blog posts"

    def items(self):
        return Post.objects.filter(published=True).order_by("-created_at")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary_text or item.content_md

    def item_link(self, item):
        return "/blog/%d/%s/" % (item.created_at.year, item.slug)

    def item_author_name(self, item):
        return "Marco Richetta"

    def get_feed(self, obj, request):
        original_feed = super().get_feed(obj, request)
        # Evitar que el browser lo quiera descargar
        # https://til.simonwillison.net/django/building-a-blog-in-django#user-content-the-atom-feed
        original_feed.content_type = "application/xml; charset=utf-8"
        return original_feed
