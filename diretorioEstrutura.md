# Estrutura de pastas do projeto

### Script para gerar a estrutura de pastas
```bash
$excludedFolders = '__init__py', '.venv', 'pycache', '__pycache__', '__init__', 'venv'
$targetDirectory = Get-Location

function Get-DirectoryTree($path, $prefix = '') {
    Get-ChildItem -Path $path -Directory | Where-Object { $excludedFolders -notcontains $_.Name } | ForEach-Object {
        "$prefix+ $($_.Name)"
        Get-DirectoryTree $_.FullName -prefix "$prefix   |"
    }
    Get-ChildItem -Path $path -File | ForEach-Object {
        "$prefix   |--- $($_.Name)"
    }
}

Get-DirectoryTree $targetDirectory | Out-File 'tree.md'
```

```python

+ clas
   |+ migrations
   |   |   |--- __init__.py
   |   |   |--- 0001_initial.py
   |+ templates
   |   |+ clas
   |   |   |   |--- cla_detail.html
   |   |   |   |--- cla_form.html
   |   |   |   |--- cla_list.html
   |   |   |   |--- home.html
   |   |--- __init__.py
   |   |--- admin.py
   |   |--- apps.py
   |   |--- forms.py
   |   |--- models.py
   |   |--- tests.py
   |   |--- urls.py
   |   |--- views.py
+ disciplinas
   |+ migrations
   |   |   |--- __init__.py
   |   |   |--- 0001_initial.py
   |+ templates
   |   |+ disciplinas
   |   |   |   |--- disciplina_detail.html
   |   |   |   |--- disciplina_form.html
   |   |   |   |--- disciplina_list.html
   |   |   |   |--- home.html
   |   |--- __init__.py
   |   |--- admin.py
   |   |--- apps.py
   |   |--- forms.py
   |   |--- models.py
   |   |--- tests.py
   |   |--- urls.py
   |   |--- views.py
+ livros
   |+ migrations
   |   |   |--- __init__.py
   |   |   |--- 0001_initial.py
   |+ templates
   |   |+ livros
   |   |   |   |--- edicao_detail.html
   |   |   |   |--- edicao_form.html
   |   |   |   |--- edicao_list.html
   |   |   |   |--- home.html
   |   |   |   |--- livro_detail.html
   |   |   |   |--- livro_form.html
   |   |   |   |--- livro_list.html
   |   |--- __init__.py
   |   |--- admin.py
   |   |--- apps.py
   |   |--- forms.py
   |   |--- models.py
   |   |--- tests.py
   |   |--- urls.py
   |   |--- views.py
+ personagens
   |+ migrations
   |   |   |--- __init__.py
   |   |   |--- 0001_initial.py
   |   |   |--- 0002_alter_personagem_ficha_pdf.py
   |+ templates
   |   |+ personagens
   |   |   |   |--- home.html
   |   |   |   |--- personagens_detail.html
   |   |   |   |--- personagens_form.html
   |   |   |   |--- pesonagens_list.html
   |   |--- __init__.py
   |   |--- admin.py
   |   |--- apps.py
   |   |--- forms.py
   |   |--- models.py
   |   |--- tests.py
   |   |--- urls.py
   |   |--- views.py
+ wodTimeline
   |   |--- __init__.py
   |   |--- asgi.py
   |   |--- debug.log
   |   |--- settings.py
   |   |--- urls.py
   |   |--- wsgi.py
   |--- .gitignore
   |--- db.sqlite3
   |--- diretorioEstrutura.md
   |--- manage.py
   |--- requirements.txt

```