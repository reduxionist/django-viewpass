"""Middleware to support viewpass temporary-access tokens."""

from django.core import signing
from django.core.exceptions import SuspiciousOperation


class ViewPassMiddleware(object):
    """Handles when viewpass is given in the request.

    If the user is presenting a viewpass token in the URL, check its
    authenticity and, if good, store the permission-to-be-granted on the user
    object.
    """

    def process_request(self, request):
        """Grab viewpass information from request, if present.

        Args:
            request (Request): request in process; this is marked-up with permission granted

        Returns:
            None
        """

        # Look on URL for "viewpass" parameter -- if it's there , the user is
        # trying to use a viewpass token

        viewpass = request.GET.get('viewpass')

        if viewpass:

            # The viewpass token is a signed object; use the crypto library to
            # check the signature and decompose into the original object.
            # This will raise an exception if the signature is forged or the
            # object is corrupted -- which is what we'd want to happen.

            info = signing.loads(viewpass)
            path, permission = info

            if path != request.path:
                raise SuspiciousOperation("Viewpass URL does not match")

            # noinspection PyBroadException
            try:
                user = request.user

                # Add onto the user the permission they'll have for this request.
                user._viewpass_perm = permission

            except Exception:
                # Ugh, a bare exception -- but there are so many things that
                # could happen in weird configurations in trying to get a user
                # object at this point, so better safe than sorry.
                pass

        # We do not return a request; doing so would say that we want to skip
        # all other middleware and Django processing. Instead, we return None.


