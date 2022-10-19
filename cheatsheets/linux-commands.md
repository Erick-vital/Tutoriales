### Head
head es un comando que nos permite ver la 10 primeras lineas de un archivo

**10 lineas primeras de un archivo**    
`head archivo.txt`

**10 primeras de un comando ls**   
`head ls /lib/ | head`


**20 primeras de un comando ls**   
`head ls /lib/ | head -n 20

la contra de head es tail

### Ver usuarios en un sistema
Para listas los usuarios en un sistema podermos usar los siguientes comandos
```
cat /etc/passwd
```
o tambien
```
getent passwd
```


## WSL
pequeno truco para ver los archivos de wsl2 desde el explorador de archivos de windows
solo tienes que poner la siguiente ruta \\wsl$\ y recuerda de tener una instancia de wsl2 corriendo para poder
ver los archivos
