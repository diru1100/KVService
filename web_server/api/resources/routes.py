from .store import KeyValueStore
from .listen import Listener


def initialize_routes(api):
    api.add_resource(KeyValueStore, '/kvstore')
    api.add_resource(Listener, '/listen')
