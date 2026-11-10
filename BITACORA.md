# 📓 Bitácora — Blog Django (proyecto de portfolio)

> **Para qué sirve este archivo:** es la memoria detallada del proyecto. Al terminar cada etapa se actualiza (estado actual + registro de la etapa) y se vuelve a subir al Proyecto de Claude. Así cualquier chat nuevo puede retomar exactamente desde donde quedamos.
>
> También vive dentro del repositorio, así que queda versionado con Git.

---

## 1. Objetivo

Construir **desde cero** un blog en Django con calidad de portfolio, publicado online y con su código en GitHub, **aprendiendo en el camino** cómo funciona cada parte. La meta principal no es solo tener la app, sino poder desarrollar con Django de forma autónoma.

## 2. Entorno

| Elemento | Valor |
|---|---|
| Sistema operativo | Windows |
| Editor | VS Code |
| Python | Python 3.14.7 |
| Django | 6.1.2  |
| Control de versiones | Git (instalado) + GitHub (cuenta creada) |
| Base de datos | SQLite (desarrollo) |
| Repositorio | https://github.com/lucascauhepe-spec/django-blog-audio |
| Deploy previsto | PythonAnywhere (plan gratuito) |

## 3. Decisiones tomadas

| Fecha | Decisión | Motivo |
|---|---|---|
| 2026-10-14 | Empezar un proyecto **nuevo desde cero** (no seguir mutando `django-blog lucas`) | Historial de Git limpio desde el primer commit, consolidar lo aprendido y diseñar bien el modelo desde el principio |
| 2026-10-14 | No conservar los posts de prueba anteriores | Eran solo de prueba |
| 2026-10-14 | Usar **Git + GitHub** desde la Etapa 1 | Aprender la herramienta; el historial de commits también es parte del portfolio |
| 2026-10-14 | El código lo escribe Lucas; Claude explica, muestra y revisa | El objetivo es aprender, no copiar |
| 2026-10-14 | Proyecto `config` + app `blog` | Mismo esquema que ya conozco; el nombre de la app no cambia nada técnico |
| 2026-10-14 | Bootstrap por CDN para el diseño | Resultado prolijo sin agregar herramientas ni complejidad |
| 2026-10-15 | Temática: **blog de producción musical y audio** | Conecta con mi experiencia real como músico y técnico de sonido; contenido propio hace al proyecto más memorable |
| 2026-10-15 | Nombre del blog y del repo: **django-blog-audio** | Descriptivo para el portfolio; el título visible se define en la Etapa 4 |
| 2026-10-15 | El blog (interfaz y contenido) va **en inglés** | Alcance internacional del portfolio |
| 2026-10-15 | `TIME_ZONE = "America/Argentina/Buenos_Aires"`, `LANGUAGE_CODE` queda en `en-us` | Idioma y zona horaria son independientes; las fechas se guardan en UTC y se muestran en hora local |
| 2026-10-15 | Versiones exactas en `requirements.txt` (`pip freeze`) | Que el deploy instale exactamente lo mismo que uso en desarrollo |
| 2026-10-15 | No correr `migrate` hasta la Etapa 2 | Diseñar primero la relación usuarios/posts, antes de que exista la base |
| 2026-10-15 | Código (modelos, campos, URLs, templates, commits) **en inglés**; la bitácora sigue en español | Consistencia con la interfaz en inglés y estándar de la industria |
| 2026-10-15 | Categorías quedan como **extra**, fuera del núcleo | Agregarlas después es una migración simple; primero llegar a una versión publicada |
| 2026-10-15 | **Modelo de usuario propio** (`accounts.User` heredando de `AbstractUser`) | Recomendación oficial de Django: cambiarlo después de la primera migración es muy difícil |
| 2026-10-16 | `Post.status` con `TextChoices`: solo `draft` y `published` (default `draft`) | Lo que pide el alcance; nada se publica sin querer |
| 2026-10-16 | `author` con `on_delete=CASCADE` y `related_name="posts"` | Simple para un blog personal; `user.posts.all()` se lee claro |
| 2026-10-16 | Slug generado en `save()` una sola vez; en el admin es `readonly` (sin `prepopulated_fields`) | Las URLs no cambian y no se rompen los links compartidos |

