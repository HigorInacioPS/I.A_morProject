# I.A_marProject
OBS: IA_MAR NÃO SUBSTITUI A AJUDA DE PROFISSIONAIS.


##########################################
ARQUIVO EXECUTAVEL: https://drive.google.com/drive/folders/1o2dNd8VgYnBoIJeOAjaLe6YSslcv0FlL?usp=sharing
##########################################



# I.A_mar - Assistente de Bem Estar Emocional

## Descrição do Projeto

I.A_mar é um assistente virtual de bem-estar emocional construído com Streamlit e a API Gemini da Google. O objetivo principal é oferecer um espaço de apoio e conforto para os usuários, analisando o humor em suas mensagens e respondendo de forma apropriada para promover o bem-estar emocional.

## Funcionalidades

* **Análise de Humor:** Identifica o estado emocional predominante na mensagem do usuário (positivo, negativo ou neutro).
* **Respostas Empáticas:** Gera respostas contextuais e de apoio, adaptando o tom à emoção detectada.
* **Histórico de Conversas:** Mantém um histórico das interações para referência.
* **Interface de Chat Interativa:** Uma interface de chat amigável construída com Streamlit, com rolagem automática para novas mensagens.
* **Barra Lateral com Logomarca:** Exibe a logomarca do projeto na barra lateral esquerda.

## Tecnologias Utilizadas

* **Streamlit:** Framework Python para criar aplicativos web interativos de forma rápida.
* **Google Gemini API:** Modelo de linguagem grande do Google para análise de humor e geração de respostas.
* **python-dotenv:** Para carregar variáveis de ambiente de um arquivo `.env`.
* **Pillow (PIL):** Biblioteca de imagem para manipular e exibir a logomarca.

## Pré-requisitos

Antes de executar o projeto, você precisará ter o seguinte instalado:

* **Python 3.6 ou superior:** Certifique-se de que o Python esteja instalado no seu sistema.
* **pip:** O gerenciador de pacotes do Python.

## Configuração

1.  **Clone o repositório (se aplicável):**
    ```bash
    git clone [https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
    cd seu_projeto
    ```

2.  **Crie um arquivo `.env`:**
    Na raiz do seu projeto, crie um arquivo chamado `.env` e adicione sua chave da API Gemini da Google:
    ```
    GOOGLE_API=SUA_CHAVE_DA_API_GOOGLE
    ```
    **Importante:** Mantenha este arquivo privado e não o compartilhe em repositórios públicos.

3.  **Instale as dependências:**
    Execute o seguinte comando para instalar as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```
    (Você precisará criar um arquivo `requirements.txt` listando as dependências. Veja a seção abaixo.)

## Arquivo `requirements.txt`

Crie um arquivo chamado `requirements.txt` na raiz do seu projeto e adicione as seguintes linhas:

Com certeza, Motoko! Um arquivo README.md é essencial para documentar seu projeto. Aqui está um modelo completo que você pode usar como base, explicando o projeto, como executá-lo e as tecnologias utilizadas.

Crie um arquivo chamado README.md na raiz do seu projeto (na mesma pasta onde está o seu arquivo .py). Cole o seguinte conteúdo dentro dele:

Markdown

# I.A_mar - Assistente de Bem Estar Emocional

## Descrição do Projeto

I.A_mar é um assistente virtual de bem-estar emocional construído com Streamlit e a API Gemini da Google. O objetivo principal é oferecer um espaço de apoio e conforto para os usuários, analisando o humor em suas mensagens e respondendo de forma apropriada para promover o bem-estar emocional.

## Funcionalidades

* **Análise de Humor:** Identifica o estado emocional predominante na mensagem do usuário (positivo, negativo ou neutro).
* **Respostas Empáticas:** Gera respostas contextuais e de apoio, adaptando o tom à emoção detectada.
* **Histórico de Conversas:** Mantém um histórico das interações para referência.
* **Interface de Chat Interativa:** Uma interface de chat amigável construída com Streamlit, com rolagem automática para novas mensagens.
* **Barra Lateral com Logomarca:** Exibe a logomarca do projeto na barra lateral esquerda.

## Tecnologias Utilizadas

* **Streamlit:** Framework Python para criar aplicativos web interativos de forma rápida.
* **Google Gemini API:** Modelo de linguagem grande do Google para análise de humor e geração de respostas.
* **python-dotenv:** Para carregar variáveis de ambiente de um arquivo `.env`.
* **Pillow (PIL):** Biblioteca de imagem para manipular e exibir a logomarca.

## Pré-requisitos

Antes de executar o projeto, você precisará ter o seguinte instalado:

* **Python 3.6 ou superior:** Certifique-se de que o Python esteja instalado no seu sistema.
* **pip:** O gerenciador de pacotes do Python.

## Configuração

1.  **Clone o repositório (se aplicável):**
    ```bash
    git clone [https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
    cd seu_projeto
    ```

2.  **Crie um arquivo `.env`:**
    Na raiz do seu projeto, crie um arquivo chamado `.env` e adicione sua chave da API Gemini da Google:
    ```
    GOOGLE_API=SUA_CHAVE_DA_API_GOOGLE
    ```
    **Importante:** Mantenha este arquivo privado e não o compartilhe em repositórios públicos.

3.  **Instale as dependências:**
    Execute o seguinte comando para instalar as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```
    (Você precisará criar um arquivo `requirements.txt` listando as dependências. Veja a seção abaixo.)

## Arquivo `requirements.txt`

Crie um arquivo chamado `requirements.txt` na raiz do seu projeto e adicione as seguintes linhas:

streamlit
python-dotenv
google-generativeai
Pillow

## Como Executar o Projeto

1.  **Navegue até o diretório do projeto** no seu terminal.
2.  **Execute o aplicativo Streamlit** com o seguinte comando:
    ```bash
    streamlit run seu_arquivo.py
    ```
    Substitua `seu_arquivo.py` pelo nome do seu arquivo principal do Streamlit.

3.  O aplicativo será aberto automaticamente no seu navegador web (geralmente em `http://localhost:8501`).

## Estrutura de Arquivos (Sugestão)

seu_projeto/
├── seu_arquivo.py         # Arquivo principal do Streamlit
├── .env                   # Arquivo com as variáveis de ambiente (chave da API)
├── Logo IA_mar.png        # Arquivo da logomarca (opcional)
└── README.md              # Este arquivo
└── requirements.txt       # Lista de dependências

## Notas Adicionais

* Certifique-se de ter uma conexão de internet para que o aplicativo possa se comunicar com a API Gemini da Google.
* A qualidade das respostas do assistente depende da capacidade do modelo Gemini e do prompt fornecido.

## Contribuição (Opcional)

Se você deseja que outros contribuam para o seu projeto, adicione uma seção sobre como eles podem fazer isso (por exemplo, enviando pull requests).

## Licença (Opcional)

Adicione informações sobre a licença sob a qual o seu projeto está distribuído.

---

Este arquivo `README.md` fornece uma visão geral completa do seu projeto. Certifique-se de ajustar os detalhes (como o nome do arquivo principal, a descrição e quaisquer notas adicionais) para corresponderem precisamente ao seu projeto.
