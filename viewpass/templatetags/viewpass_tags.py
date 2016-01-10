"""Template tags for viewpass."""

from django import template

from viewpass.util import get_viewpass_url

register = template.Library()


@register.simple_tag(takes_context=True)
def viewpass_url(context, perm, path=None):
    """Return a URL path for current path, viewpass-encoded with permission.

    Args:
        context (Context): context of template tag
        perm (str): permission to grant
        path (str): Path to encode; if none given, uses current path

    Returns:
        str: URL path with embedded viewpass information.

    To use this, in a template:

    .. code-block:: jinja

       {% viewpass_url 'View' %}

    This would return a URL with embedded, cryptographically-signed information about the
    `View` permission in it
    """

    if path is None:
        path = context.request.get_full_path()

        # Don't re-viewpass an existing viewpass URL
        if "viewpass=" in path:
            return path

    return get_viewpass_url(path, perm)
