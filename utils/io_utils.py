import csv
import os
from datetime import datetime

def salvar_em_csv(dados, nome_arquivo):
    if not dados:
        print("Nenhum dado para salvar.")
        return

    os.makedirs("data", exist_ok=True)
    caminho = os.path.join("data", nome_arquivo)
    campos = dados[0].keys()

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(dados)

    print(f"✅ Dados salvos em {caminho}")

def salvar_resumo_txt_historico(filmes_cartaz):
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho = os.path.join("data", f"resultado_{timestamp}.txt")

    try:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("Projeto: filmes_scraper\n\n")
            f.write("Resumo:\n")
            f.write("Coleta de filmes em cartaz pelo site AdoroCinema, com:\n")
            f.write("- Título\n- Classificação (nota)\n- Sinopse curta\n\n")
            f.write("Fonte:\n")
            f.write("https://www.adorocinema.com/filmes/em-cartaz/\n\n")
            f.write(f"Quantidade de filmes em cartaz coletados: {len(filmes_cartaz)}\n")
            f.write(f"Data da coleta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Arquivo gerado:\n- data/filmes_em_cartaz.csv\n")

            # Top 5
            f.write("\nTop 5 filmes com melhores classificações:\n")
            filmes_ordenados = sorted(
                filmes_cartaz,
                key=lambda x: float(x.classificacao.replace(",", ".")) if x.classificacao.replace(",", ".").replace('.', '', 1).isdigit() else 0,
                reverse=True
            )
            for i, filme in enumerate(filmes_ordenados[:5], start=1):
                f.write(f"{i}. {filme.titulo} ({filme.classificacao})\n")

        print(f"✅ Resumo salvo em {caminho}")
    except Exception as e:
        print(f"❌ Erro ao salvar resumo: {e}")
