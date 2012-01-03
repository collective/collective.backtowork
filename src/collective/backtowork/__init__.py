from five import grok
from zope.processlifetime import IProcessStarting
import os
import logging

logger = logging.getLogger(__name__)

@grok.subscribe(IProcessStarting)
def backtowork(event):
    if os.uname()[0].lower() == 'linux':
        if os.system('notify-send "Zope up and running"'):
            logger.warning("Could not send notification. Is the CLI tool"
                           "notify-send available?")
    else:
        logger.warning("Sorry, no notification support for your OS yet. "
                       "Care to add it?")
