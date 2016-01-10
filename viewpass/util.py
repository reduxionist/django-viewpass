"""Utility code for viewpass."""

from django.core import signing


def get_viewpass_url(path, perm):
    """Returns viewpass encoded path for this path and permission.

    Args:
        path (str): site path you want a token for. For example, '/report/'
        perm (str): permission you want a token for. For example, 'reporting.view_report'

    Returns:
        str: path with a "viewpass" GET request token.
            This token has a crypto-signed version of the path/permission so, when this
            URL is used, the viewpass middleware can trust this and give the user
            permission to visit that URL.
    """

    token = signing.dumps([path, perm])

    if "?" in path:
        return path + "&viewpass=" + token

    else:
        return path + "?viewpass=" + token