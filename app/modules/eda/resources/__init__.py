from app.extensions.api import api


def init_app():

    from .eda import ns as ns_eda

    api.add_namespace(ns_eda, path="/eda")