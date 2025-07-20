# Git

Git es un sistema de control de versiones distribuido ampliamente utilizado para la gestión de código fuente. Está diseñado para manejar desde proyectos pequeños hasta muy grandes con rapidez y eficiencia. Git es fácil de aprender y tiene un tamaño reducido con un rendimiento muy rápido.

## Instalación

Para instalar Git, visita el [sitio web de Git](https://git-scm.com) y descarga el instalador para tu sistema operativo. Después de descargarlo, ejecútalo y sigue las instrucciones de instalación.

## Configuración

Después de instalar Git, debes configurar tu nombre de usuario y correo electrónico. Abre la terminal y ejecuta los siguientes comandos:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "Tu Correo"
```

Para verificar tu configuración, ejecuta:

```bash
git config --global --list
```

## Uso básico

Para crear un nuevo repositorio Git, navega al directorio del proyecto y ejecuta:

```bash
git init
```

Para agregar archivos al área de preparación (staging), ejecuta:

```bash
git add .
```

Para guardar los cambios (commit), ejecuta:

```bash
git commit -m "Primer commit"
```

Para enviar los cambios a un repositorio remoto, ejecuta:

```bash
git push origin master
```

Para obtener cambios de un repositorio remoto, ejecuta:

```bash
git pull
```

Para clonar un repositorio remoto, ejecuta:

```bash
git clone <url_del_repositorio>
```

Para crear una nueva rama, ejecuta:

```bash
git checkout -b nueva_rama
```

Para cambiar a una rama existente, ejecuta:

```bash
git checkout rama_existente
```
