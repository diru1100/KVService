from .store import KeyValueStore


def initialize_routes(api):
    api.add_resource(KeyValueStore, '/kvstore')
