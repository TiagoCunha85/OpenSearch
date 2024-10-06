from opensearchpy import OpenSearch, ConnectionError

# Configurações de conexão
host = 'http://localhost:9200'  # Use 'https' se necessário
index_name = 'contatos'

# Criar cliente OpenSearch
try:
    es = OpenSearch(host)

    # Testar a conexão
    if not es.ping():
        print("Falha na conexão.")
    else:
        print("Conexão bem-sucedida!")

        # Criar o índice se não existir
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)
            print(f"Índice '{index_name}' criado com sucesso.")

        # Documento a ser indexado
        documento = {
            'nome': 'Sofia Andrade',
            'email': 'sofia.andrade@gmail.com',
            'telefone': '(84) 91234-5679',
            'cns': '123456789012346'
        }

        # Indexar documento
        try:
            response = es.index(index=index_name, body=documento)
            print("Documento indexado com sucesso:", response)
        except Exception as e:
            print(f"Erro ao indexar o registro {documento}: {e}")

except ConnectionError as ce:
    print(f"Erro de conexão: {ce}")
