import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TitleSlugMixin(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        unique=True,
        help_text=_("The main textual identifier or name for the content"),
    )

    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        unique=True,
        help_text=_(
            "A URL-friendly version of the title, typically used in"
            "the URL to identify the content's location."
        ),
    )

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        unique=True,
        help_text=_(
            "A URL-friendly version of the title, typically used in"
            "the URL to identify the content's location."
        ),
    )

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        help_text=_(
            "The timestamp indicating when the model instance was"
            "initially added or created."
        ),
    )

    modified = models.DateTimeField(
        _("Modified at"),
        auto_now=True,
        help_text=_(
            "The timestamp representing the most recent update or"
            "modification to the model instance."
        ),
    )

    class Meta:
        abstract = True


class StockUnitMixin(models.Model):
    sku = models.UUIDField(
        verbose_name=_("Stock of Unit"),
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        help_text=_(
            "A unique identifier assigned to each product in inventory."),
    )

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    description = models.TextField(
        verbose_name=_("Description"),
        null=True,
        blank=True,
        help_text=_(
            "A textual explanation or summary providing additional"
            "information about the item's characteristics or purpose."
        ),
    )

    class Meta:
        abstract = True
