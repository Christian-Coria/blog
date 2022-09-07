ispc_BlogEstudiantil
ISPC ESTUDIANTIL
                                                  Plataforma Estudiantil ISPC
!Deploy <<<<<<< HEAD

=======

57fe6603c2117e77f4589d92d43b8e8102468b1a

==> Casos de Prueba <== <- a completar!

Este proyecto tiene como objetivo el apoyo al estudiantado en lo concerniente a la Tecnicatura de Innovcion con Tecnologias 4.0 del Instituto Politectico Cordoba.
Cosas que puedes hacer::

==> Video de Funcionalidades <== <- a completar!

Ingresar a los siguientes servicios previo Login:
Crear, leer, actualizar y eliminar Contenido conserniente a temas relacionados con la Carrera (Publicacion de articulos).
Crear, leer, actualizar y eliminar Apuntes da cada materia.
Acceder al calendario academico.
Una seccion de apoyo donde podras:
Crear, leer, actualizar y eliminar Material complementario (videos, cursos afines...etc).
Un buscador general
Enlaces de comunicacion para el profesorado.
Enlaces de comunicacion para el profesorado.
Area para Chat entre Usuarios :
-- Nota: Es necesario previamente acceder al administrador con el SuperUsuario y generar la salas de Chat.

Area para agendar Recordatorios de Tareas:
Podras agendar o eliminar notas de recordatorio.
Instalar
Para instalar este software necesitas:

Comprobar la versión de Python
Este proyecto se escribió con Python 3.10.5, por lo que le sugiero que pruebe con esta versión o superior para no tener problemas de compatibilidad.

Cómo verifico mi versión de python,

en sistemas *nix:

> python --version
> Python 3.8.0
en windows:

c:\> py --version
c:\> Python 3.8.0
Crea tu Ambiente Virtual
---bash pip install virtualenv

virtualenv env .\env\Scripts\activate

Instalar dependencias
Para instalar las dependencias, debe ejecutar pip install, asegúrese de estar en la carpeta del proyecto y pueda ver el 'requirements.txt' archivo cuando haga 'ls' o 'dir':

> pip install -r requirements.txt
Este último instalara los requerimientos necesarios en la terminal..

algunos sistemas operativos requieren el uso de pip3 o pip

Configuración de la aplicación Django
Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django.

Migraciones
Initialize the database :

> python mananage.py migrate

py manage.py collectstatic

windows:
```bash
c:\> py mananage.py migrate
Ejecutar el servidor de prueba
> python mananage.py runserver
windows:

c:\> py mananage.py runserver
Go to localhost:8000/

para tener acceso a la aplicación.

'Aclaracion: es necesario contar con internet par la carga de imagenes de templates.

Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.