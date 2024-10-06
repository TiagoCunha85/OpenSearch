import json
import pdfkit
import requests

def gerar_relatorio(dados):
    html_content = "<h1>Relatório de Dados</h1><table><tr><th>ID</th><th>Nome</th></tr>"
    
    for dado in dados:
        html_content += f"<tr><td>{dado['_id']}</td><td>{dado['_source']['nome']}</td></tr>"
    
    html_content += "</table>"
    
    pdfkit.from_string(html_content, 'relatorio.pdf')

def carregar_dados():
    url = 'http://localhost:9200/contato/_search'
    response = requests.get(url)
    dados = response.json()
    return dados['hits']['hits']

if __name__ == '__main__':
    dados = carregar_dados()
    gerar_relatorio(dados)
