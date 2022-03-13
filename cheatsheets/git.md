# github cheatsheet
atajos y pequenos tutoriales de git

## Subir repositorio
1. Primero creamos un nuevo repositorio usando github
2. `git init` Iniciamos repositorio en nuetro proyecto local 
3. `git add -A` Agrega archivos al staging area
4. `git commit -m "comentario"`Agrega los archivos al repositorio local
5. `git remote add origin http://github/repo-que-creamos` Nos conecta con el repositorio remoto
6. `git push -u origin master` Empuja los commmit de la rama local a la remota (github)

## Agregar nuevo commit al proyecto
1. `git add -A` Agrega archivos al staging area
2. `git commit -m "comentario` Agrega archivos al repo local
3. `git push -u origin master` Empuja los archivos de la rama local a la remota (github)

## Sincronizar repo local y remoto
Antes de agregar nuevos commits a tus repos recuerda que estos deben estar sincronizados el remoto y el local

1. `git fetch origin` Descarga los cambios remotos al local
2. `git pull origin master` Fuciona los cambios descargados, parecido a un **merge**

## Error al hacer pull
a veces puedes tener errores de conflicto y no puedes hacer pull, recibiendo este errror    
**error: Pulling is not possible because you have unmerged files**

To solve
flushes out local conflicting files, requiring not only a merge-head or HEAD reset, but also a -hard reset. The local workspace will not be flushed without the following hard. It just overwhelms the stage. 
  
```
git reset --hard FETCH_HEAD
```
