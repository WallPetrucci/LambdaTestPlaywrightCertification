LambdaTest Certification - Playwright (PYTHON)
Esse projeto foi criado para atender o desafio da certificação do Lambdatest com Playwright
Foi utilizado Python e Playwright executando a plataforma do LambdaTest e GitPod para executar o projeto.

**Pre-requisitos**
- Python 3
- Conta no LambdaTest

# Executar o projeto com Gitpod
- Instale a extensao do Gitpod no browser
  https://www.gitpod.io/docs/configure/user-settings/browser-extension

- Ao acessar o repositório, clique no botão "Open"
![Screenshot 2024-08-23 at 12 14 42](https://github.com/user-attachments/assets/9941ed99-54ed-451b-9f97-0ea3630a20ba)


- Quando o workspace do GitPod conectar, execute o projeto no terminal
```bash
# Execução em serial
pytest test_playwright.py

# Execução com testes paralelos
pytest test_playwright.py -n 3
```

# Instalação local
```bash
# Clone o repositório
git clone https://github.com/WallPetrucci/LambdaTestPlaywrightCertification

# Entre no diretório do projeto
cd LambdaTestPlaywrightCertification

# Instale as dependências
pip install -r requirements.txt
playwright install-deps
playwright install
```

# Variáveis de ambiente local
Para executar o teste na plataforma da LambdaTest remotamente é necessário configurar as variáveis de ambiente
que ficam no arquivo settings.py (LN11 / LN12)
![image](https://github.com/user-attachments/assets/69976eec-8f76-436f-9047-f35e8cc1e441)

1 - Dentro do LambdaTest na aba "Automation", clique em "Access Key"
![image](https://github.com/user-attachments/assets/a1347bec-9d24-47e1-a3c5-73030ddd91d5)

2 - Configure na sua máquina as variáveis de ambiente com os valores do LambdaTest
```bash
export LT_USERNAME <Username>
export LT_ACCESS_KEY <Access Key>
```

# Executando Local
```bash
# Execução em serial
pytest test_playwright.py

# Execução com testes paralelos
pytest test_playwright.py -n 3
```

**Alguma dúvida? Entre em contato!******

**Contato**
Wallace - Linkedin: https://www.linkedin.com/in/wallacepetrucci - wallacepetrucci@gmail.com

Link do Projeto: https://github.com/WallPetrucci/LambdaTestPlaywrightCertification
