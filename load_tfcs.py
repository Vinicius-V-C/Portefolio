import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portefolio.settings")
django.setup()

from core.models import TFC

with open("data/tfcs.json", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados:
    TFC.objects.create(
        titulo=item.get("titulo", ""),
        ano=item.get("ano", ""),
        licenciatura=item.get("licenciatura", ""),
        sumario=item.get("sumario", ""),
        link_pdf=item.get("link_pdf"),
        imagem=item.get("imagem"),
        palavras_chave=", ".join(item.get("palavras_chave", [])),
        areas=", ".join(item.get("areas", [])),
        tecnologias=", ".join(item.get("tecnologias", [])),
        rating=item.get("rating", 0)
    )

print("TFCs carregados com sucesso!")