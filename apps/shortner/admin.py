from typing import Tuple

from django.contrib import admin

from shortner.models import Url


@admin.register(Url)
class UrlModel(admin.ModelAdmin):  # noqa
    list_display: Tuple[str] = (
        'link', 'uuid', 'is_deleted',
        'datetime_created', 'datetime_deleted',
    )
    readonly_fields: Tuple[str] = (
        'uuid', 'is_deleted',
        'datetime_created', 'datetime_deleted',
    )
