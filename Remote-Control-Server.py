import socket
import hashlib

from mcdreforged.api.decorator import new_thread

PLUGIN_METADATA = {
    'id'     : 'remote_control',
    'version': '1.0.0',
    'name'   : 'Remote Control MCDR',
    'author' : 'shenjack and DXbai_zhou',
    'link'   : 'https://github.com/DXbai-zhou/MCDR-Remote-Control'
}


@new_thread('RemoteThread_ClientHandler')
def client_handler(server, tcp_client, tcp_client_address):
    is_asking = True
    while is_asking:
        gets = tcp_client.recv(2048).decode()  # gets:list
        if gets == 'exit':
            is_asking = False
            continue
        else:
            server.execute(gets)


@new_thread('RemoteThread')
def dispose_client_request(server):
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ts.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    ts.bind(("127.0.0.1", 12212))
    while True:
        ts.listen(1)
        tcp_client, tcp_client_address = ts.accept()
        


def on_load(server, *args):
    dispose_client_request(server)  # start up main thread
