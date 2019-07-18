"""
update this file to implement the following already declared methods:
- enqueue: Should add a member to the list
- dequeue: Should remove and return an element from the top or the bottom of the list (depending on the list mode: FIFO or LIFO)
- get_all: should return the entire list as it is
- size: Should return the total size of the list
"""
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
from random import randint

class Queue:

    def __init__(self, mode='FIFO'):
        self.account_sid = 'AC761170e2a7add93aedc5df0e98793cad'
        self.auth_token = '6bcfc7c21a251fdb59942719e1f13e72'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode


    # Variable that holds the queue's length

    def enqueue(self, item):
        # fill this function with the logic needed to make it work
        if self._mode == 'FIFO' or self._mode == 'LIFO':
            self._queue.insert(0, item.data)
            self.sendMessage("Added "+ str(self.size()) +" in front")
        else:
            self._mode = 'FIFO'


    # This def pops an item from the end of the queue if mode is FIFO or from the front if is LIFO
    def dequeue(self):
        # fill this function with the logic needed to make it work
        if self._mode == 'FIFO':
            self.sendMessage("It's your turn, bye bye")
            self._queue.pop(self.size()-1)
        elif self._mode == 'LIFO':
            self._queue.pop(0)
        else:
            self._mode = 'FIFO'
        pass

    def get_all(self):
        return self._queue
        # fill this function with the logic needed to make it work
        pass

    def size(self):
        return len(self._queue)
        # fill this function with the logic needed to make it work
        pass

    def sendMessage(self,
        body="Hello!"):
            message = self.client.messages \
                        .create(
                            body=body,
                            from_='+56937610029',
                            to='+56954540463'
                        )
            print(message.sid)