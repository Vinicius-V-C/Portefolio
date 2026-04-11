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
- (Extra) ExperienciaProfissional, Decidi incluir ExperienciaProfissional para enriquecer o portfólio além do contexto académico.

---

## ATRIBUTOS:

### Observação:
Ao declarar os atributos de cada entidade, coloquei o atributo e, separado por vírgula, expliquei o porquê da sua existência.

---

### Entidade: Licenciatura
- id  
- nome, identifica o curso  
- instituicao, fornece contexto académico  
- duracao, representa a estrutura do curso  
- descricao, permite adicionar informação relevante  

**Justificações:**
- O atributo nome foi incluído para identificar claramente o curso frequentado.  
- O atributo instituicao permite contextualizar academicamente o percurso.  

---

### Entidade: UnidadeCurricular
- id  
- nome, identifica claramente a UC  
- descricao, permite explicar o conteúdo  
- ano, organiza cronologicamente  
- semestre, organiza cronologicamente  
- imagem, melhora a apresentação visual  

**Justificações:**
- O atributo ano e semestre foram incluídos para organizar as UCs ao longo do percurso académico.  
- O atributo imagem foi adicionado para enriquecer a componente visual da aplicação.  

---

### Entidade: Docente
- id  
- nome  
- email, permite contacto  
- pagina_lusofona, ligação oficial  
- foto, parte visual  

**Justificações:**
- O atributo email permite estabelecer contacto com o docente.  
- O atributo pagina_lusofona garante uma ligação oficial à instituição.  

---

### Entidade: Projeto
- id  
- nome  
- descricao, permite explicar o conteúdo  
- imagem, melhora a apresentação visual  
- video_demo, demonstra o funcionamento  
- github_link, importante para contexto profissional  

**Justificações:**
- O atributo github_link foi incluído por ser relevante em contexto profissional.  
- O atributo video_demo permite demonstrar visualmente o funcionamento do projeto.  

---

### Entidade: Tecnologia
- id  
- nome  
- tipo (linguagem, framework, etc.), permite melhor organização  
- descricao, permite explicar brevemente  
- logotipo, parte visual  
- site_oficial, fonte de referência  
- nivel_interesse (1-5), indica nível de conhecimento/interesse  

**Justificações:**
- O atributo tipo permite categorizar as tecnologias.  
- O atributo nivel_interesse foi incluído para representar o nível de domínio.  

---

### Entidade: TFC
- id  
- titulo  
- descricao, permite explicar o conteúdo  
- ano, organiza cronologicamente  
- classificacao, permite destacar desempenho  

**Justificações:**
- O atributo classificacao permite destacar os melhores trabalhos.  
- O atributo ano permite organizar os TFCs temporalmente.  

---

### Entidade: Competencia
- id  
- nome  
- nivel (iniciante/intermedio/avancado), representa o nível  
- descricao, explica a competência  

**Justificações:**
- O atributo nivel foi incluído para diferenciar o grau de domínio.  
- O atributo descricao permite detalhar cada competência.  

---

### Entidade: Formacao
- id  
- nome  
- instituicao  
- data_inicio  
- data_fim  
- descricao, descreve o que foi aprendido  

**Justificações:**
- Os atributos data_inicio e data_fim permitem organizar cronologicamente as formações.  
- O atributo descricao permite detalhar os conteúdos adquiridos.  

---

### Entidade: ExperienciaProfissional
- id  
- empresa  
- cargo  
- descricao, descreve funções desempenhadas  
- data_inicio  
- data_fim  
- aprendizagem, evidencia conhecimentos adquiridos  

**Justificações:**
- O atributo aprendizagem foi incluído para destacar o crescimento profissional.  
- Os atributos datas permitem organizar a experiência ao longo do tempo.  

---

### Entidade: MakingOf
- id  
- descricao, explica o processo realizado  
- data, organiza cronologicamente  
- imagem, comprova o trabalho realizado  
- decisao, regista decisões tomadas  
- erro, evidencia dificuldades  
- correcao, demonstra aprendizagem  

