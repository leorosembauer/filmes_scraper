from src.scraper import AdoroCinemaScraper
from src.filmes_analyzer import FilmesAnalyzer
from utils.io_utils import salvar_em_csv, salvar_resumo_txt_historico

def main():
    scraper = AdoroCinemaScraper()
    filmes = scraper.coletar_filmes_em_cartaz()

    print("\n🎬 Filmes em Cartaz:\n")
    for f in filmes:
        print(f"- {f.titulo} ({f.classificacao}): {f.sinopse[:60]}...")

    # Salva o CSV com todos os filmes
    salvar_em_csv([f.to_dict() for f in filmes], "filmes_em_cartaz.csv")

    # Salva o resumo em .txt
    salvar_resumo_txt_historico(filmes)

    # Análise: Top 5 filmes mais bem classificados
    analyzer = FilmesAnalyzer("data/filmes_em_cartaz.csv")
    analyzer.carregar_dados()
    analyzer.exibir_top_filmes(n=5, salvar_em_csv=True)

    print("\n✅ Dados e resumo salvos.")

if __name__ == "__main__":
    main()
