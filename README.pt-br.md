# Playwright Quotes Scraper 

Uma leve pipeline ETL (Extract, Transform, Load) em Python para realizar scraping de dados e paginação no site [Quotes to Scrape](https://quotes.toscrape.com/) via Playwright de forma automatizada e resiliente, processar os dados segundo as regras de negócio adotadas no projeto e persistir em formato CSV.

🌐 *Leia isto em [English](README.md).* 

## Funcionalidades

- **Abertura e acesso do browser:** gerencia a inicialização e navegação do browser Chromium de forma resiliente.
- **Resiliência:** implementa tratamento de timeout, tentativas de navegação e fallback com recarregamento da página para casos de falha no carregamento de conteúdo.
- **Transformação de dados:** limpa, sanitiza (remoção de aspas e espaços NBSP), descarta incompletos e deduplica os dados O(1).
- **Persistência:** exporta dados processados ​​para um arquivo CSV, sobrescrevendo o arquivo existente para a mesma data de execução.
- **Testes unitários:** testes com Pytest cobrindo as regras de sanitização, validação e deduplicação dos dados.

## Tecnologias e Conceitos Aplicados

- **Python 3.11+**
- **Playwright:** automação e gerenciamento de navegação web.
- **Pandas:** estruturação e exportação dos dados.
- **Pytest:** cobertura de testes unitários.
- **Gerenciamento Centralizado de Configurações:** Parâmetros de execução (URL base, timeouts, retentativas e modo headless) parametrizados e isolados no módulo `config/settings.py`.
- **Separação de responsabilidades & PEP 8:** camadas desacopladas (browser, scraper, cleaner, storage) com type hints e docstrings.

## Instalação e Uso

### Quickstart

Clone o repositório e entre na pasta do projeto:
```bash
git clone [https://github.com/SEU_USUARIO/playwright-quotes-scraper.git](https://github.com/SEU_USUARIO/playwright-quotes-scraper.git)
cd playwright-quotes-scraper
```

### Criar e ativar um ambiente virtual

No Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

No Linux/macOS (Bash):
```bash
python -m venv .venv
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
playwright install chromium
```

### Executar a pipeline ETL

```bash
python main.py
```

### Saída

Os conjuntos de dados processados serão gravados no diretório `data/`:

- `data_aaaa-mm-dd.csv` — CSV em `UTF-8-sig` para perfeita compatibilidade com Excel e Power BI.

Dica: abra a pasta após a execução para verificar os arquivos gerados:

Windows PowerShell:
```powershell
explorer.exe .\data
```

Linux/macOS:
```bash
xdg-open data || open data
```

## Testes

Execute a suíte de testes com `pytest`:

```bash
python -m pytest
```

## Estrutura do projeto

```
playwright-quotes-scraper/
├── config/
│   ├── logger.py          # Configuração e formatação de logs do sistema
│   └── settings.py        # Centralização de parâmetros e constantes de execução
├── data/                  # Conjuntos de dados gerados (.csv)
├── src/
│   ├── browser.py         # Gerenciamento e resiliência do browser
│   ├── scraper.py         # Extração de dados e paginação
│   ├── cleaner.py         # Sanitização, validação e deduplicação
│   └── storage.py         # Persistência e exportação em arquivo CSV
├── tests/
│   └── test_cleaner.py    # Suíte de testes unitários
├── main.py                # Orquestrador principal da pipeline
├── requirements.txt
├── README.md
└── README.pt-br.md
```