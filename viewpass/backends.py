"""Authentication backend to support viewpass."""

from django.contrib.auth.backends import ModelBackend


class ViewPassBackend(ModelBackend):
    """Authentication backend that checks for viewpass permission.

    This is the heart of viewpass, used when a viewpass-visiting-user has a
    permission check.

    This checks to see if the permission being sought is the one
    stored on the user as `_viewpass_perm` (this storing is done earlier by
    the middleware).

    To be used, this must be added to your config's `AUTHENTICATION_BACKENDS`.
    """

    def has_perm(self, user_obj, perm, obj=None):
        """Does this user have permission for this object? (check viewpass).

        Args:
            user_obj (User): Django user object.
            perm (str): String name of permission.
            obj (Optional): (Ignored by us).

        Returns:
            bool: does user have permission?
        """

        return perm == getattr(user_obj, '_viewpass_perm', None)
