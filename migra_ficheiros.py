import os

from django.core.files import File

from portefolio.models import (
    Docente,
    UnidadeCurricular,
    Tecnologia,
    Projeto,
    MakingOf
)

# =========================
# DOCENTES
# =========================

for obj in Docente.objects.all():

    if obj.foto and obj.foto.name:

        local_path = obj.foto.path

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.foto.save(

                    os.path.basename(local_path),

                    File(f),

                    save=True

                )

            print(f"Docente migrado: {obj}")


# =========================
# UCS
# =========================

for obj in UnidadeCurricular.objects.all():

    if obj.imagem and obj.imagem.name:

        local_path = obj.imagem.path

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.imagem.save(

                    os.path.basename(local_path),

                    File(f),

                    save=True

                )

            print(f"UC migrada: {obj}")


# =========================
# TECNOLOGIAS
# =========================

for obj in Tecnologia.objects.all():

    if obj.logotipo and obj.logotipo.name:

        local_path = obj.logotipo.path

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.logotipo.save(

                    os.path.basename(local_path),

                    File(f),

                    save=True

                )

            print(f"Tecnologia migrada: {obj}")


# =========================
# PROJETOS
# =========================

for obj in Projeto.objects.all():

    if obj.imagem and obj.imagem.name:

        local_path = obj.imagem.path

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.imagem.save(

                    os.path.basename(local_path),

                    File(f),

                    save=True

                )

            print(f"Projeto migrado: {obj}")


# =========================
# MAKING OF
# =========================

for obj in MakingOf.objects.all():

    if obj.imagem and obj.imagem.name:

        local_path = obj.imagem.path

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.imagem.save(

                    os.path.basename(local_path),

                    File(f),

                    save=True

                )

            print(f"MakingOf migrado: {obj}")