**Justificações:**
- O atributo erro foi incluído para evidenciar dificuldades encontradas.  
- O atributo correcao permite demonstrar o processo de aprendizagem.  

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

### Projeto ↔ Tecnologia:
Um projeto pode utilizar várias tecnologias e uma tecnologia pode ser usada em vários projetos, justificando a relação N:N.

### UnidadeCurricular ↔ Docente:
Uma unidade curricular pode ter vários docentes e um docente pode lecionar várias unidades curriculares.

### Projeto ↔ Competencia:
Os projetos desenvolvem competências, sendo possível associar várias competências a um projeto.

### Tecnologia ↔ Competencia:
O conhecimento de uma tecnologia contribui para o desenvolvimento de competências.

### Formacao / Experiencia ↔ Competencia:
Formações e experiências profissionais contribuem diretamente para o desenvolvimento de competências.

### TFC ↔ Tecnologia:
Os trabalhos finais de curso utilizam tecnologias, tal como os projetos.

---

## JUSTIFICAÇÕES DE MODELAGEM:

Inicialmente, a tecnologia foi considerada como atributo dos projetos, mas foi posteriormente alterada para uma relação ManyToMany, por representar melhor a realidade.

A entidade ExperienciaProfissional foi adicionada para enriquecer o portfólio e não limitar a informação apenas ao contexto académico.

A entidade MakingOf foi criada para documentar o processo de desenvolvimento, permitindo registar decisões, erros e correções.

---

## MAKING OF:

### Processo de Modelação:

A modelação foi iniciada com um rascunho no papel, onde foram definidas as entidades e algumas relações principais de forma inicial.

Posteriormente, foi utilizada uma ferramenta de IA para gerar o código em PlantUML com base nesse rascunho, permitindo criar um diagrama mais organizado e visual.

Durante esse processo, o modelo foi sendo ajustado progressivamente.

---

### Evolução do Modelo:

Versão 1:  
Modelo inicial feito em papel com definição das entidades.

Versão 2:  
Conversão para PlantUML, permitindo visualizar melhor a estrutura.

Versão 3:  
Ajustes nas relações entre entidades, especialmente nas relações N:N.

---

### Erros e Correções:

Erro: Inicialmente algumas relações foram definidas como 1:N quando na realidade deveriam ser N:N.  
Correção: Após análise e discussão com colegas, essas relações foram corrigidas para ManyToMany.

Erro: Dificuldade em compreender corretamente as ligações entre entidades.  
Correção: Foram realizados ajustes progressivos e validações até obter uma modelação coerente.

---

### Dificuldades e Dúvidas:

A principal dificuldade encontrada foi na definição das relações entre entidades.

Houve dúvidas na escolha entre relações 1:N e N:N, sendo necessário discutir com colegas para chegar a uma solução mais correta.

---

### Decisões de Modelação:

Foi tomada a decisão de ajustar várias relações ao longo do processo, após perceber que algumas não representavam corretamente a realidade.

Seguindo uma abordagem semelhante ao exemplo analisado, optou-se por simplificar algumas ligações do MakingOf, de forma a evitar complexidade excessiva na futura implementação em Django.

---

### Uso de Inteligência Artificial:

Foi utilizada Inteligência Artificial como apoio na geração do código PlantUML a partir do rascunho inicial.

A IA foi também utilizada como suporte para validar a modelação, embora todas as decisões tenham sido analisadas manualmente.

---

### Ferramentas Utilizadas:

- PlantUML  
- GitHub  
- Django  

---

## REGISTOS VISUAIS:

### Versão Inicial:
![DER inicial](media/makingof/DerBasico.png)

### Versão Final:
![DER final](media/makingof/Der.png)

---

## APONTAMENTOS FINAIS:

O modelo foi pensado para ser flexível e permitir evolução ao longo do tempo, acompanhando o crescimento académico e profissional.

Alguns atributos e relações poderão ser ajustados futuramente conforme novas necessidades do portfólio.