## 4. Proyectos de referencia

- **`django-blog lucas`** (proyecto anterior): `Post(titulo, autor, likes)`, lista, detalle por `id` y creación con `ModelForm`. Ahora sirve como apunte.
- **`blog_django`** (proyecto del profesor): CRUD completo con slug, `base.html`, búsqueda por GET (`BuscarForm`), estadísticas con `aggregate`, formulario de contacto (`forms.Form`), admin personalizado y 19 tests. Sirve como referencia de cómo resolver cada parte.

## 5. Alcance "portfolio"

Lo que debería tener la versión final:

- [ ] Usuarios: registro, login y logout
- [ ] Posts con autor = `User` real; solo el autor puede editar o borrar los suyos
- [ ] CRUD completo, con validaciones y confirmación antes de borrar
- [ ] Mensajes de feedback ("Post publicado ✓")
- [ ] Borradores y publicados; URLs con slug
- [ ] Búsqueda y paginación
- [ ] Diseño prolijo y responsive (Bootstrap)
- [ ] Tests automáticos
- [ ] Secretos fuera del código (`.env`), `requirements.txt`
- [ ] Deploy con URL pública
- [ ] README con descripción, capturas e instrucciones

## 6. Hoja de ruta

| # | Etapa | Conceptos clave | Estado |
|---|---|---|---|
| 0 | Diagnóstico del proyecto propio y del profesor | Estructura de un proyecto Django, comparación | ✅ |
| 1 | **Preparación**: configurar Git, repo en GitHub, `.venv`, Django, `startproject`, `.gitignore`, `requirements.txt`, primer commit y push | Git (`init`, `add`, `commit`, `push`), entorno virtual, estructura de Django | ✅ |
| 2 | **Modelo `Post` bien diseñado** (`title`, `slug`, `content`, `author` → `User`, `status`, fechas) + usuario propio + migraciones + admin personalizado | `AbstractUser`, `AUTH_USER_MODEL`, `ForeignKey`, `TextChoices`, `Meta`, `save()`, migraciones, `ModelAdmin` | ✅ |
| 3 | **Lista y detalle** (solo publicados), URLs con slug | Vistas de función, QuerySets, `get_object_or_404`, `get_absolute_url` | ⬜ |
| 4 | **Templates y estilo**: `base.html`, navegación, Bootstrap, archivos estáticos | `extends`/`block`, filtros, `static` | ⬜ |
| 5 | **Autenticación**: login, logout, registro | `django.contrib.auth`, `UserCreationForm`, `request.user` | ⬜ |
| 6 | **Crear post** con `ModelForm` (autor = usuario logueado) + validaciones + mensajes | bound/unbound, `clean_<campo>`, `commit=False`, `messages` | ⬜ |
| 7 | **Editar y eliminar** con permisos | `instance=`, `@login_required`, borrar solo por POST, 403 | ⬜ |
| 8 | **Borradores**: página "Mis posts" | Filtrar por usuario y estado | ⬜ |
| 9 | **Búsqueda y paginación** | `forms.Form` por GET, `icontains`, `Paginator` | ⬜ |
| 10 | **Tests** | `TestCase`, `self.client`, `assertRedirects` | ⬜ |
| 11 | **Preparar para producción**: `.env`, `DEBUG`, `ALLOWED_HOSTS`, `collectstatic` | Configuración por entorno, seguridad básica | ⬜ |
| 12 | **Deploy** en PythonAnywhere | Servir una app Django real | ⬜ |
| 13 | **README final** con capturas y link | Presentar el proyecto | ⬜ |

**Extras opcionales** (después de la 13): categorías/etiquetas, comentarios, imágenes en los posts (media), likes, estadísticas, formulario de contacto, vistas basadas en clases (CBVs).

## 7. Estado actual

- **Última etapa completada:** 2 — Modelo `Post`, usuario propio y admin
- **Próximo paso:** Etapa 3 — Lista y detalle (solo publicados), URLs con slug
- **Pendientes / dudas abiertas:** —

---

## 8. Registro de etapas

