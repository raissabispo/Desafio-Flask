# Desafio-Flask
# Flask Employee Management System


Este é um sistema de gerenciamento de  alunos construído com Flask. Ele permite criar, visualizar e listar os alunos.

 

## Requisitos

 

- Python 3.7+
- pip (gerenciador de pacotes do Python)

 

## Configuração do Ambiente

 

### 1. Clonar o Repositório

 

```bash
git clone https://github.com/raissabispo/Desafio-Flask.git
cd Desafio-Flask
```

 

### 2. Configurar o Ambiente Virtual

 

Crie, ative e instale as bibliotecas em um ambiente virtual para o projeto:
- **Windows:**

 

  ```bash
  python -m venv .venv && .\.venv\Scripts\activate && pip install -r requirements.txt
  ```

 

- **macOS e Linux:**

 

  ```bash
  python -m venv .venv || source .venv/bin/activate || pip install -r requirements.txt
  ```

 

## Executar o Aplicativo

 

Para iniciar o servidor Flask, execute:

 

```bash
python src\app.py
```

 

O aplicativo estará disponível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

 

## Estrutura do Projeto

 
```
src/
├── models/
│   └── alunoController.py
├── controllers/
│   └── alunoController.py
├── views/
│   ├── consulta_matricula.html
│   ├── createpage.html
│   ├── data.html
│   ├── datalist.html
│   ├── delete.html
│   └── mainpage.html
|   └── mostrar_aluno.html
|   └── update.html
├── app.py
├── aluno.db (pode não existir inicialmente)
├── requirements.txt
└── README.md
```

## Contribuição

 

1. Faça um fork do projeto.
2. Crie um branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para o branch (`git push origin feature/nome-da-feature`).
5. Crie um novo Pull Request.
