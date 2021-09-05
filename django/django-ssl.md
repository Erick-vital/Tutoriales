## Agregar certificado ssl a proyecto django
usaremos certbot y para el servidor apache2

### 1. configurar archivo sites-available/django.conf
Entramos al archivo de configuracion de apache2 **/etc/apache2/sites-available/django.conf**, el archivo de configracion django.conf 
puede tener un nombre algo diferente.   
Primero descomentamos la linea **ServerName example** y agregamos nuestro nombre de dominio y ahora comentamos momentaniamente las lineas con **WSGIS**
```
#WSGIScriptAlias
#WSGIDaemonProcess
#WSGIProcessGroup

