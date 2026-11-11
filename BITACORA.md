# 📓 Bitácora — Blog Django (proyecto de portfolio)

> **Para qué sirve este archivo:** es la memoria detallada del proyecto. Al terminar cada etapa se actualiza (estado actual + registro de la etapa) y se vuelve a subir al Proyecto de Claude. Así cualquier chat nuevo puede retomar exactamente desde donde quedamos.
>
> También vive dentro del repositorio, así que queda versionado con Git.

---

## 1. Objetivo

Construir **desde cero** un blog en Django con calidad de portfolio, publicado online y con su código en GitHub, **aprendiendo en el camino** cómo funciona cada parte. La meta principal no es solo tener la app, sino poder desarrollar con Django de forma autónoma.

Además, este proyecto es la **entrega final de Django de la Diplomatura (Coderhouse)**.

## 2. Entorno

| Elemento | Valor |
|---|---|
| Sistema operativo | Windows |
| Editor | VS Code |
| Python | Python 3.14.7 |
| Django | 6.1.2 |
| Control de versiones | Git (instalado) + GitHub (cuenta creada) |
| Base de datos | SQLite (desarrollo) |
| Repositorio | https://github.com/lucascauhepe-spec/django-blog-audio |
| Deploy previsto | PythonAnywhere (plan gratuito), después de la entrega |
| Entrega final Coderhouse | ~2026-12-01 (este proyecto es la entrega) |

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
| 2026-11-10 | Este proyecto es la **entrega final de Django de la Diplomatura (Coderhouse)** | Cubre casi todos los criterios; solo hay que sumar imágenes y perfil |
| 2026-11-10 | **Imágenes en los posts** y **perfil de usuario** pasan al núcleo | Son obligatorios en la consigna |
| 2026-11-10 | Variables de entorno con **`python-decouple`** | Es lo que espera la consigna |
| 2026-11-10 | Tests, paginación y deploy quedan **para después de la entrega** | No los pide la consigna; priorizar llegar a tiempo |
| 2026-11-10 | "Mis posts" (borradores) se integra en la página de **perfil** | Una sola etapa cubre las dos cosas |
| 2026-11-10 | Sin preguntas de repaso ni ejercicios entre pasos | Avanzar paso a paso; las dudas las planteo yo |
| 2026-11-10 | Rutas con namespace (`app_name = "blog"`) | Va a haber rutas de varias apps (`blog`, `accounts`); evita choques de nombres |
| 2026-11-10 | `select_related("author")` en la lista | Evita una consulta extra por post (problema N+1) |
| 2026-11-10 | Un borrador da 404 en el detalle público | Los borradores no existen para el público; el autor los verá desde su perfil |
| 2026-11-10 | `base.html` en `templates/` **a nivel proyecto** (`DIRS = [BASE_DIR / "templates"]`) | Lo comparten todas las apps (`blog`, `accounts`); no pertenece a ninguna |
| 2026-11-10 | CSS propio en `static/` **a nivel proyecto** (`STATICFILES_DIRS`) | Es el estilo de todo el sitio; la consigna pide estáticos en el repo |
| 2026-11-10 | Bootstrap 5.3.3 por CDN con **versión fija** en la URL | El sitio no cambia solo; mismo criterio que `requirements.txt` |
| 2026-11-10 | Título visible del blog: **Headroom** (en un solo lugar, `base.html`) | Concepto de audio (margen antes de saturar); se cambia en un segundo |
| 2026-11-10 | Rutas armadas con `BASE_DIR`, nunca absolutas | Funciona en cualquier PC o servidor; lo exige la consigna |
| 2026-11-11 | Login y logout con las vistas de Django (`LoginView`, `LogoutView`); registro con vista propia | No reescribir lo que Django ya resuelve de forma segura |
| 2026-11-11 | `SignUpForm` hereda de `UserCreationForm` con `model = accounts.User` y pide `username` + `email` | `UserCreationForm` está atado a `auth.User`, que en este proyecto está reemplazado |
| 2026-11-11 | Después de registrarse, el usuario queda logueado (`login()`) | Mejor experiencia: no tiene que volver a escribir sus datos |
| 2026-11-11 | Rutas de autenticación en `/accounts/` con namespace `accounts` | Convención de la documentación de Django |
| 2026-11-11 | `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` con nombres de rutas | Se ajustan solos si cambian las URLs |
| 2026-11-11 | Formularios con `{{ form }}` + reglas CSS propias (`.django-form`), sin `django-crispy-forms` | Sin dependencias extra; sirve para todos los formularios del sitio |

