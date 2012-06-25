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
        if os.system('growlnotify -t "Zope is up and running !" -m "You can go back to work ..."'):
            logger.warning("Could not send notification. Are growl and"
                           "growlnotify tool available?")
    else:
        logger.warning("Sorry, no notification support for your OS yet. "
                       "Care to add it?")
