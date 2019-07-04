
from meross_iot.api import MerossHttpClient


def get_aquarium(httpHandler):
    devices = httpHandler.list_supported_devices()
    for d in devices:
        if d._name == "Aquarium":
            return d
    return None


if __name__ == '__main__':
    httpHandler = MerossHttpClient(email="nico.marcq@gmail.com", password="password")

    # get my device by name
    aquarium = get_aquarium(httpHandler)
    if aquarium is not None:
        channels = aquarium.get_channels()
        if channels[0] is not None:
            aquarium.turn_on_channel(channels[0])


