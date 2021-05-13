
# Tarea4-Arquitectura_Sistema
Tecnología y atributos de calidad - Django

# Autores :man:  :man:  :girl:

- Juan Ortiz -1151498
- Jhonatan Calderon -1151624
- Angela Acevedo -1151628

# Requisitos:clipboard:
- 	S

# Construido con :hammer:
+ Nube Amazon, aws
+ Python3
+ Django
+ SQLite3


# Instrucciones:arrow_left:

## Despliegue Nube aws:

### Creación de EC2
+ Crear instancia Amazon EC2 con Ubuntu server 20.04 LTS
+ Agregar los grupos de seguridad HTTP y HTTPS en sus puertos por defecto
+ Agregar grupo de seguridad TCP personalizado en el puerto 8000
+ Descargar par de claves(formato .pem)
+ Crear una ip elástica y asociarla a la EC2 recién creada

### Conexión SSH (Método 1-Putty)
+ Con el programa Pyttygen cargamos la clave y generamos la clave privada que se descargará en una extensión .ppk
+ Con el programa Putty nos dirigimos a la parte de "Session" y en Host Name colocaremos la ip pública(elástica) de nuestra EC2
+ Seleccionamos el apartado "Conection", desplegamos el check-box de "SSH" y seleccionaremos "AUTH"
+ Cargamos la clave en el formato ppk que se convirtió anteriormente, damos clic en "Open" y clic en "si"
+ Escribiremos el usuario que para este caso es "ubuntu"
+ Y listo nos conectamos a nuestra EC2 por medio de Putty

### Conexión SSH (Método 2-Git Bash)
+ Seleccionamos nuestra EC2
+ En "Acciones" seleccionamos "Conectar"
+ Abrimos la consola de Git bash en la ruta donde tenemos guardada nuestra clave en formato .pem
+ Copiamos y pegamos en la consola de git Bash el comando `chmod 400 "nombre la clave sin comillas"` que nos aparece luego de seleccionar "Conectar" (Item3) en aws y damos Enter
+ Copiamos y pegamos en la consola de git Bash el comando `ssh -i "clave-aws-..." ubuntu@ec2...` que nos aparece en la sección de "Ejemplo" en la pagina de aws y damos Enter
+ Escribimos "yes" en la consola de git Bash
+ Y listo nos conectamos a nuestra EC2 por medio de git bash


### Instalación de paquetes y dependencias en la máquina virtual
+ 


## Proceso de descarga
   **1. Descargar el repositorio en el formato .zip disponible.**
   
   **2. Descomprimir el archivo**




