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
`hostnamectl set-hostname <nombre que asignaremos>`
podemos verificar que el hostname este correcto con el comando:
`hostname`

Ahora haremos lo mismo modificando el archivo **hosts** que se encuentra en /etc/hosts
`vim /etc/hots`
y debajo de localhost agregamos la ip del servidor y nuestro hostname que acabamos de asignar

`127.0.0.1  localhost
<ip-del-servidor> <nombre-del-host>`

Ahora crearemos un nuevo usuario con el comando
`adduser <nombre de usuario>`
y agregamos al usuario creado al grupo de sudo
`adduser <nombre de usuario> sudo` 

bien ahora salimos del ssh y volvemos a entrar como el usuario que acabamos de crear
`ssh <usuario>@<ip>`

### 3. Agregar llaves ssh 
Agregaremos las llaves [ssh](https://github.com/Erick-vital/Tutoriales/blob/master/redes/protocolos/ssh.md) para poder entrar sin contrasena y de forma mas segura al servidor, en nuestra maquina local crearemos el directorio **.ssh** si es que no existe ya y hacemos lo mismo en nuestra maquina remota(el servidor)

En nuestra maquina local ejecutamos el siguiente comando `ssh-keygen -b 4096` lo que creare dos llaves una publica y otra privada, la llave privada nos servira para desencriptar la llave publica, por lo que solo compartiremos la publica

Ahora enviaremos la llave privada al servidor con el siguiente comando `scp ~/.ssh/id_rsa.pub <usuario>@<ip>:~/.ssh`, Ahora solo debemos cambiar los permisos del directorio **.ssh** de nuestro servidor `sudo chmod 700 ~/.ssh/` y hacemos lo mismo con la llave publica que acabamos de enviar `sudo chmod 600 ~/.ssh/*`

ya podemos entrar al servidor desdes nuestra maquina local sin contrasena, puedes intentar reiniciar la terminal si tienens problemas para entrar 

Por ultimo es aconsejable desactivar poder logearte desde root, esto lo qutas en el archvo de configuracion `/etc/ssh/ssh_config`, debes desactivar la opcion `permitrootlogin` si esque no esta desactivada ya 
