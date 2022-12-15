from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

from tekir.customcontent import _


class ICustomFolder(model.Schema):
    """A custom folder."""

    title = schema.TextLine(
        title=_("Name"),
    )

    description = schema.Text(
        title=_("A short summary"),
    )

    model.primary("detail")
    detail = RichText(
        title=_("Detail"),
        required=False,
    )
