from .store import KeyValueStore
from .listen import Listener


def initialize_routes(api):
    # handles routing modularly
    api.add_resource(KeyValueStore, '/kvstore')
    api.add_resource(Listener, '/listen')
