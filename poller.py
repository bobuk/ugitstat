from time import sleep
import asyncio
import subprocess
import logging
import os

from configparser import ConfigParser

C = ConfigParser()
C.read('.ugitstat')

class uGitClientProtocol:
    def get_git_log(self):
        git = subprocess.check_output(['git', 'log', '--oneline', '-1'])
        return git.decode('utf-8').split(' ', 1)[0]

    def __init__(self, loop):
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        message = "GIT " + self.get_git_log()
        self.transport.sendto(message.encode('utf-8'))

    def datagram_received(self, data, addr):
        current = self.get_git_log()
        logging.debug("Received:" + str(data))
        data = data.decode().split(' ', 1)
        logging.debug("Close the socket")
        self.transport.close()
        if data[0] == 'GIT':
            logging.debug('Remote version is:' + data[1])
            logging.debug('Local version is:' + current)
            if current != data[1]:
                logging.info('Version is differ, so run command from config # ' + C['client']['command'])
                res = subprocess.check_output(C['client']['command'], shell=True)
                logging.debug("Result: " + res.decode('utf-8'))
        else:
            logging.info('Unknown answer: ' + data[0])


    def error_received(self, exc):
        logging.debug(exc)
        loop = asyncio.get_event_loop()
        loop.stop()

    def connection_lost(self, exc):
        logging.debug("Socket closed, stop the event loop")
        loop = asyncio.get_event_loop()
        loop.stop()

if __name__ == '__main__':
    os.chdir(C['client'].get('repository', '.'))
    logging.basicConfig(format='%(asctime)s %(message)s', level = int(C['client']['logging']))
    loop = asyncio.new_event_loop()
    while True:
        connect = loop.create_datagram_endpoint(
            lambda: uGitClientProtocol(loop),
            remote_addr=(C['client']['server'], 19798))
        transport, protocol = loop.run_until_complete(connect)
        loop.run_forever()
        sleep(int(C['client']['delay']))
    transport.close()
    loop.close()