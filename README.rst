Viewpass
========

Overview
--------

This is a system for allowing the creation and use of URLs that contain a token that allows
a site visitor, even an anonymous visitor, access to pages that might not normally be allowed
to visit.

For example, say you have a report page at `/report/` that normally requires the permission
'reporting.view_report' to view. However, you'd like to be able to send emails to some friends
to allow them to view this page without needing an account.

Viewpass is:

- a utility to craft URLs with embedded, cryptographically-signed information about a
  permission

- a Django middleware that intercepts URLs with these kind of URLs, and stores information
  about that permission onto the user object.

Installing
----------

Add 'viewpass' to the `INSTALLED_APPS`::

    INSTALLED_APPS = [
        # ...
        'viewpass',
    ]

Add it to the middleware classes: This need to be after the Authentication Middleware (since
we need a user!). A good arrangement could be::

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'viewpass.middleware.ViewPassMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

Add viewpass to the `AUTHENTICATION_BACKENDS`::

    AUTHENTICATION_BACKENDS = [
        'viewpass.backends.ViewPassBackend',
        'django.contrib.auth.backends.ModelBackend'
    ]

.. TODO

    should this stuff be added automatically via AppConfig?

Generating Viewpass URLs
------------------------

You can generate the proper URL for them by using the method `util.get_viewpass_url`, like::

    get_viewpass_url('/report/', 'reporting.view_report')

This URL will look like `/report/?viewpass=STRING1:STRING2` and visitors can use this URL to
visit the `/report/` page.

The STRING1 and STRING2 are encoded versions of the timestamp/path/permission-to-grant and a
signed copy of the path/permission-to-grant, respectively. This prevents any tampering by users
trying to re-use a viewpass URL to view another page or to change the permission granted.
(The timestamp is not used but can be used to create time-limited URLs; you can edit the
`signing.loads()` call in `viewpass.middleware.ViewPassMiddleware` to add a
`max_age=<num_seconds>` parameter).

As a convenience, you can also use the template tag to generate the proper URL. On the template
that is used by `/report/`, you can include::

    {% load viewpass_tags %}
    <a href="{% viewpass_url 'reporting.view_report' %}">Get public URL</a>

This will show a link with the viewpass URL on it.

Credit
======

Viewpass is written and maintained by Joel Burton <joel@joelburton.com>.

