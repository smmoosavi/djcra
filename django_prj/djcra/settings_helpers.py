import json
import os

import logging


def load_static_asset_manifest(frontend_build_root, frontend_dev):
    if frontend_dev:
        return {
            'main.js': 'js/bundle.js',
        }

    manifest_path = os.path.join(frontend_build_root, 'asset-manifest.json')
    try:
        with open(manifest_path) as data_file:
            data = json.load(data_file)
        main_css = os.path.relpath(data.get('main.css'), 'static/')
        main_js = os.path.relpath(data.get('main.js'), 'static/')
        return {
            "main_css": main_css,
            "main_js": main_js,
        }
    except Exception as e:
        logging.warning("can't load static asset manifest")
    return None
