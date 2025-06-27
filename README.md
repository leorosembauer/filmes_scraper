# 🎬 filmes_scraper

## Descrição

Projeto em Python que realiza scraping no site [AdoroCinema](https://www.adorocinema.com/filmes/em-cartaz/) para coletar informações de filmes atualmente em cartaz. Os dados extraídos incluem:

- Título do filme  
- Classificação (nota dos usuários)  
- Sinopse curta  

Os dados são salvos automaticamente em um arquivo `.csv`, um arquivo com o top 5 filmes mais bem avaliados (`data/top_5_filmes.csv`), e um resumo da coleta é gerado em `.txt`.

## Estrutura

filmes_scraper/
├── data/
│   ├── filmes_em_cartaz.csv            # Dados completos dos filmes em cartaz  
│   ├── top_5_filmes.csv                # Top 5 filmes com melhores classificações  
│   └── resultado_YYYYMMDD_HHMMSS.txt  # Resumo da coleta  
├── src/
│   ├── scraper.py                      # Scraper principal  
│   └── filmes_analyzer.py              # Lógica para análise simples (não obrigatória)  
├── utils/
│   └── io_utils.py                    # Funções utilitárias de leitura e escrita  
├── run_scraper.py                     # Script principal de execução  
└── requirements.txt                   # Dependências do projeto  

## Instalação e Execução

git clone https://github.com/leorosembauer/filmes_scraper.git
cd filmes_scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

PYTHONPATH=. python3 run_scraper.py