## 4. Proyectos de referencia

- **`django-blog lucas`** (proyecto anterior): `Post(titulo, autor, likes)`, lista, detalle por `id` y creación con `ModelForm`. Ahora sirve como apunte.
- **`blog_django`** (proyecto del profesor): CRUD completo con slug, `base.html`, búsqueda por GET (`BuscarForm`), estadísticas con `aggregate`, formulario de contacto (`forms.Form`), admin personalizado y 19 tests. Sirve como referencia de cómo resolver cada parte.

## 5. Alcance "portfolio"

Lo que debería tener la versión final (✱ = obligatorio para la entrega de Coderhouse):

- [x] ✱ Usuarios: registro, login y logout
- [ ] ✱ Posts con autor = `User` real; solo el autor puede editar o borrar los suyos
- [ ] ✱ CRUD completo desde la web, con validaciones y confirmación antes de borrar
- [ ] ✱ Imagen en los posts (el template no se rompe si falta)
- [ ] ✱ Perfil de usuario (con sus posts y borradores)
- [ ] ✱ Rutas protegidas con `@login_required`
- [ ] Mensajes de feedback ("Post published ✓")
- [x] Borradores y publicados; URLs con slug
- [ ] Búsqueda (opcional en la consigna) y paginación
- [x] Diseño prolijo y responsive (Bootstrap)
- [ ] Tests automáticos
- [ ] ✱ Secretos fuera del código (`.env` + `.env.example`), `requirements.txt` actualizado
- [ ] Deploy con URL pública
- [ ] ✱ README con descripción, tecnologías, instalación y autor

## 6. Hoja de ruta

| # | Etapa | Conceptos clave | Estado |
|---|---|---|---|
| 0 | Diagnóstico del proyecto propio y del profesor | Estructura de un proyecto Django, comparación | ✅ |
| 1 | **Preparación**: Git, GitHub, `.venv`, Django, `startproject`, `.gitignore`, `requirements.txt` | Git, entorno virtual, estructura de Django | ✅ |
| 2 | **Modelo `Post`** + usuario propio + migraciones + admin | `AbstractUser`, `AUTH_USER_MODEL`, `ForeignKey`, `TextChoices`, `save()`, migraciones, `ModelAdmin` | ✅ |
| 3 | **Lista y detalle** (solo publicados), URLs con slug | `include`, namespace, vistas de función, QuerySets, `get_object_or_404`, `get_absolute_url` | ✅ |
| 4 | **Templates y estilo**: `base.html`, navegación, Bootstrap, estáticos | `extends`/`block`, `DIRS`, `static`, `STATICFILES_DIRS` | ✅ |
| 5 | **Autenticación**: registro, login, logout | `django.contrib.auth`, `UserCreationForm`, `request.user` | ✅ |
| 6 | **Crear post** con `ModelForm` (autor = usuario logueado) | bound/unbound, `commit=False`, `messages`, `@login_required` | ⬜ |
| 7 | **Editar y eliminar** (solo el autor) | `instance=`, borrar solo por POST, 403 | ⬜ |
| 8 | **Imágenes en los posts** | `ImageField`, Pillow, `MEDIA_URL`/`MEDIA_ROOT`, `enctype` | ⬜ |
| 9 | **Perfil** con mis posts y borradores | Filtrar por usuario y estado, `related_name` | ⬜ |
| 10 | **Búsqueda** | `forms.Form` por GET, `Q`, `icontains` | ⬜ |
| 11 | **Configuración**: `python-decouple`, `.env`, `.env.example` | Configuración por entorno, secretos | ⬜ |
| 12 | **README** + revisión con el checklist de la consigna → **ENTREGA** | Documentar y presentar | ⬜ |

