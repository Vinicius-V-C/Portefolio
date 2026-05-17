import json

from django.core.management.base import BaseCommand

from portefolio.models import TFC


class Command(BaseCommand):

    help = 'Importa TFCs do JSON'

    def handle(self, *args, **kwargs):

        with open('portefolio/data/tfcs.json', encoding='utf-8') as ficheiro:

            dados = json.load(ficheiro)

            for item in dados:

                TFC.objects.create(

                    titulo=item['titulo'],

                    ano=item['ano'],

                    licenciatura=item['licenciatura'],

                    sumario=item['sumario'],

                    link_pdf=item['link_pdf'],

                    imagem=item['imagem'],

                    palavras_chave=', '.join(item['palavras_chave']),

                    areas=', '.join(item['areas']),

                    tecnologias=', '.join(item['tecnologias']),

                    rating=item['rating']

                )

        self.stdout.write(
            self.style.SUCCESS('TFCs importados com sucesso')
        )