from typing import Tuple
from datetime import datetime

from django.db import models

from abstracts.models import DateTimeCustom


class Url(DateTimeCustom):  # noqa
    MAX_LINK_LENGHT = 10000
    MAX_ID_LENGHT = 10
    link = models.CharField(
        max_length=MAX_LINK_LENGHT,
        verbose_name='url link'
    )
    uuid = models.CharField(
        max_length=MAX_ID_LENGHT,
        unique=True,
        db_index=True,
        verbose_name='shortened link'
    )

    class Meta:  # noqa
        verbose_name: str = 'Url'
        verbose_name_plural: str = 'Ulr(ы)'
        ordering: Tuple[str] = ('datetime_created',)

    def __str__(self) -> str:  # noqa
        return f'FULL Url link: {self.link}, SHORT URL: {self.uuid}'

    def delete(self) -> None:  # noqa
        self.datetime_deleted = datetime.now()
        self.is_deleted = True
        self.save(
            update_fields=['datetime_deleted', 'is_deleted']
        )
