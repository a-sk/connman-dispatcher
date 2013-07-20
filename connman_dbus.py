import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from pyee import EventEmitter
import logbook
logger = logbook.Logger('connman-dispatcher')

__all__ = 'detector'


def property_changed(_, message):
    if message.get_member() == "PropertyChanged":
        _, state =  message.get_args_list()
        if state == 'online':
            logger.info('network state change: online' )
            detector.emit('up')
        elif state == 'idle':
            logger.info('network state change: offline' )
            detector.emit('down')


detector = EventEmitter()
DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()
bus.add_match_string_non_blocking("interface='net.connman.Manager'")
bus.add_message_filter(property_changed)
manager = dbus.Interface(bus.get_object('net.connman', "/"), 'net.connman.Manager')


def is_online():
    properties = manager.GetProperties()
    if properties['State'] == 'online':
        return True
    return False


def run():
    mainloop = glib.MainLoop()
    mainloop.run()


detector.run = run
detector.is_online = is_online
