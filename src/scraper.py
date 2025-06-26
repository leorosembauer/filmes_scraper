import requests
from bs4 import BeautifulSoup

class Filme:
    def __init__(self, titulo, classificacao, sinopse):
        self.titulo = titulo
        self.classificacao = classificacao
        self.sinopse = sinopse

    def __repr__(self):
        return f"{self.titulo} ({self.classificacao}): {self.sinopse[:60]}..."

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "classificacao": self.classificacao,
            "sinopse": self.sinopse
        }

class AdoroCinemaScraper:
    BASE_URL = "https://www.adorocinema.com"

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def _get_soup(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def coletar_filmes_em_cartaz(self):
        url = f"{self.BASE_URL}/filmes/em-cartaz/"
        soup = self._get_soup(url)
        filmes = []

        cards = soup.select(".mdl")
        for card in cards:
            titulo_tag = card.select_one(".meta-title-link")
            sinopse_tag = card.select_one(".synopsis")
            nota_tag = card.select_one(".stareval-note")

            if titulo_tag:
                titulo = titulo_tag.text.strip()
                sinopse = sinopse_tag.text.strip() if sinopse_tag else "Sem sinopse"
                nota = nota_tag.text.strip() if nota_tag else "N/A"
                filmes.append(Filme(titulo, nota, sinopse))
        return filmes

    def coletar_melhores_filmes(self):
        url = f"{self.BASE_URL}/filmes/melhores/"
        soup = self._get_soup(url)
        filmes = []

        cards = soup.select(".card.card-entity.card-entity-list.cf")
        for card in cards:
            titulo_tag = card.select_one(".meta-title-link")
            sinopse_tag = card.select_one(".content-txt")
            nota_tag = card.select_one(".stareval-note")

            if titulo_tag:
                titulo = titulo_tag.text.strip()
                sinopse = sinopse_tag.text.strip() if sinopse_tag else "Sem sinopse"
                nota = nota_tag.text.strip() if nota_tag else "N/A"
                filmes.append(Filme(titulo, nota, sinopse))
        return filmes
