from src.scraper import AdoroCinemaScraper
from utils.io_utils import salvar_em_csv, salvar_resumo_txt_historico

def main():
    scraper = AdoroCinemaScraper()
    filmes = scraper.coletar_filmes_em_cartaz()

    print("\n🎬 Filmes em Cartaz:\n")
    for f in filmes:
        print(f"- {f.titulo} ({f.classificacao}): {f.sinopse[:50]}...")

    salvar_em_csv([f.to_dict() for f in filmes], "filmes_em_cartaz.csv")

    try:
        salvar_resumo_txt_historico(filmes)
    except Exception as e:
        print(f"❌ Erro ao salvar resumo: {e}")

    print("\n✅ Dados e resumo salvos.")

if __name__ == "__main__":
    main()
