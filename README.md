
# 🤖 wpp_bot

**WhatsApp Automático em Python**

---

## 📝 Descrição do Projeto

O **wpp_bot** é um bot de automação para WhatsApp, desenvolvido em Python, que utiliza técnicas de web scraping e automação de navegador para interagir com o WhatsApp Web.
O projeto permite o envio de mensagens em massa, respostas automáticas e execução de tarefas repetitivas de comunicação, aumentando a eficiência e otimizando seu tempo.

---

## ✨ Recursos Principais

* ✅ **Envio de Mensagens em Massa:** Envie a mesma mensagem para uma lista de contatos predefinida.
* ✅ **Sistema de Contatos:** Gerencie números de telefone através do diretório `contacts/`.
* ✅ **Templates de Mensagem:** Utilize modelos de texto dinâmicos armazenados no diretório `message/`.
* ✅ **Automação de Navegador:** Uso do ChromeDriver para simular a interação humana no WhatsApp Web.

---

## ⚙ Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

* Python 3.x
* Git
* Google Chrome (ou outro navegador compatível com o WebDriver configurado no projeto)

---

## 🚀 Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/lucas-souza-code/wpp_boot.git
cd wpp_boot
```

### 2. Criar e Ativar o Ambiente Virtual

**Para Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Para Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o WebDriver

O projeto inclui o ChromeDriver na pasta `drivers/chromedriver-win64`.
Certifique-se de que a versão do seu Google Chrome seja compatível ou substitua pelo WebDriver adequado.

---

## 🛠 Configuração do Projeto

### A. Lista de Contatos

Insira os nomes e telefones no arquivo `list.xlsx` dentro do diretório `data/`.

### B. Templates de Mensagens

O diretório `message/` contém arquivos de texto (`message.txt`) com o conteúdo das mensagens que serão enviadas.
Edite conforme a necessidade da sua automação.

---

## ▶ Como Usar

Para iniciar a automação, execute o script principal:

```bash
python main.py
```

O bot abrirá uma janela do navegador. Na primeira execução, será necessário escanear o QR Code do WhatsApp Web.

> ⚠️ A pasta `dist/` contém a versão finalizada do projeto, pronta para execução.

---

## 💻 Tecnologias Utilizadas

* Python 3.x
* Selenium/WebDriver: Para automação de navegador (interação com o WhatsApp Web)
* Pandas: Para manipulação de arquivos `.xlsx`
* Outras bibliotecas conforme `requirements.txt`

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para sugerir melhorias, siga os passos:

1. Faça um fork do projeto
2. Crie uma nova branch:

```bash
git checkout -b feature/minha-melhoria
```

3. Comite suas mudanças:

```bash
git commit -m "feat: Adiciona nova funcionalidade X"
```

4. Faça push para a branch:

```bash
git push origin feature/minha-melhoria
```

5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🧑‍💻 Autor

| Nome     | Lucas Souza                                                   |
| -------- | ------------------------------------------------------------- |
| GitHub   | [lucas-souza-code](https://github.com/lucas-souza-code)       |
| LinkedIn | www.linkedin.com/in/lucas-santos-code                           |
| Email    | [lucas.network15@gmail.com](mailto:lucas.network15@gmail.com) |

---