> Plantilla para cada etapa nueva (copiar y completar al cerrarla):
>
> ### Etapa N — Nombre (fecha)
> **Objetivo:**
> **Archivos creados/modificados:**
> **Qué aprendí:**
> **Cómo verificar que funciona:**
> **Errores que aparecieron y cómo los resolví:**
> **Commit(s):**
> **Dudas para repasar:**

### Etapa 0 — Diagnóstico (2026-10-13/14)

**Objetivo:** entender el proyecto propio, el del profesor y las diferencias entre ambos, y definir cómo seguir.

**Qué aprendí:**
- Mi proyecto anterior ya tenía lista, detalle (`get_object_or_404` por `id`) y creación con `ModelForm` (patrón GET/POST + `csrf_token`).
- El proyecto del profesor agrega edición (`instance=`), borrado con confirmación por POST, slug generado en `save()`, herencia de templates, búsqueda por GET, `aggregate(Avg)`, `forms.Form` sin modelo, admin personalizado y tests.
- Agregar un campo `unique` (como el slug) a una tabla con datos existentes requiere cuidado con las migraciones.
- Recorrido completo de una petición: URL → View → Form/Model → Template → respuesta (y el redirect después de un POST).

**Decisiones:** ver sección 3.

### Etapa 1 — Preparación (2026-10-15)

**Objetivo:** dejar lista la base del proyecto: Git, GitHub, entorno virtual, Django y `startproject`.

