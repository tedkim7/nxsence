'''
Communication with Discord, updating User status.
'''

import pypresence
import errors
import logging

class Discord():
    def __init__(self, log):
        self.client = pypresence.Presence('1056071283491749928')
        if log:
            self.logging = True
            logging.getLogger(__name__) ## set up logger if the -log flag is set

    def set_user(self, user_name):
        self.user_name = user_name
    
    def connect(self):
        try:
            logging.info('Attempting to establish connection to Discord.')
            self.client.connect()
        except ConnectionRefusedError:
            logging.error("Couldn't find an active Discord instance.")
            raise errors.DiscordError() from None
        logging.info('Connection to Discord established.')
    
    def update(self, large_image, small_image, status, start=None):
        try:
            self.client.update(
                large_image=large_image,
                small_image=small_image,
                details=status,
                start=start
            )
            logging.info(f'Status: {status}')
        except pypresence.exceptions.InvalidID:
            if self.logging:
                logging.error("Couldn't find active Discord instance.")
            raise errors.DiscordError() from None