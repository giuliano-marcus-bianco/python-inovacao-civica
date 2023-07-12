import scrapy

class RnNatalSpider(scrapy.Spider): # Spider base: faz com que a classe RnNatalSpider herde tudo que é necessário de scrapy.Spider
    name = "rn_natal" # todo raspador Scrapy é excecutado a partir do seu nome
    start_urls = ["https://www.natal.rn.gov.br/dom/"] # primeira requisição
    
    def parse(self, response): # a resposta da requisição da url vai para o método padrão parse
        yield {"body": response.text} # yield é como um return que permite retornar mais de uma vez na mesma função