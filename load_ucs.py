import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portefolio.settings')
django.setup()

from core.models import UnidadeCurricular, Licenciatura

ucs = [
    {"curricularUnitName": "Programação I", "curricularYear": 1, "semester": 1},
    {"curricularUnitName": "Programação II", "curricularYear": 1, "semester": 2},
    {"curricularUnitName": "Bases de Dados", "curricularYear": 2, "semester": 1},
    {"curricularUnitName": "Sistemas Operativos", "curricularYear": 2, "semester": 2},
    {"curricularUnitName": "Inteligência Artificial", "curricularYear": 3, "semester": 1},
]

lic, _ = Licenciatura.objects.get_or_create(
    nome="Engenharia Informática",
    defaults={
        "instituicao": "Universidade Lusófona",
        "duracao": 3,
        "descricao": "Curso de Engenharia Informática"
    }
)

for uc in ucs:
    UnidadeCurricular.objects.get_or_create(
        nome=uc["curricularUnitName"],
        licenciatura=lic,
        defaults={
            "descricao": "UC do curso",
            "ano": uc["curricularYear"],
            "semestre": uc["semester"]
        }
    )

print("UCs carregadas com sucesso!")