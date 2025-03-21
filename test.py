import requests

# URL do endpoint de cadastro
url = "https://api.exemplo.com/cadastro"

# Dados do usuário para cadastro
dados_usuario = {
    "email": "usuario_teste@example.com",
    "senha": "SenhaSegura123"
}

# Enviar requisição POST para cadastrar o usuário
resposta = requests.post(url, json=dados_usuario)

# Verificar o código de status da resposta
if resposta.status_code == 201:
    print("Teste de cadastro bem-sucedido!")
    print("Código de status:", resposta.status_code)
    print("Redirecionamento para:", resposta.headers.get("Location"))
else:
    print("Falha no teste de cadastro.")
    print("Código de status:", resposta.status_code)
    print("Resposta:", resposta.json())