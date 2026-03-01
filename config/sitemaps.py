from django.contrib.sitemaps import Sitemap
from listings.models import Listing


class ListingSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Listing.objects.filter(status='approved')
