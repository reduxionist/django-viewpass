from django.shortcuts import render

from django.contrib.auth.decorators import permission_required


@permission_required('foo.can_bar')
def test_view(request):
    return render(request, "page.html")
