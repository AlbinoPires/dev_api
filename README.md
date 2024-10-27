# 👋 Olá, eu sou Albino Pires, espero que esteja bem!


## 🌐 Onde me encontrar

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/albino-pires-b188391b3/)
- [![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:albinofp34@gmail.com)
- [![DIO](https://img.shields.io/badge/DIO-30A3DC?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAKlBMVEUBCQn///8AAADMzMzX19fGxsYxMTHs7OypqanU1NQsLCwzMzNdXV2ampqysrKg2cPMAAAAAXRSTlMAQObYZgAAAP9JREFUeF7t2qEJwiAQRNGZyP9Xzr4W0NBBA8+YkUdm7p+al0FCIiCAQCBBgO+BX8dGZNBjJXyD8UK1y8GAQHBwAAAAAAAAAAAAB8x/wuJ3tnN/C+HYTnZO8LN+SrmU2/klrTG/VqXWQt6SbvmNbclY/TGWaTXc6zxVqXt8lrbGR2xJSfbbVmLVyxrpJlLtc0WW0ayDtvTNeUX2+6iMbUl77DduI/F7lmHMyLdsb+wPZtp45Fxb5l+nMOqMxqSc5PZUl2dG9KM4l9Kmvr67Rs5S8fQwAAAAAElFTkSuQmCC)](https://www.dio.me/users/albinofp34)

# Curso na DIO Desenvolvendo Rest APIs Com Python e Flask: 

- **O que foi aplicado?**  
📚 Estudo em API Rest com Flask e FlaskRestful 💻 🐍

# 🚀 Hard Skills

- Python Developer JR 🐍
- Python & API REST com Flask🐍
- Python & Flask-RESTful 🐍
- Git (Versionamento de Código) 🔧
- Linux (Ubuntu 22.04.4)🐧
- Redes - Conexão SSH 🔒


# REST API com Flask e Flask-RESTful

Este repositório contém uma implementação de uma API RESTful utilizando Flask e Flask-RESTful, onde manipulamos dados relacionados a desenvolvedores e suas habilidades. A API permite criar, consultar, atualizar e excluir registros de forma simples e eficiente, seguindo as boas práticas de APIs RESTful.

## Funcionalidades

- **GET**: Retorna a lista de desenvolvedores ou um desenvolvedor específico baseado em seu ID.
- **POST**: Permite a criação de novos desenvolvedores e suas respectivas habilidades.
- **PUT**: Atualiza informações de um desenvolvedor já existente, utilizando o ID.
- **DELETE**: Remove um desenvolvedor específico da lista através de seu ID.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework leve para desenvolvimento web.
- **Flask-RESTful**: Extensão do Flask para criação de APIs RESTful de forma rápida e simples.
- **Postman**: Ferramenta utilizada para testar a API.

## Nota de uso e experiência:

- **Uso Flask-RESTful**: Uso do Flask-RESTful: O Flask-RESTful oferece uma solução leve e direta para APIs simples, mas limitações surgem ao tentar manipular módulos com dados estruturados na lógica. Experimentei várias incertezas ao lidar com erros persistentes ao iterar entre módulos e lógica de dados. Minha recomendação é manter a estrutura simples e modularizar apenas quando necessário, especialmente em APIs de baixa complexidade. Para projetos que exigem manipulação avançada ou dados altamente estruturados, pode ser mais eficiente considerar frameworks mais robustos e especializados, já que essa não é a finalidade principal do Flask-RESTful.


## Instalação

Para rodar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/AlbinoPires/dev_api.git
   ```

2. Entre no diretório do projeto:

   ```bash
   cd dev_api
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o servidor:

   ```bash
   python app.py
   ```

6. Acesse a API em `http://127.0.0.1:5000`.

## Exemplos de Uso

### Listar todos os desenvolvedores (GET)

```http
GET /dev/
```

### Inserir novo desenvolvedor (POST)

```http
POST /dev/
```
Body:
```json
{
  "responsavel": "Albino Pires",
  "tarefa": "Desenvolver API REST",
  "status": "Em andamento"
}
```

### Atualizar um desenvolvedor pelo ID (PUT)

```http
PUT /dev/<int:id>/
```
Body:
```json
{
  "responsavel": "Albino Pires",
  "tarefa": "Atualizar a API REST",
  "status": "Finalizado"
}
```

### Deletar um desenvolvedor (DELETE)

```http
DELETE /dev/<int:id>/
```

## Estrutura do Projeto

```bash
dev_api/
├── app.py               # Arquivo principal da API
├── venv/                # Ambiente virtual
├── requirements.txt     # Arquivo com as dependências do projeto
└── README.md            # Documentação do projeto
```

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e abrir um pull request com melhorias, novas funcionalidades ou correções de bugs.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

