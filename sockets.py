//Servidor Echo
import socket

def start_echo_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa o socket ao endereço local e porta 12345
    server_socket.bind(('localhost', 12345))
    # Coloca o socket em modo de escuta, permitindo até 5 conexões pendentes
    server_socket.listen(5)
    print("Servidor de Echo iniciado na porta 12345")

    while True:
        # Aceita uma nova conexão
        client_socket, addr = server_socket.accept()
        print(f"Conexão de {addr}")
        # Recebe dados do cliente
        data = client_socket.recv(1024)
        if data:
            # Envia de volta os dados recebidos (eco)
            client_socket.sendall(data)
        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    start_echo_server()
---------------------------------------------------------------------------------------------------------------------------------------------------
//Servidor de Chat
import socket
import threading

# Lista para armazenar os clientes conectados
clients = []

def handle_client(client_socket):
    while True:
        try:
            # Recebe mensagem do cliente
            message = client_socket.recv(1024)
            if message:
                # Envia a mensagem para todos os outros clientes
                broadcast(message, client_socket)
            else:
                # Remove o cliente se a mensagem estiver vazia
                remove(client_socket)
        except:
            continue

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                # Envia a mensagem para o cliente
                client.send(message)
            except:
                # Remove o cliente se houver um erro ao enviar a mensagem
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_chat_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa o socket ao endereço local e porta 12346
    server_socket.bind(('localhost', 12346))
    # Coloca o socket em modo de escuta, permitindo até 5 conexões pendentes
    server_socket.listen(5)
    print("Servidor de Chat iniciado na porta 12346")

    while True:
        # Aceita uma nova conexão
        client_socket, addr = server_socket.accept()
        # Adiciona o cliente à lista de clientes conectados
        clients.append(client_socket)
        print(f"Conexão de {addr}")
        # Cria uma nova thread para lidar com o cliente
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_chat_server()
---------------------------------------------------------------------------------------------------------------------------------------------------
//Servidor de Arquivos
import socket
import os

def handle_client(client_socket):
    # Recebe a solicitação do cliente
    request = client_socket.recv(1024).decode()
    # Extrai o nome do arquivo da solicitação
    filename = request.split()[1]

    if os.path.isfile(filename):
        # Se o arquivo existe, abre e envia o conteúdo do arquivo
        with open(filename, 'rb') as file:
            client_socket.sendall(file.read())
    else:
        # Se o arquivo não existe, envia uma mensagem de erro
        client_socket.send(b"Arquivo não encontrado")

    # Fecha a conexão com o cliente
    client_socket.close()

def start_file_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa o socket ao endereço local e porta 12347
    server_socket.bind(('localhost', 12347))
    # Coloca o socket em modo de escuta, permitindo até 5 conexões pendentes
    server_socket.listen(5)
    print("Servidor de Arquivos iniciado na porta 12347")

    while True:
        # Aceita uma nova conexão
        client_socket, addr = server_socket.accept()
        print(f"Conexão de {addr}")
        # Lida com a solicitação do cliente
        handle_client(client_socket)

if __name__ == "__main__":
    start_file_server()
