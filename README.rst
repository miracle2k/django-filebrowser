Changes from original django-filebrowser:
=========================================

Removed dependency on django-grappelli.

New way to install the django-filebrowser urlset. Instead of adding
the urls manually::

    (r'^admin/filebrowser/', include('filebrowser.urls')),

You need to create a custom AdminSite, and include the filebrowser
mixin::

	from filebrowser.admin import FilebrowserAdmin
	class MyAdminSite(admin.AdminSite, FilebrowserAdmin):
		pass

This will ensure that filebrowser is wrapped inside
``self.admin_view()``, including support for your custom a
``admin_view`` implementation.

For a more recent port, see also:
    https://github.com/wardi/django-filebrowser-no-grappelli
