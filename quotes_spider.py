import scrapy

class TextSpider(scrapy.Spider):
    name = 'text_spider'
    start_urls = ['https://tcrf.net/Mortal_Kombat_II_(SNES)']

    def parse(self, response):
        #extrair todo o texto na página
        textoExtraido = response.css('*::text').extract()

        #gerar arquivo de texto e inserir o texto extraído
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(''.join(textoExtraido))
            #alternativa: file.write('\n'.join(all_text))
