from flask_assets import Bundle, Environment
from .. import app

bundles = {
    'home_css': Bundle(
        'css/home.css',
        output='gen/home.css')
}

assets = Environment(app)

assets.register(bundles)