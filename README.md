# Headroom — Blog de producción musical y audio

Blog web desarrollado con **Django** sobre producción musical, grabación y sonido. Los usuarios pueden registrarse, escribir posts con imagen, guardarlos como borradores o publicarlos, y gestionarlos desde su perfil.

Proyecto final de Django de la **Diplomatura de Coderhouse**. La interfaz del blog está en inglés.

---

## Funcionalidades

**Posts**
- Listado de posts publicados, del más nuevo al más viejo.
- Detalle de cada post con URL amigable (slug), por ejemplo `/how-to-eq-vocals/`.
- Crear, editar y eliminar posts desde la interfaz web (no solo desde el admin).
- Confirmación antes de eliminar un post.
- Imagen opcional en cada post: se muestra en el listado y en el detalle, y la página funciona igual si un post no tiene imagen.
- Estados **borrador** y **publicado**: los borradores solo los ve su autor.
- Búsqueda por título o contenido, con aviso cuando no hay resultados.
- Validaciones en los formularios (por ejemplo, título de al menos 5 caracteres).
- Mensajes de confirmación después de crear, editar o eliminar.

**Usuarios**
- Registro, inicio y cierre de sesión.
- Perfil con los datos del usuario y todos sus posts, separados en borradores y publicados.
- Edición del perfil (nombre, apellido y email).
- La navegación cambia según el visitante sea anónimo o esté autenticado.

**Permisos**
- Crear, editar y eliminar posts, y ver o editar el perfil, requieren sesión iniciada (`@login_required` en las vistas).
- Cada usuario solo puede editar o eliminar **sus propios** posts.

**Administración**
- Panel de administración de Django con filtros y búsqueda de posts y usuarios.

---

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje |
| Django 6.1 | Framework web |
| SQLite | Base de datos (desarrollo) |
| Bootstrap 5.3 (CDN) | Diseño responsive |
| Pillow | Manejo de imágenes (`ImageField`) |
| python-decouple | Variables de entorno (`.env`) |
| Git y GitHub | Control de versiones |

---

## Instalación y ejecución local

### Requisitos previos

- Python 3.12 o superior (desarrollado con Python 3.14).
- Git.

### 1. Clonar el repositorio

```bash
git clone https://github.com/lucascauhepe-spec/django-blog-audio.git
cd django-blog-audio
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> Si PowerShell no permite ejecutar el script de activación, correr una vez
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y volver a intentar.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Cuando el entorno está activo, la terminal muestra `(.venv)` al principio de la línea.

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

El proyecto lee su configuración de un archivo `.env`, que no está en el repositorio. Hay que crearlo copiando la plantilla `.env.example`:

**Windows:**

```powershell
copy .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

Con los valores de la plantilla el proyecto funciona en local. Para usar una clave propia, generarla con:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

y reemplazar el valor de `SECRET_KEY` en el archivo `.env`.

| Variable | Descripción | Valor para desarrollo |
|---|---|---|
| `SECRET_KEY` | Clave secreta de Django | Cualquier texto (o una clave generada) |
| `DEBUG` | Modo de depuración | `True` |
| `ALLOWED_HOSTS` | Dominios permitidos, separados por comas | `localhost,127.0.0.1` |

> Con `DEBUG=True`, Django sirve los archivos estáticos y las imágenes subidas. Con `DEBUG=False`, el sitio se vería sin estilos ni imágenes al usar `runserver`.

### 5. Crear la base de datos

```bash
python manage.py migrate
```

### 6. Crear un superusuario (para el panel de administración)

```bash
python manage.py createsuperuser
```

Pide nombre de usuario, email (opcional) y contraseña.

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

- Blog: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

---

## Probar el proyecto desde cero

El repositorio **no incluye** la base de datos (`db.sqlite3`) ni las imágenes subidas (`media/`): son datos locales, no código. Después de seguir la instalación, el blog arranca vacío. Para probar todas las funcionalidades:

1. **Registrarse** desde *Sign up* (el usuario queda logueado).
2. **Crear un post publicado con imagen** desde *New post*. Aparece en el listado y en su detalle.
3. **Crear un post sin imagen**: el listado y el detalle se ven correctamente.
4. **Crear un borrador** (status *Draft*): no aparece en el listado, pero sí en el perfil (*Hi, usuario*).
5. **Editar y eliminar** un post desde los botones *Edit* y *Delete* de su detalle.
6. **Buscar** una palabra del título o del contenido con la caja de búsqueda del listado.
7. **Editar el perfil** desde *Edit profile*.
8. **Probar los permisos:**
   - Cerrar sesión e intentar entrar a `/new/` o `/accounts/profile/`: redirige al login.
   - Con otro usuario, intentar editar un post ajeno escribiendo `/<slug>/edit/` en la URL: responde 404.

---

## Rutas principales

| URL | Descripción | Requiere sesión |
|---|---|---|
| `/` | Listado de posts publicados y búsqueda (`/?q=...`) | No |
| `/<slug>/` | Detalle de un post | No (borradores: solo su autor) |
| `/new/` | Crear un post | Sí |
| `/<slug>/edit/` | Editar un post | Sí, y ser el autor |
| `/<slug>/delete/` | Eliminar un post (con confirmación) | Sí, y ser el autor |
| `/accounts/signup/` | Registro | No |
| `/accounts/login/` | Inicio de sesión | No |
| `/accounts/logout/` | Cierre de sesión (POST) | Sí |
| `/accounts/profile/` | Perfil del usuario con sus posts y borradores | Sí |
| `/accounts/profile/edit/` | Editar el perfil | Sí |
| `/admin/` | Panel de administración | Sí (staff) |

---

## Estructura del proyecto

```
django-blog-audio/
├── accounts/               # App de usuarios: modelo User propio, registro, perfil
│   ├── templates/
│   │   ├── accounts/       # profile.html, profile_form.html
│   │   └── registration/   # login.html, signup.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── blog/                   # App de posts: modelo Post, CRUD, búsqueda
│   ├── templates/blog/     # post_list, post_detail, post_form, post_confirm_delete
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── config/                 # Configuración del proyecto (settings.py, urls.py)
├── static/css/             # Estilos propios
├── templates/              # base.html (estructura común de todas las páginas)
├── .env.example            # Plantilla de variables de entorno
├── .gitignore
├── BITACORA.md             # Registro del desarrollo, etapa por etapa
├── manage.py
├── README.md
└── requirements.txt
```

---

## Autor

**Lucas Cauhepé**
GitHub: [lucascauhepe-spec](https://github.com/lucascauhepe-spec)
