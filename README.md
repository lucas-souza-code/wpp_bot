🤖 wpp_bot

WhatsApp Automático em Python

📝 Descrição do Projeto
O wpp_boot é um bot de automação para WhatsApp, desenvolvido em Python, que utiliza técnicas de web scraping e automação de navegador para interagir com o WhatsApp Web.
Este projeto visa facilitar o envio de mensagens em massa, respostas automáticas ou a execução de tarefas repetitivas de comunicação, otimizando o tempo e a eficiência.

✨ Recursos Principais
 * ✅ Envio de Mensagens em Massa: Capacidade de enviar a mesma mensagem para uma lista de contatos predefinida.
 * ✅ Sistema de Contatos: Gerenciamento de números de telefone através do diretório contacts/.
 * ✅ Templates de Mensagem: Utilização de modelos de texto dinâmicos armazenados no diretório message/.
 * ✅ Automação de Navegador: Uso do ChromeDriver para simular a interação humana no WhatsApp Web.

   
⚙ Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

 * Python 3.x
 * Git
 * Google Chrome (ou outro navegador compatível com o WebDriver configurado no projeto).

   
🚀 Instalação

Siga os passos abaixo para clonar o repositório e configurar o ambiente de desenvolvimento:

1. Clonar o Repositório
git clone https://github.com/lucas-souza-code/wpp_boot.git
cd wpp_boot

2. Criar e Ativar o Ambiente Virtual
   
É uma boa prática isolar as dependências do projeto.

# Para Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate

3. Instalar as Dependências
As dependências são listadas no arquivo requirements.txt.
pip install -r requirements.txt

4. Configurar o WebDriver
O projeto já inclui um chromedriver na pasta drivers/chromedriver-win64. Certifique-se de que a versão do seu Google Chrome é compatível com o WebDriver fornecido ou substitua-o pelo WebDriver adequado.

🛠 Configuração do Projeto
A funcionalidade do bot depende de como você configura as listas de contatos e as mensagens.

A. Lista de Contatos

Insira a lista com nomes e telefones no arquivo list.xlsx no diretório data 

B. Templates de Mensagens

O diretório message/ contém os arquivos de texto( message.txt ) com o conteúdo das mensagens que serão enviadas. Adapte estes arquivos conforme a necessidade da sua automação.


▶ Como Usar

Para iniciar a automação, execute o script principal.

python main.py

O bot abrirá uma janela do navegador. Você precisará escanear o QR Code do WhatsApp Web na primeira execução. 

💻 Tecnologias Utilizadas
 * Python 3.x
 * Selenium/WebDriver: Para automação de navegador (interação com o WhatsApp Web).
 * Pandas: Para manipulação dos arquivos em .xlsx
 * Outras Bibliotecas (de requirements.txt):

🤝 Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, relatórios de bugs ou melhorias, sinta-se à vontade para:
 * Fazer um Fork do projeto.
 * Criar uma nova Branch (git checkout -b feature/minha-melhoria).
 * Comitar suas mudanças (git commit -m 'feat: Adiciona nova funcionalidade X').
 * Fazer Push para a Branch (git push origin feature/minha-melhoria).
 * Abrir um Pull Request.

   
📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
🧑‍💻 Autor
|  | Lucas Souza |
|---|---|
| GitHub: lucas-souza-code | LinkedIn: [Seu LinkedIn] |

| Email: [lucas.network15@gmail.com] |  |
