import os
import logging

logger = logging.getLogger(__name__)


def backtowork(event):
    osname = os.uname()[0].lower()
    if osname == 'linux':
        if os.system('notify-send "Zope is up and running !"'):
            logger.warning("Could not send notification. Is the CLI tool"
                           "notify-send available?")
    elif osname == 'darwin':
        os.environ['G_TITLE'] = 'Zope'
        if os.system('growlnotify "Zope is up and running !"'):
            logger.warning("Could not send notification. Is the CLI tool"
                           "growlnotify available?")
    else:
        logger.warning("Sorry, no notification support for your OS yet. "
                       "Care to add it?")
