from django.contrib import admin
from django.conf.urls.defaults import patterns, url, include

from filebrowser.views import (
    browse, mkdir, upload, rename, delete, versions, _check_file, _upload_file)


def make_patterns(admin_site=admin.site):
    return patterns('',
        url(r'^browse/$', admin_site.admin_view(browse), name="browse"),
        url(r'^mkdir/', admin_site.admin_view(mkdir), name="mkdir"),
        url(r'^upload/', admin_site.admin_view(upload), name="upload"),
        url(r'^rename/$', admin_site.admin_view(rename), name="rename"),
        url(r'^delete/$', admin_site.admin_view(delete), name="delete"),
        url(r'^versions/$', admin_site.admin_view(versions), name="versions"),

        # Those were not using admin_view in the original filebrowser
        # urlset (before moving to an admin mixin), so for now we don't
        # apply it here either. Note that _upload_file *is* using it's own
        # decorator to check access nevertheless.
        url(r'^check_file/$', _check_file, name="check"),
        url(r'^upload_file/$', _upload_file, name="do_upload"),
    ), 'filebrowser', 'filebrowser'


class FilebrowserAdmin(admin.AdminSite):
    """Mixin to include in your own admin site subclass (or directly
    inherit from it).

    If you do multiple inheritance, make sure all participants use proper
    super() calls.
    """

    def get_urls(self):
        base_urls = super(FilebrowserAdmin, self).get_urls()
        filebrowser_urls = patterns('',
                url(r'^filebrowser/', include(make_patterns(self)))
            )
        return filebrowser_urls + base_urls