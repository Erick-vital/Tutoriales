## Deploy de django 
Un deploy o deployment es cuando publicamos nuestra pagina web en un servidor para que esta este en el internet, ahora 
veremos como hacer un deploy de nuestra pagina de django 

### 1. Crear un servidor y conectarnos mediante **ssh**
En este caso estaremos usando un servidor creado en linode al cual conectaremos mediante ssh con la ip del servidor 
  ejemplos:
  `ssh root@ip-del-servidor`
  
Una vez dentro debemos asegurarnos de actualizar nuestro linux con los comandos **apt update** y **apt upgrade**

### 2. Cambiar el hostname y agregar usuarios nuevos
lo primero que haremos sera cambiar el hostname o **nombre del equipo** con el siguietne comando 
```
hostnamectl set-hostname <nombre que asignaremos>
```
podemos verificar que el hostname este correcto con el comando:
`hostname`

Ahora haremos lo mismo modificando el archivo **hosts** que se encuentra en /etc/hosts
`vim /etc/hosts`
y debajo de localhost agregamos la ip del servidor y nuestro hostname que acabamos de asignar

```
127.0.0.1  localhost
<ip-del-servidor> <nombre-del-host>
```

Ahora crearemos un nuevo usuario con el comando
`adduser <nombre de usuario>`
y agregamos al usuario creado al grupo de sudo
`adduser <nombre de usuario> sudo` 

`cat /etc/passwd` para ver todos los usuarios

bien ahora salimos del ssh y volvemos a entrar como el usuario que acabamos de crear
`ssh <usuario>@<ip>`

### 3. Agregar llaves ssh 
Agregaremos las llaves [ssh](https://github.com/Erick-vital/Tutoriales/blob/master/redes/protocolos/ssh.md) para poder entrar sin contrasena y de forma mas segura al servidor, en nuestra maquina local crearemos el directorio **.ssh** si es que no existe ya y hacemos lo mismo en nuestra maquina remota(el servidor)

En nuestra maquina local ejecutamos el siguiente comando `ssh-keygen -b 4096` lo que creare dos llaves una publica y otra privada, la llave privada nos servira para desencriptar la llave publica, por lo que solo compartiremos la publica

Ahora enviaremos la llave privada al servidor con el siguiente comando `scp ~/.ssh/id_rsa.pub <usuario>@<ip>:~/.ssh`, Ahora solo debemos cambiar los permisos del directorio **.ssh** de nuestro servidor `sudo chmod 700 ~/.ssh/` y hacemos lo mismo con la llave publica que acabamos de enviar `sudo chmod 600 ~/.ssh/*`

ya podemos entrar al servidor desdes nuestra maquina local sin contrasena, puedes intentar reiniciar la terminal si tienens problemas para entrar 

Por ultimo es aconsejable desactivar poder logearte desde root, esto lo qutas en el archvo de configuracion `/etc/ssh/ssh_config`, debes desactivar la opcion `permitrootlogin` si esque no esta desactivada ya 

### 4. Instalar firewall en nuestro servidor
Como ultima medida de seguridad vamos a instalar y configurar de forma sencilla un firewall.

Instalaremos el firewall 'ufw' `sudo apt install ufw`

Permitiremos y negaremos las siguientes conexiones `sudo ufw default allow outgoing` y `sudo ufw default deny incoming`

Permitimos la conexion ssh `sudo ufw allow ssh` y usaremos el puerto 8000 para probar nuestra web antes de permitir conexiones htttp `sudo ufw allow 8000`.

Ahora solo queda prender el firewall `sudo ufw enable` y podemos corroborar con ` sudo ufw status`

### 5. Clonar repositorio y crear entorno virtual python
Desde github clonaremos nuestro repositorio a nuestra maquina remota y crearemos un nuevo entorno virtual python.

`git clone <http//:repositorio>`.

Para el entorno Instalamos primero **pip** `sudo apt install python3-pip` y el entorno virtual `pip install virtualenv` ahora creamos el entorno dentro de nuestro repositorio `virtualenv --python=/usr/bin/python3 venv`

Ahora solo queda instalar los modulos python que usaremos en este proyecto el cual esta contenido en el file requisitos.txt que creamos previamente usando **pip freeze** > requisitos, ya dentro de nuestro entorno virtual instalamos los requisitos con **pip** `pip install -r requisitos.txt` 

Ya todo deberia estar listo, si tuviste problema en la instalacion de requisitos borra la siguiente lista del file, 'pkg-resources==0.0.0'

### 6. Agregar ip a settings y archivos staticos
Ahora haremos unos pequenos cambios al archivo **settings.py** y recolectaremos los archivos static en una nueva carpeta static para produccion, bien ahora entraremos al archivo **settings.py** y en la constante **ALLOWED_HOSTS=[]** agregaremos la ip de nuestro server en forma de string
```
# Recuerda agregar tambien tu dominio si tienes uno
# esta ip solo es un ejemplo
ALLOWED_HOSTS = ['www.mydominio.com', '12.123.12.5']
```

Ahora crearemos una nueva constante
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
no te olvides de importart el modulo **os** y por convencion crear la constante donded esta la otra constante static, bien ahora guardamos cambios

Por ultimo ya podemos ejecutar el comando `python3 manage.py collectstatic` el cual recolectara los archivos staticos y creara carpeta static de produccion.

Ahora ya podemos probar la web con el puerto que abrimos el 8000 `python3 manage.py runserver 0.0.0.0:8000` para probar la web usamos la ip del servidor y el puerto 8000 en un navegador, ejemplo `124.14.2.16:8000`, obviamente cambiando la ip por la nuestra

### 7. Apache2
Toca instalar el servidor **apache2** en nuestra maquina remota el cual nos servira para mantener nuestra pagina web encendida sin nesecidad de hace "python3 manage.py runserver" cada vez para prender nuestra web

Instala apache2 `sudo apt install apache2`, instala modulo de apache **wsgi** `sudo apt install libapache2-mod-wsgi-py3` este nos permite interactuar python con apache2
