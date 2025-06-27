import pandas as pd

class FilmesAnalyzer:
    def __init__(self, caminho_arquivo_csv):
        self.caminho_arquivo_csv = caminho_arquivo_csv
        self.df = None

    def carregar_dados(self):
        self.df = pd.read_csv(self.caminho_arquivo_csv)

    def exibir_top_filmes(self, n=5, salvar_em_csv=False):
        if self.df is None or self.df.empty:
            print("⚠️ Nenhum dado carregado para análise.")
            return

        # Corrige nome e tipo da coluna de classificação
        if "classificacao" in self.df.columns:
            if self.df["classificacao"].dtype == object:
                self.df["classificacao"] = self.df["classificacao"].str.replace(",", ".")
            self.df["classificacao"] = pd.to_numeric(self.df["classificacao"], errors="coerce")
        else:
            print("⚠️ Coluna 'classificacao' não encontrada.")
            return

        top_filmes = self.df.sort_values(by="classificacao", ascending=False).head(n)

        print(f"\n🏆 Top {n} filmes com melhores classificações:\n")
        for _, row in top_filmes.iterrows():
            print(f"- {row['titulo']} ({row['classificacao']}): {row['sinopse'][:60]}...")

        if salvar_em_csv:
            caminho_saida = "data/top_5_filmes.csv"
            top_filmes.to_csv(caminho_saida, index=False)
            print(f"\n✅ Top {n} filmes salvos em: {caminho_saida}")
