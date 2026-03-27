from http.server import HTTPServer, BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):

    # Método GET (já usado antes)
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor funcionando com GET")


    # Método POST (novo)
    def do_POST(self):

        # pega o tamanho dos dados enviados na requisição
        tamanho = int(self.headers['Content-Length'])

        # lê os dados enviados
        dados = self.rfile.read(tamanho)

        # mostra os dados recebidos no terminal
        print("Dados recebidos:", dados.decode())

        # envia resposta para o cliente
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST recebido")


HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()

# Importa classes necessárias para criar um servidor HTTP
from http.server import BaseHTTPRequestHandler, HTTPServer

# Importa biblioteca para trabalhar com JSON
import json

# Classe que define como o servidor responde às requisições
class MeuServidor(BaseHTTPRequestHandler):

    # Método GET: usado para o cliente pedir informações ao servidor
    def do_GET(self):
        # Envia código de status 200 (OK)
        self.send_response(200)

        # Define que a resposta será em formato JSON
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Cria uma resposta em formato de dicionário
        resposta = {
            "mensagem": "Servidor funcionando com GET!"
        }

        # Converte o dicionário para JSON e envia para o cliente
        self.wfile.write(json.dumps(resposta).encode())


    # Método POST: usado para o cliente enviar dados ao servidor
    def do_POST(self):
        # Pega o tamanho dos dados enviados
        tamanho = int(self.headers['Content-Length'])

        # Lê os dados enviados pelo cliente
        dados = self.rfile.read(tamanho)

        # Converte os dados para JSON
        dados_json = json.loads(dados)

        # Mostra no terminal os dados recebidos
        print("Dados recebidos:", dados_json)

        # Envia resposta para o cliente
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        resposta = {
            "status": "Dados recebidos com sucesso!"
        }

        # Envia a resposta em JSON
        self.wfile.write(json.dumps(resposta).encode())


# Configuração do servidor
servidor = HTTPServer(('localhost', 8000), MeuServidor)

# Mensagem no terminal indicando que o servidor está rodando
print("Servidor rodando em http://localhost:8000")

# Mantém o servidor rodando continuamente
servidor.serve_forever()