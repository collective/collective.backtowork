import os
import logging

logger = logging.getLogger(__name__)


def backtowork(event):
    if os.uname()[0].lower() == 'linux':
        if os.system('notify-send "Zope up and running"'):
            logger.warning("Could not send notification. Is the CLI tool"
                           "notify-send available?")
    else:
        logger.warning("Sorry, no notification support for your OS yet. "
                       "Care to add it?")
