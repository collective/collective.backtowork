.. contents::

Introduction
============

Most systems have some form of notification systems. This library tries to
use them to tell the user that his zope is up and running.
This can be useful in development, when one needs to restart often, and
does not want to watch the system starting up.

Supported operating systems
===========================
[x] Linux (via notify-send)
[ ] Mac
[ ] Windows

If your linux flavor does not provide notify-send nothing really happens.

Installation
============
Add the package name ot the eggs part of your zope2 instance and rerun buildout.
