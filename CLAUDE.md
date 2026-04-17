# Pythonisas

## Context
Blog educativo de Python y Pygame para alumnos de Formación Profesional (DAM/ASIR). Publicamos prácticas, tutoriales y recursos orientados al aprendizaje por proyectos (ABP). El sitio es estático, generado con Hugo y desplegado automáticamente en GitHub Pages.

## Current Focus
- [x] Práctica 3.1 — SQLite con Python (CRUD)
- [x] Práctica 3.2 — POO con perros ASCII (Pyrro)
- [x] POO — Naves espaciales, coches y Python
- [x] Práctica 3.3 — Modelando naves espaciales
- [x] Práctica 3.4 — Herencia y coches eléctricos
- [x] Práctica 3.5 — Refactoriza el duelo de naves espaciales
- [x] Pygames en itch.io — showcase de juegos Pygame

## Important Files
- `content/blog.org` — Fuente única de todos los posts (ox-hugo). Cada post es un heading `**` con propiedades `:EXPORT_*:`
- `config.toml` — Configuración de Hugo (baseURL, tema smol, idioma español, zona horaria Madrid)
- `static/images/` — Imágenes de los posts (PNG, JPG, BMP)
- `static/code/` — Código descargable para las prácticas (ficheros incompletos para alumnos)
- `content/posts/` — Markdown generado por ox-hugo (no editar a mano)
- `content/pages/inicio.md` — Landing page con índice de prácticas y recursos
- `.github/workflows/hugo.yaml` — CI/CD: build Hugo + deploy a GitHub Pages

## Commands
```bash
# Preview local (con borradores)
hugo server -D

# Build producción
hugo --gc --minify

# Exportar un post desde Emacs (ox-hugo)
# Posicionar cursor en el heading ** del post, luego:
# C-c C-e H H  (org-hugo-export-wim-to-md)

# Exportar desde emacsclient
emacsclient --eval '(with-current-buffer (find-file-noselect "content/blog.org") (goto-char (point-max)) (re-search-backward "TITULO DEL POST") (org-hugo-export-wim-to-md))'

# Monitorizar deploy
gh run watch
```

## Conventions
- Contenido en español, tono informal ("tú"), orientado a estudiantes de FP
- Cada post en `blog.org` usa propiedades ox-hugo: `:EXPORT_FILE_NAME:`, `:EXPORT_HUGO_SECTION: posts`, `:EXPORT_HUGO_PUBLISHDATE:`, `:EXPORT_HUGO_URL:`, `:EXPORT_HUGO_TAGS:`
- Tag `prácticas` para ejercicios con entrega y rúbrica; otros tags para artículos de recurso
- Headings `***` = h2 en el post, `****` = h3
- Código fuente de prácticas: se ofrece un fichero incompleto con huecos `___` y `...` para que el alumno complete
- Imágenes referenciadas como `[[/images/nombre.png]]` en org (Hugo las sirve desde `static/images/`)
- Posts con estado `TODO` = borrador (Hugo `draft: true`), `DONE` = publicado

## Stack técnico
- **Org-mode + ox-hugo**: Escribimos en un solo fichero `blog.org` en Emacs. Cada heading `**` es un post. `ox-hugo` exporta a Markdown con front matter TOML
- **Hugo v0.160.1** (extended): Generador estático. Tema `smol` (minimalista, sin JS, sin Sass)
- **GitHub Actions**: Un workflow (`hugo.yaml`) hace build + deploy a GitHub Pages en cada push a `main`
- **Flujo**: Escribir en Org → `C-c C-e H H` → genera `.md` en `content/posts/` → `git push` → CI/CD → live
