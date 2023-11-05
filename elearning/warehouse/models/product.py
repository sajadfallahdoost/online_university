from django.db import models
from django.utils.translation import gettext_lazy as _

from elearning.warehouse.helper.consts import Difficulty, Scope
from painless.models.mixins import (DescriptionMixin, StockUnitMixin,
                                    TimestampMixin, TitleSlugMixin)


class Product(TitleSlugMixin, StockUnitMixin, TimestampMixin, DescriptionMixin):
    """Django model representing a Product."""

    is_buyable = models.BooleanField(
        verbose_name=_("Is Buyable"),
        default=False,
        help_text=_("Can users purchase this item?"),
        db_comment="Can users purchase this item?",
    )

    experience = models.FloatField(
        verbose_name=_("Experience"),
        default=0.00,
        help_text=_(
            "How users feel about using this item, \
                    often indicated by ratings or feedback."
        ),
        db_comment="How users feel about using this item, \
        often indicated by ratings or feedback.",
    )

    difficulty = models.CharField(
        verbose_name=_("Difficulty"),
        max_length=20,
        null=True,
        choices=Difficulty.choices,
        help_text=_("Indicates the level of challenge or complexity."),
        db_comment="Indicates the level of challenge or complexity.",
    )

    priority = models.PositiveIntegerField(
        verbose_name=_("Priority"),
        help_text=_(
            "Ranking items based on importance for \
            resource allocation and decision-making."
        ),
        db_comment="Ranking items based on importance for \
            resource allocation and decision-making.",
    )

    scope = models.CharField(
        verbose_name=_("Product Group"),
        max_length=20,
        choices=Scope.choices,
        help_text=_("Defines the category that this product group belongs to."),
        db_comment="Defines the category that this product group belongs to.",
    )

    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
        help_text=_("its product description"),
        db_comment="description",
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.title}"
