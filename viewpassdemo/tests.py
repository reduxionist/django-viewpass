from django.test import TestCase


class ViewpassTests(TestCase):

    def test_no_viewpass(self):
        result = self.client.get("/")
        self.assertEqual(result.status_code, 302)

    def test_viewpass(self):
        from viewpass.util import get_viewpass_url

        url = get_viewpass_url('/', 'foo.can_bar')
        result = self.client.get(url)
        self.assertEqual(result.status_code, 200)
