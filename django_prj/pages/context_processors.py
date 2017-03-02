from django.conf import settings


def static(requiest):
    if settings.FRONTEND_DEV:
        return {
            'bundle_js': 'http://localhost:3000/static/js/bundle.js',
        }
    if settings.STATIC_ASSET_MANIFEST:
        return {
            'main_css': settings.STATIC_ASSET_MANIFEST.get('main_css'),
            'main_js': settings.STATIC_ASSET_MANIFEST.get('main_js'),
        }
    return {}
