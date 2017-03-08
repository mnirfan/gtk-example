#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject, GLib
import time

def slow_stuff(job, cancellable, user_data):
    print("entering slow_stuff()")
    for i in range(10):
        print("finished in", i)
        time.sleep(1)
    print("finished")
    print(job)

class Utama(Gtk.Window):
    def __init__(self):
        GObject.threads_init()
        Gtk.Window.__init__(self)
        print("Starting...")
        Gio.io_scheduler_push_job(slow_stuff,
                                  None,
                                  GLib.PRIORITY_DEFAULT,
                                  None)

if __name__ == "__main__":
    u = Utama()
    u.show_all()
    Gtk.main()
