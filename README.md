# Portfólio Académico – Django

## Descrição

Este projeto consiste no desenvolvimento de uma aplicação web em Django para gestão de um portfólio académico.

O sistema permite representar:
- Licenciatura
- Unidades Curriculares
- Projetos
- Tecnologias
- Competências
- Trabalhos Finais de Curso (TFC)
- Experiência Profissional

---

## Tecnologias Utilizadas

- Python  
- Django  
- SQLite  
- PlantUML  
- GitHub  

---

## Funcionalidades

- Modelação de dados com múltiplas entidades  
- Relações 1:N e N:N  
- Administração de dados através do Django Admin  
- Importação de TFCs via ficheiro JSON  
- Script de carregamento de Unidades Curriculares  

---

## Estrutura do Projeto

- `core/models.py` → definição das entidades  
- `load_tfcs.py` → importação de TFCs  
- `load_ucs.py` → carregamento de unidades curriculares  
- `informacoes.md` → descrição da modelação  

---

## Como Executar

### 1. Instalar dependências
```
pip install django
```

### 2. Executar migrações
```
python manage.py migrate
```

### 3. Criar superutilizador
```
python manage.py createsuperuser
```

### 4. Executar servidor
```
python manage.py runserver
```

### 5. Aceder ao admin
```
http://127.0.0.1:8000/admin
```

---

## Carregamento de Dados

### TFCs
```
python load_tfcs.py
```

### Unidades Curriculares
```
python load_ucs.py
```

---

## Observações

A API da Universidade Lusófona foi inicialmente considerada para carregamento de dados, no entanto não se encontrava disponível.

Como alternativa, foram utilizados dados simulados para garantir o funcionamento do sistema.

---

## Autor

- Nome: Vinícius Vasconcellos Cardoso
- Curso: Engenharia Informática
