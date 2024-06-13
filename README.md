**Projeto Conexão Alimentar**

**Visão Geral**

O sistema "Conexão Alimentar" foi criado pensando em um meio facilitador para o registro de doações alimentares. O projeto pode ser utilizado por um ponto de coleta já existente para controle das entradas ou pode se tornar um ponto de coleta próprio. As funções de login e rastreamento são dependentes dessas possíveis integrações e não foram implementadas de início.

Na prática, ele pode ser usado em pontos de doações para controle ou pode ser escalonado para se tornar o próprio ponto de coleta físico. O projeto se tornará escalável à medida em que sua usabilidade for definida.

**Estrutura**

A estrutura do projeto é composta pelo framework Django, e a sua conexão com o MongoDB é realizada através da biblioteca PyMongo.


**Integrantes**

  - Eryck Ribeiro Lino
  - Fernando Claudiano
  - Frank Lima
  - Isabela B. M. Almeida
  - João Augusto Selegatto Pacolla


**Logotipo**


**Funcionalidades**

  - Registro de doações alimentares
  - Registro de múltiplos produtos por doação
  - Edição de registros de doações
  - Exclusão de registros de doações
  - Integração futura com pontos de coleta existentes ou novos pontos de coleta próprios


**Tecnologias Utilizadas**

Django: Framework web para o backend e frontend do projeto.

MongoDB: Banco de dados NoSQL utilizado para armazenar as doações e produtos.

PyMongo: Biblioteca utilizada para conectar o Django ao MongoDB.


**Instalação**

*Siga os passos abaixo para configurar e rodar o projeto localmente*

  - Clone o repositório
  - Crie e ative um ambiente virtual
  - Instale as dependências

  - Configure o MongoDB
    
Certifique-se de ter o MongoDB instalado e rodando localmente ou forneça a URL de conexão para um banco de dados MongoDB hospedado.

  - Configure as variáveis de ambiente
  - Rodar as migrações do Django
  - Iniciar o servidor de desenvolvimento
  - Acesse a aplicação: Abra o navegador e vá para http://localhost:8000.


**Contato**
Para mais informações, entre em contato com isabela.almeida4@fatec.gov.br ou crie uma issue no repositório.
