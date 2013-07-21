import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from pyee import EventEmitter
import logbook
logger = logbook.Logger('connman-dispatcher')

__all__ = ['detector']


def property_changed(_, message):
    if message.get_member() == "PropertyChanged":
        _, state =  message.get_args_list()
        if state == 'online' and detector.state == 'offline':
            logger.info('network state change: online' )
            detector.emit('up')
            detector.state = 'online'
        elif state == 'idle':
            logger.info('network state change: offline' )
            detector.emit('down')
            detector.state = 'offline'


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
    detector.state = 'offline'
    if is_online:
        detector.emit('up')
        detector.state = 'online'

    mainloop = glib.MainLoop()
    mainloop.run()


detector.run = run
