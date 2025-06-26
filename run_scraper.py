from src.scraper import AdoroCinemaScraper
from utils import salvar_em_csv, salvar_resumo_txt_historico

def main():
    scraper = AdoroCinemaScraper()

    filmes_cartaz = scraper.coletar_filmes_em_cartaz()
    print("\n🎬 Filmes em Cartaz:\n")
    for filme in filmes_cartaz:
        print(f"- {filme}")
    salvar_em_csv("data/filmes_em_cartaz.csv", filmes_cartaz)

    melhores_filmes = scraper.coletar_melhores_filmes()
    print("\n🏆 Melhores Avaliados:\n")
    for filme in melhores_filmes:
        print(f"- {filme}")
    salvar_em_csv("data/melhores_filmes.csv", melhores_filmes)

    caminho_resumo = salvar_resumo_txt_historico("data", len(filmes_cartaz), len(melhores_filmes))
    print(f"\n✅ Dados e resumo salvos. Arquivo resumo: {caminho_resumo}")

if __name__ == "__main__":
    main()
