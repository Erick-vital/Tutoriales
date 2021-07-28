# Docker
algunos comandos y pequenos pero importantes tutoriales sobre docker, para mas informacion sobre los conceptops de que es deocker visita [aqui](https://github.com/Erick-vital/Tutoriales/tree/master/linux/docker_conceptops)

## Instalar y usar docker en Arch o Manjaro
Este tutorial esta basado en este de [aqui](https://linuxhint.com/install_start_docker_arch_linux/)
primero actualizamos nuestro sistema de reposositorios
```
sudo pacman -Syu
```
Activamos el **loop module** con lo siguientes comando
```
sudo tee /etc/modules-load.d/loop.conf <<< "loop"
```
```
modprobe loop
```
### Instalacion repo oficial
el repo de docker lo podemos encontrar en el gestor de paquetes oficial de arch. Por lo que lo podemos instalar con pacman
```
sudo pacman -S docker
```
### Configurar docker
Para activar docker debemos ejecutar los siguientes comandos
```
sudo systemctl start docker.service
sudo systemctl enable docker.service
```
Verifica que docker este prendido
```
sudo docker info
```

### Docker sin usar sudo
por default docker solo puede correr como sudo por lo que tenemos que agregar nuestro usuario el grupo de docker para poderlo ejecutar sin usar **sudo** cada vez

Crea grupo de docker si es que no existe ya
```
sudo groupadd docker
```

Agrega nuestro usuario al grupo de docker 
```
sudo usermod -aG docker <username>
```

Recuerda que para que los cambios surtan efectos tienes que reiniciar la terminal o el computador 


