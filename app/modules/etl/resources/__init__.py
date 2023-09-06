from app.extensions.api import api


def init_app():

    from .etl import ns as ns_etl

    api.add_namespace(ns_etl, path="/etl")