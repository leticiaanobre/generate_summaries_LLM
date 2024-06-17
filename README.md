# Google Maps Reviews Scraper and Summarizer

Este projeto consiste em um scraper para coletar reviews de um local no Google Maps e um summarizer para gerar um resumo desses reviews usando a API de geração de texto do Google Generative AI.

## Funcionalidades

- **Scraping de Reviews**: Coleta reviews de um local específico no Google Maps.
- **Tradução de Reviews**: Tradução dos reviews coletados para o inglês usando a biblioteca `googletrans`.
- **Resumo de Reviews**: Gera um resumo dos reviews traduzidos usando a API do Google Generative AI.

## Pré-requisitos

- Python 3.6 ou superior
- Google Chrome
- Instalar as dependências do projeto

## Instalação

1. **Clone o repositório**:

    ```sh
    git clone https://github.com/leticiaanobre/generate_summaries_LLM.git
    cd generate_summaries_LLM
    ```

2. **Crie um ambiente virtual** (recomendado):

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. **Instale as dependências**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Configurar a chave da API**:

    - Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

      ```env
      API_KEY=your_api_key_here
      ```

    - Substitua `your_api_key_here` pela sua chave de API do Google Generative AI.

## Uso

1. **Execute o script principal**:

    ```sh
    python main.py
    ```

2. **Insira a URL do Google Maps** do local que você deseja coletar os reviews.

3. **Veja o resumo** dos reviews coletados e traduzidos.

## Estrutura do Projeto

- `main.py`: Script principal que executa o scraping, tradução e geração de resumo.
- `config.py`: Arquivo de configuração que carrega a chave da API do arquivo `.env`.
- `requirements.txt`: Lista de dependências do projeto.

## Dependências

- `google-generativeai`
- `pyppeteer`
- `googletrans`
- `python-dotenv`

## Contribuição

Contribuições externas não são aceitas neste projeto. Se você encontrar um problema ou tiver uma sugestão, por favor, abra uma issue no repositório.

