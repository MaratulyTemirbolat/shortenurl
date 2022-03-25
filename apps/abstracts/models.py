from django.db import models


class DateTimeCustom(models.Model):  # noqa
    datetime_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    datetime_deleted = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата и время удаления'
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Удален'
    )

    class Meta:  # noqa
        abstract = True
