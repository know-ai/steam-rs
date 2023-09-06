from app.extensions.api import api


def init_app():

    from .mlo import ns as ns_mlo

    api.add_namespace(ns_mlo, path="/mlo")