**Después de la entrega:** tests, paginación, deploy en PythonAnywhere, categorías, avatar de usuario, comentarios, CBVs.

## 7. Estado actual

- **Última etapa completada:** 5 — Autenticación
- **Próximo paso:** Etapa 6 — Crear post desde la web (`ModelForm`, `@login_required`, autor = usuario logueado)
- **Pendientes / dudas abiertas:** idioma del README (inglés con sección en español, o al revés) → se decide en la Etapa 12

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

### Etapa 3 — Lista y detalle (2026-11-10)

**Objetivo:** primeras páginas públicas: lista de posts publicados en `/` y detalle en `/<slug>/`.

**Archivos creados/modificados:** `config/urls.py`, `blog/urls.py` (nuevo), `blog/views.py`, `blog/templates/blog/post_list.html` y `post_detail.html` (nuevos), `blog/models.py` (`get_absolute_url`).

**Qué aprendí:**
- `config/urls.py` distribuye: `include("blog.urls")` delega en las rutas de la app.
- `path("<slug:slug>/", vista, name=...)`: el convertidor `slug` captura esa parte de la URL y la pasa a la vista como argumento con ese nombre.
- `app_name` da namespace a las rutas (`blog:post_detail`). Django prueba las rutas en orden: las fijas (`new/`) van antes que `<slug:slug>/`.
- Una vista recibe `request` y devuelve una respuesta; `render(request, template, contexto)` arma el HTML.
- Los QuerySets son perezosos: el SQL se ejecuta cuando se recorren (por ejemplo en el `{% for %}`).
- `select_related("author")` trae posts y autores en una sola consulta (evita N+1).
- `get_object_or_404` con varias condiciones: un borrador da 404 para el público.
- Templates en `app/templates/app/`: Django los busca por `APP_DIRS`; la subcarpeta repetida evita choques entre apps.
- `{{ }}` muestra valores, `{% %}` es lógica; `{% for %}`/`{% empty %}`; filtros `date` y `linebreaks`; el HTML se escapa solo.
- `{% url 'blog:post_detail' post.slug %}` y `reverse()` generan URLs a partir del nombre de la ruta.
- `get_absolute_url()`: cada objeto sabe su URL; el admin agrega "View on site". En templates los métodos sin argumentos se llaman sin paréntesis.

**Cómo verificar que funciona:** `/` lista solo publicados; clic → detalle en `/<slug>/`; el slug de un borrador o uno inexistente → 404; en el admin, "View on site" abre el post.

**Errores que aparecieron y cómo los resolví:** contraseña del superusuario olvidada → `python manage.py changepassword <usuario>` (las contraseñas se guardan como hash, no se pueden recuperar, solo reemplazar).

**Commit(s):**
- `Add post list and detail views with slug URLs`
- `Add get_absolute_url to Post and use it in templates`
- `Update project log for stage 3`

**Dudas para repasar:** —

### Etapa 4 — Templates y estilo (2026-11-10)

**Objetivo:** estructura común para todas las páginas (`base.html`), navegación, diseño responsive con Bootstrap y archivos estáticos propios.

**Archivos creados/modificados:** `config/settings.py` (`TEMPLATES["DIRS"]`, `STATICFILES_DIRS`), `templates/base.html` (nuevo), `blog/templates/blog/post_list.html` y `post_detail.html` (heredan de `base.html`), `static/css/styles.css` (nuevo).

