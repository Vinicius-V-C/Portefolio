# MODELAGEM INICIAL – PORTFÓLIO

## Entidades:
- Licenciatura  
- UnidadeCurricular  
- Projeto  
- Tecnologia  
- TFC  
- Competencia  
- Formacao  
- Docente  
- MakingOf  
- (Extra) ExperienciaProfissional  

A entidade ExperienciaProfissional foi incluída para enriquecer o portfólio, permitindo representar experiências além do contexto académico.

---

## ATRIBUTOS:

### Observação:
Cada atributo foi definido com base na sua utilidade prática dentro da aplicação.

---

### Entidade: Licenciatura
- id  
- nome, identifica o curso  
- instituicao, fornece contexto académico  
- duracao, representa a estrutura do curso  
- descricao, permite adicionar informação relevante  

**Justificações:**
- O atributo nome identifica claramente o curso frequentado.  
- O atributo instituicao contextualiza o percurso académico.  

---

### Entidade: UnidadeCurricular
- id  
- nome  
- descricao  
- ano  
- semestre  
- imagem  

**Justificações:**
- Ano e semestre permitem organização cronológica.  
- A imagem melhora a apresentação visual da aplicação.  

---

### Entidade: Docente
- id  
- nome  
- email  
- pagina_lusofona  
- foto  

**Justificações:**
- O email permite contacto direto.  
- A página Lusófona garante ligação oficial.  

---

### Entidade: Projeto
- id  
- nome  
- descricao  
- imagem  
- video_demo  
- github_link  

**Justificações:**
- O GitHub é essencial em contexto profissional.  
- O vídeo permite demonstrar o funcionamento.  

---

### Entidade: Tecnologia
- id  
- nome  
- tipo  
- descricao  
- logotipo  
- site_oficial  
- nivel_interesse  

**Justificações:**
- O tipo permite organização (linguagem, framework, etc.).  
- O nível de interesse representa domínio/conhecimento.  

---

### Entidade: TFC
- id  
- titulo  
- descricao  
- ano  
- classificacao  
- licenciatura  
- link_pdf  
- imagem  
- palavras_chave  

**Justificações:**
- O atributo classificacao permite destacar desempenho.  
- O link_pdf permite acesso direto ao trabalho.  
- As palavras-chave facilitam pesquisa e organização.  

---

### Entidade: Competencia
- id  
- nome  
- nivel  
- descricao  

**Justificações:**
- O nível diferencia grau de domínio.  
- A descrição detalha a competência.  

---

### Entidade: Formacao
- id  
- nome  
- instituicao  
- data_inicio  
- data_fim  
- descricao  

**Justificações:**
- Datas permitem organização temporal.  
- A descrição detalha os conteúdos adquiridos.  

---

### Entidade: ExperienciaProfissional
- id  
- empresa  
- cargo  
- descricao  
- data_inicio  
- data_fim  
- aprendizagem  

**Justificações:**
- O atributo aprendizagem evidencia evolução profissional.  

---

### Entidade: MakingOf
- id  
- descricao  
- data  
- imagem  
- decisao  
- erro  
- correcao  

**Justificações:**
- Permite documentar o processo de desenvolvimento.  
- Regista decisões, erros e aprendizagens.  

---

## RELAÇÕES:

- Licenciatura 1 --- N UnidadeCurricular  
- UnidadeCurricular 1 --- N Projeto  
- UnidadeCurricular N --- N Docente  

- Projeto N --- N Tecnologia  
- Projeto N --- N Competencia  

- Tecnologia N --- N Competencia  

- Formacao N --- N Competencia  
- ExperienciaProfissional N --- N Competencia  

- TFC N --- N Tecnologia  

- MakingOf N --- 1 Projeto  
- MakingOf N --- 1 Tecnologia  
- MakingOf N --- 1 UnidadeCurricular  

---

## EXPLICAÇÕES DAS RELAÇÕES:

As relações N:N foram utilizadas sempre que uma entidade pode estar associada a múltiplas instâncias de outra.

Exemplos:
- Um projeto utiliza várias tecnologias  
- Uma tecnologia pode ser utilizada em vários projetos  

---

## JUSTIFICAÇÕES DE MODELAGEM:

Inicialmente, algumas relações foram modeladas como 1:N, mas foram corrigidas para N:N após análise mais detalhada.

A entidade Tecnologia foi separada de Projeto para evitar redundância e melhorar a normalização.

A entidade ExperienciaProfissional foi adicionada para enriquecer o portfólio.

A entidade MakingOf foi criada para documentar o processo de desenvolvimento.

---

## CARREGAMENTO DE DADOS (TFCs)

Foi utilizado um ficheiro JSON contendo dados reais de TFCs.

Foi desenvolvido um script Python (`load_tfcs.py`) que:
- lê o ficheiro JSON  
- processa os dados  
- insere na base de dados utilizando o ORM do Django  

Durante este processo:
- foi necessário adaptar o modelo TFC  
- foram adicionados novos atributos (ex: link_pdf, palavras-chave)  

Os dados foram carregados com sucesso e validados no Django Admin.

---

## CARREGAMENTO DE UNIDADES CURRICULARES

Foi desenvolvido um script (`load_ucs.py`) para inserir automaticamente unidades curriculares na base de dados.

Inicialmente foi tentada a utilização da API da Universidade Lusófona, no entanto, esta não se encontrava disponível (erro 404).

Como alternativa, foram utilizados dados simulados para garantir o funcionamento do sistema.

As unidades curriculares foram corretamente associadas à licenciatura através de uma relação ForeignKey.

Os dados foram validados no Django Admin.

---

## DJANGO ADMIN

O Django Admin foi configurado para melhorar a usabilidade:

- list_display para visualizar campos importantes  
- search_fields para permitir pesquisa  
- list_filter para facilitar navegação  

Exemplo:

```python
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'classificacao')
    search_fields = ('titulo',)
    list_filter = ('ano',)