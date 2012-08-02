.. contents::

Introduction
============

Most systems have some form of notification systems. This library tries to
use them to tell the user that his zope is up and running.
This can be useful in development, when one needs to restart often, and
does not want to watch the system starting up.

Supported operating systems
===========================
 [x] Linux (via ``notify-send``)
 
 [x] Mac (via ``growlnotify`` or ``terminal-notifier``)
 
 [ ] Windows

Linux
-----
If your linux flavor does not provide ``notify-send`` nothing really happens.

Mac OS
------
For MacOS 10.8 you might want to use the notification system via `terminal-notifier 
<https://github.com/alloy/terminal-notifier/downloads>`_ since Growl is no longer free. 

For MacOS 10.x-10.7 you need `Growl notification system <http://growl.info>`_ and ``growlnotify``
extra script. Otherwise, nothing will happen.
See `official instructions <http://growl.info/extras.php#growlnotify>`_ for
installing growlnotify script.



Installation
============
Add the package name ot the eggs part of your zope2 instance and rerun buildout.