**Qué aprendí:**
- Herencia de templates: `base.html` define huecos con `{% block %}`; los hijos usan `{% extends "base.html" %}` (siempre la primera etiqueta) y rellenan esos bloques. En un hijo, todo lo que está fuera de un bloque se ignora.
- `DIRS = [BASE_DIR / "templates"]` agrega una carpeta de templates a nivel proyecto; `APP_DIRS` sigue buscando dentro de cada app. Django busca primero en `DIRS`.
- `BASE_DIR` es la raíz del proyecto calculada desde `settings.py`: las rutas se arman con `/` y nunca son absolutas.
- Estáticos = archivos del sitio que se entregan tal cual (CSS, JS, imágenes del diseño). Media = archivos que suben los usuarios (Etapa 8).
- `STATIC_URL` es el prefijo de la URL; `STATICFILES_DIRS` agrega carpetas donde buscar. Con `DEBUG = True`, `runserver` los sirve solo.
- `{% load static %}` se pone en cada template que use `{% static %}` (no se hereda). `{% static 'css/styles.css' %}` genera la URL, igual que `{% url %}` para rutas.
- El CSS propio va después del de Bootstrap para poder pisarlo.
- Bootstrap: `viewport` para el celular, `container`, utilidades de espaciado (`py-4`, `mb-3`, `ms-auto`), `navbar-expand-md` + JS para el menú ☰, tarjetas (`card`).
- Filtros y tags nuevos: `truncatewords`, `{% now "Y" %}`.

**Cómo verificar que funciona:** `/` muestra la barra de navegación, las tarjetas y el pie; la pestaña dice "Posts · Headroom"; en vista de celular (F12 → `Ctrl+Shift+M`) el menú se colapsa en ☰; `/static/css/styles.css` muestra el CSS; las tarjetas tienen sombra al pasar el mouse.

**Errores que aparecieron y cómo los resolví:** ninguno. Nota: si el CSS no cambia, recargar con `Ctrl+F5` (caché del navegador).

**Commit(s):**
- `Add base template with Bootstrap layout and navigation`
- `Add static files setup with custom stylesheet`
- `Update project log for stage 4`

**Dudas para repasar:** —

### Etapa 5 — Autenticación: registro, login y logout (2026-11-11)

**Objetivo:** que los visitantes puedan registrarse, iniciar y cerrar sesión, y que el sitio distinga entre usuario anónimo y autenticado.

**Archivos creados/modificados:** `accounts/urls.py` (nuevo), `accounts/forms.py` (nuevo), `accounts/views.py`, `accounts/templates/registration/login.html` y `signup.html` (nuevos), `config/urls.py`, `config/settings.py` (`LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`), `templates/base.html` (navegación), `static/css/styles.css` (formularios).

**Qué aprendí:**
- `django.contrib.auth` trae `LoginView` y `LogoutView`; son vistas basadas en clases y se conectan con `.as_view()` (los argumentos de `as_view()` las configuran, por ejemplo `redirect_authenticated_user=True`).
- `LoginView` busca el template `registration/login.html` y le pasa `form` y `next`.
- Desde Django 5, el logout **solo acepta POST**: en la navegación es un formulario con `{% csrf_token %}`, no un link (un GET no debería cambiar nada en el servidor).
- `request.user` existe en cada petición: es mi `User` si está logueado o un `AnonymousUser` si no. En templates está como `{{ user }}` gracias a un context processor. Se pregunta con `user.is_authenticated`.
- Ocultar un link en el template no protege nada; la protección va en la vista.
- `UserCreationForm` está atado a `auth.User`: con un usuario propio se hereda y se cambia `Meta.model` (`class Meta(UserCreationForm.Meta)`).
- Patrón de formulario: GET → form vacío (unbound); POST → form con `request.POST` (bound) → `is_valid()` → `save()` + redirect; si es inválido, se vuelve a mostrar el mismo form con los errores.
- Post/Redirect/Get: después de un POST exitoso siempre redirect, para que recargar la página no reenvíe el formulario.
- `login(request, user)` crea la sesión (tabla `django_session` + cookie en el navegador).
- `{% csrf_token %}` es obligatorio en todo formulario POST; sin él, Django responde 403.
- Las contraseñas viajan por POST y se guardan como hash; un usuario registrado no es staff, así que no entra al admin.
- El mensaje de login fallido es genérico a propósito: no revela qué usuarios existen.
- Grilla de Bootstrap: `row`, `col-md-6`, `justify-content-center`.

