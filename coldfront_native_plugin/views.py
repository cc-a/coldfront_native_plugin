from django.shortcuts import render
from django.conf import settings

def demo_view(request):
    return render(request, 'coldfront_native_plugin/demo.html', context={"value":
        settings.NATIVE_PLUGIN_VALUE})
