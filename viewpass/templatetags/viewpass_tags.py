"""Template tags for viewpass."""

from django import template

from viewpass.util import get_viewpass_url

register = template.Library()


@register.simple_tag(takes_context=True)
def viewpass_url(context, perm):
    """Return a URL path for current path, viewpass-encoded with permission.

    Args:
        context (Context): context of template tag
        perm (str): permission to grant

    Returns:
        str: URL path with embedded viewpass information.

    To use this, in a template:

    .. code-block:: jinja

       {% viewpass_url 'View' %}

    This would return a URL with embedded, cryptographically-signed information about the
    `View` permission in it
    """

    path = context.request.path
    return get_viewpass_url(path, perm)
