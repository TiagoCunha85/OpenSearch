import json
from opensearchpy import OpenSearch
from opensearchpy.helpers import bulk

# Configurações de conexão
host = 'localhost'  # Ou o endereço do container (localhost, porque o Docker redireciona a porta 9200)
port = 9200         # Porta padrão mapeada no Docker
auth = ('admin', 'SuaSenhaForte123!')  # Autenticação conforme definida no Docker Compose

# Criação do cliente OpenSearch
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=True,  # SSL habilitado
    verify_certs=False  # Desabilita a verificação de certificados SSL (como no Docker Compose)
)

# Verificação da conexão
if client.ping():
    print("Conectado ao OpenSearch!")
else:
    print("Não foi possível conectar ao OpenSearch.")
    exit(1)

# Nome do índice
index_name = 'contato'

# Criação do índice, se não existir
if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name)
    print(f"Índice '{index_name}' criado.")
else:
    print(f"Índice '{index_name}' já existe.")

# Caminho do arquivo JSON com os dados
file_path = 'data.json'

# Lendo os dados do arquivo JSON
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)  # Carrega os dados do JSON

# Preparando os documentos para inserção
documents = [
    {'_index': index_name, '_source': document} for document in data
]

# Inserindo os documentos em massa no OpenSearch
success, _ = bulk(client, documents)
print(f"{success} documentos inseridos com sucesso.")
