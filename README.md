# testes-software

## Objetivo:
Verificar se o sistema permite que um usuário realize seu cadastro com email e senha válidos, garantindo que os dados sejam corretamente processados e armazenados, e que o usuário seja redirecionado corretamente após o cadastro.

## Pré-condição:
* O sistema deve estar acessível e operacional.
* O endpoint de cadastro de usuário deve estar disponível.
* O banco de dados deve estar configurado para armazenar novos registros de usuários.

## Procedimento de Teste:
Enviar uma requisição POST para o endpoint de cadastro de usuário com os seguintes dados:
    * **Email**: usuario_teste@example.com
    * **Senha**: SenhaSegura123
    * Verificar o código de status da resposta.
    * Verificar se o usuário foi redirecionado para a página de login.
    * Verificar se o usuário foi armazenado corretamente no banco de dados.

## Resultado Esperado:
1. Código de status HTTP 201 (Created) ou 200 (OK).
2. Redirecionamento para a página de login.
3. Dados do usuário armazenados corretamente no banco de dados.

## Resultado Obtido:
1. Código de status HTTP 201.
2. Redirecionamento para a página de login.
3. Dados do usuário armazenados corretamente no banco de dados.

## Pós-condição:
O usuário usuario_teste@example.com está registrado no sistema e pode realizar login com as credenciais fornecidas.

## Conclusão
O teste foi bem-sucedido, confirmando que o sistema permite o cadastro de usuários com email e senha válidos, processa e armazena os dados corretamente, e redireciona o usuário para a página de login após o cadastro.