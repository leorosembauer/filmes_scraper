import csv
import os
from datetime import datetime

def salvar_em_csv(caminho, lista_de_filmes):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", newline='', encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["titulo", "classificacao", "sinopse"])
        writer.writeheader()
        for filme in lista_de_filmes:
            writer.writerow(filme.to_dict())

def salvar_resumo_txt_historico(pasta, qtd_cartaz, qtd_melhores):
    os.makedirs(pasta, exist_ok=True)
    data_coleta = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"resultado_{data_coleta}.txt"
    caminho = os.path.join(pasta, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("Projeto: filmes_scraper\n\n")
        f.write("Resumo:\n")
        f.write("Este projeto realiza web scraping no site AdoroCinema para coletar dois conjuntos de dados:\n\n")
        f.write("1. Filmes em Cartaz\n   - Título do filme\n   - Classificação (nota)\n   - Sinopse curta\n\n")
        f.write("2. Melhores Filmes Avaliados\n   - Título do filme\n   - Classificação (nota)\n   - Sinopse curta\n\n")
        f.write("Fontes:\n")
        f.write("- https://www.adorocinema.com/filmes/em-cartaz/\n")
        f.write("- https://www.adorocinema.com/filmes/melhores/\n\n")
        f.write(f"Quantidade de filmes em cartaz coletados: {qtd_cartaz}\n")
        f.write(f"Quantidade de melhores filmes coletados: {qtd_melhores}\n")
        f.write(f"Data da coleta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("Arquivos gerados:\n")
        f.write("- data/filmes_em_cartaz.csv\n")
        f.write("- data/melhores_filmes.csv\n")

    return caminho