**Archivos creados/modificados:** `.gitignore`, `requirements.txt`, `manage.py`, `config/` (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`, `__init__.py`), `BITACORA.md`.

**Qué aprendí:**
- `git config --global` configura mi identidad una sola vez por PC; `user.email` igual al de GitHub para que me atribuya los commits.
- El `.gitignore` va antes del primer `git add`: evita que Git empiece a seguir archivos, pero no borra lo que ya está en el historial.
- El entorno virtual aísla los paquetes del proyecto; no se sube, se reconstruye con `pip install -r requirements.txt`.
- `startproject config .` — el punto evita la carpeta duplicada.
- `ROOT_URLCONF` en `settings.py` le dice a Django dónde está el `urls.py` principal.
- La página del cohete es una vista interna que Django muestra solo con `DEBUG = True` y sin rutas propias.
- `USE_TZ = True`: las fechas se guardan en UTC y se muestran según `TIME_ZONE`.
- Ciclo de Git: `status` → `add` (staging) → `commit` (foto en el historial) → `push` (subir a GitHub).

**Cómo verificar que funciona:** `python manage.py runserver` → cohete en http://127.0.0.1:8000/; `git status` no muestra `.venv/`, `__pycache__/` ni `db.sqlite3`; el repo en GitHub tiene los archivos.

**Errores que aparecieron y cómo los resolví:** ninguno. Nota: `Out-File` en Windows PowerShell guarda en UTF-8 con BOM (pip lo acepta).

**Commit(s):**
- `Inicializa proyecto Django con entorno, requirements y .gitignore`
- `Set TIME_ZONE to America/Argentina/Buenos_Aires`
- `Add project log (BITACORA.md) and close stage 1`

**Dudas para repasar:** —

### Etapa 2 — Modelo Post, usuario propio y admin (2026-10-15/16)

**Objetivo:** diseñar el modelo de datos del blog (usuarios y posts), crear las tablas con migraciones y gestionar los posts desde el admin.

**Archivos creados/modificados:** `accounts/` (`models.py`, `admin.py`, `migrations/0001_initial.py`), `blog/` (`models.py`, `admin.py`, `migrations/0001_initial.py`), `config/settings.py` (`INSTALLED_APPS`, `AUTH_USER_MODEL`), `requirements.txt` (sin BOM).

**Qué aprendí:**
- Proyecto vs. app: `config` es la configuración; cada app tiene una responsabilidad (`accounts` usuarios, `blog` posts). Toda app se registra en `INSTALLED_APPS`.
- `INSTALLED_APPS` son rutas de importación: un nombre mal escrito da `ModuleNotFoundError` (error de Python).
- `AUTH_USER_MODEL = "accounts.User"` (formato `app.Modelo`) se define antes del primer `migrate`. `AbstractUser` es un molde sin tabla propia.
- Para referirse al usuario: `settings.AUTH_USER_MODEL` en modelos, `get_user_model()` en el resto del código. Nunca importar `django.contrib.auth.models.User`.
- `makemigrations` escribe el plan (archivo versionado en Git); `migrate` lo ejecuta sobre la base. Solo los cambios de estructura (campos) generan migraciones; los métodos no.
- `sqlmigrate` muestra el SQL real: tabla `blog_post`, columna `author_id` → `accounts_user`, `UNIQUE` en el slug.
- `unique` y `max_length` los hace cumplir la base; `choices` y `blank` los valida Django (forms/admin). Un `create()` directo puede guardar un status inválido.
- `ForeignKey` se recorre en dos sentidos: `post.author` y `user.posts.all()` (gracias a `related_name`; sin él sería `post_set`).
- Sobrescribir `save()`: siempre `*args, **kwargs` y siempre llamar a `super().save()`, o no se guarda nada.
- `get_<campo>_display()` lo crea Django para campos con `choices`.
- En Python la sangría define qué está dentro de qué (4 espacios por nivel).
- `ModelAdmin`: `list_display`, `list_filter`, `search_fields`, `date_hierarchy`, `readonly_fields`.

**Cómo verificar que funciona:** `python manage.py check` sin errores; `makemigrations` → "No changes detected"; en `/admin/`: Users dentro de Accounts y Posts dentro de Blog; un post creado en el admin genera su slug y el slug no cambia al editar el título.

**Errores que aparecieron y cómo los resolví:**
- `requirements.txt` aparecía como modificado: `git diff` mostró que era solo el BOM quitado → commit aparte.
- El `:` después de `git diff` es el paginador de Git → se sale con `q`.

**Commit(s):**
- `Save requirements.txt as UTF-8 without BOM`
- `Add blog and accounts apps with custom user model`
- `Add Post model with author, status and timestamps`
- `Generate unique slug from title on save`
- `Add Post admin with filters, search and read-only slug`
- `Update project log for stage 2`

**Dudas para repasar:** —

## 9. Conceptos aprendidos (glosario personal)

> Completar con mis propias palabras a medida que avancemos.

| Concepto | Qué es / para qué sirve | Etapa |
|---|---|---|
| `ModelForm` | Formulario que toma sus campos de un modelo y puede guardarlo con `.save()` | previa |
| `get_object_or_404` | Busca un objeto y, si no existe, responde 404 en vez de romper | previa |
| `{% csrf_token %}` | Protección que Django exige en formularios POST | previa |
| Entorno virtual (`.venv`) | Python aislado con los paquetes de este proyecto | 1 |
| `requirements.txt` | Receta de dependencias para reconstruir el entorno | 1 |
| `.gitignore` | Lista de archivos que Git no debe seguir | 1 |
| Staging area | Zona intermedia donde preparo qué entra en el próximo commit (`git add`) | 1 |
| `origin` | Apodo convencional del repo remoto en GitHub | 1 |
| `manage.py` | Script para ejecutar comandos de Django en este proyecto | 1 |
| `USE_TZ` / `TIME_ZONE` | Guardar fechas en UTC y mostrarlas en hora local | 1 |
| App | Módulo con una responsabilidad concreta dentro del proyecto | 2 |
| `AbstractUser` / `AUTH_USER_MODEL` | Molde del usuario de Django / setting que indica qué modelo de usuario usa el proyecto | 2 |
| Migración | Archivo que describe un cambio en la estructura de la base (`makemigrations` lo crea, `migrate` lo aplica) | 2 |
| `ForeignKey` | Relación muchos-a-uno; en la base es una columna `<campo>_id` | 2 |
| `related_name` | Nombre de la relación inversa (`user.posts`) | 2 |
| `TextChoices` | Opciones fijas para un campo: valor guardado + texto visible | 2 |
| `super().save()` | Llama al `save()` original para que el objeto se guarde de verdad | 2 |
| `ModelAdmin` | Clase que configura cómo se ve un modelo en el admin | 2 |
