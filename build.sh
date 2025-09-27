#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Atualiza o pip (opcional)
pip install --upgrade pip

# Instala as dependências via PDM
pdm install

# Coleta os arquivos estáticos (Django)
pdm run python manage.py collectstatic --no-input

# Aplica as migrações (Django)
pdm run python manage.py migrate
