import time

from meross_iot.api import MerossHttpClient


def get_device(http_handler, meross_device):

    if meross_device is not None:
        devices = http_handler.list_supported_devices()
        for d in devices:
            if d._name == "Aquarium":
                return d
    return None


def countdown_task(meross_device, meross_channel, meross_email, meross_password, seconds):
    print("Turn off the device for %s seconds" % seconds)

    http_handler = MerossHttpClient(email=meross_email, password=meross_password)

    # get my device by name
    device = get_device(http_handler, meross_device)
    if device is not None:
        channels = device.get_channels()
        if channels[0] is not None:
            device.turn_off_channel(channels[int(meross_channel)])
            time.sleep(int(seconds))
            print("Turn back on the device")
            device.turn_on_channel(channels[int(meross_channel)])
