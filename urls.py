"""
(C) 1995-2024 <YOUR_NAME_HERE> Software Corporation. All Rights Reserved.

The Copyright Owner has not given any Authority for any Publication of this Work.
This Work contains valuable Trade Secrets of <YOUR_NAME_HERE>, and must be maintained in Confidence.
Use of this Work is governed by the Terms and Conditions of a License Agreement with <YOUR_NAME_HERE>.

"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import (
    include,
    re_path)


admin.autodiscover()


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
