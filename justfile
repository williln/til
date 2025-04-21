# Define default recipe for ease of use
default:
    @echo "Specify a command to run. Options include: up, down, kill, bash, test, migrate."

build-internal-readmes:
    python3 scripts/build_subdir_toc.py aws
    python3 scripts/build_subdir_toc.py celery
    python3 scripts/build_subdir_toc.py django
    python3 scripts/build_subdir_toc.py django-rest-framework
    python3 scripts/build_subdir_toc.py drf-yasg
    python3 scripts/build_subdir_toc.py fast-ai
    python3 scripts/build_subdir_toc.py git
    python3 scripts/build_subdir_toc.py github
    python3 scripts/build_subdir_toc.py google
    python3 scripts/build_subdir_toc.py home-office
    python3 scripts/build_subdir_toc.py html
    python3 scripts/build_subdir_toc.py htmx
    python3 scripts/build_subdir_toc.py javascript
    python3 scripts/build_subdir_toc.py kubernetes
    python3 scripts/build_subdir_toc.py mac
    python3 scripts/build_subdir_toc.py markdown
    python3 scripts/build_subdir_toc.py meilisearch
    python3 scripts/build_subdir_toc.py microsoft-dynamics
    python3 scripts/build_subdir_toc.py misc
    python3 scripts/build_subdir_toc.py mkdocs
    python3 scripts/build_subdir_toc.py plata
    python3 scripts/build_subdir_toc.py postgres
    python3 scripts/build_subdir_toc.py pre-commit
    python3 scripts/build_subdir_toc.py pytest
    python3 scripts/build_subdir_toc.py python
    python3 scripts/build_subdir_toc.py r
    python3 scripts/build_subdir_toc.py seo
    python3 scripts/build_subdir_toc.py slack
    python3 scripts/build_subdir_toc.py sphinx
    python3 scripts/build_subdir_toc.py stripe
    python3 scripts/build_subdir_toc.py squarespace
    python3 scripts/build_subdir_toc.py terraform
    python3 scripts/build_subdir_toc.py wagtail