**Cómo verificar que funciona:** como anónimo, la barra muestra "Log in" y "Sign up"; el registro con errores muestra los mensajes y conserva los datos; el registro válido redirige a `/` ya logueado ("Hi, <usuario>"); logueado, `/accounts/login/` y `/accounts/signup/` redirigen a `/`; "Log out" cierra la sesión; el usuario nuevo aparece en el admin sin staff status.

**Errores que aparecieron y cómo los resolví:** ninguno.

**Commit(s):**
- `Add login and logout with Django auth views`
- `Add sign up view with custom user creation form`
- `Update project log for stage 5`

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
| `include()` | Delega un grupo de rutas en el `urls.py` de una app | 3 |
| Convertidor de ruta | `<slug:slug>`: captura una parte de la URL con un formato y la pasa a la vista | 3 |
| Namespace (`app_name`) | Prefijo para los nombres de rutas de una app (`blog:post_list`) | 3 |
| Vista | Función que recibe un `request` y devuelve una respuesta | 3 |
| QuerySet perezoso | La consulta se arma pero no se ejecuta hasta que se usan los resultados | 3 |
| `select_related` | Trae objetos relacionados por `ForeignKey` en la misma consulta (JOIN) | 3 |
| `render` / contexto | Carga un template, le pasa un diccionario de variables y devuelve el HTML | 3 |
| Filtro de template | Transforma un valor al mostrarlo (`date`, `linebreaks`) | 3 |
| `reverse()` / `{% url %}` | Generan una URL a partir del nombre de la ruta | 3 |
| `get_absolute_url()` | Método convencional que devuelve la URL de un objeto | 3 |
| Herencia de templates | `base.html` con `{% block %}` + hijos con `{% extends %}`: la estructura común se escribe una sola vez | 4 |
| `DIRS` / `BASE_DIR` | Carpetas extra de templates / raíz del proyecto para armar rutas sin escribirlas a mano | 4 |
| Archivos estáticos | CSS, JS e imágenes del diseño que se entregan tal cual (`STATIC_URL`, `STATICFILES_DIRS`) | 4 |
| `{% load static %}` / `{% static %}` | Habilita el tag en el template / genera la URL de un archivo estático | 4 |
| Viewport / responsive | La meta `viewport` hace que el sitio se adapte al ancho del celular | 4 |
| CDN | Servidor externo desde donde el navegador descarga librerías como Bootstrap | 4 |
| `request.user` / `AnonymousUser` | El usuario de cada petición: el real si está logueado, uno anónimo si no | 5 |
| `is_authenticated` | Forma correcta de preguntar si alguien inició sesión | 5 |
| Sesión | Registro en el servidor + cookie en el navegador que mantiene al usuario logueado entre peticiones | 5 |
| Vista basada en clase (CBV) / `.as_view()` | Vista escrita como clase (como `LoginView`); `.as_view()` la conecta a una ruta | 5 |
| Form bound / unbound | Con datos (`Form(request.POST)`) o vacío (`Form()`) | 5 |
| `is_valid()` / `cleaned_data` | Corre las validaciones / datos ya validados y convertidos | 5 |
| Post/Redirect/Get | Después de un POST exitoso, redirigir para que recargar no reenvíe el formulario | 5 |
| CSRF | Ataque que envía formularios desde otro sitio; `{% csrf_token %}` lo bloquea | 5 |
