from django.db import models

# Create your models here.
class Alumno(models.Model):
	Codigo = models.AutoField(primary_key=True)
	Dni = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=50)
	Apellido = models.CharField(max_length=50)
	FechaNacimiento = models.DateField()
	Generos=[('F','Femenino'),('M','Masculino')]
	Genero = models.CharField(max_length=1,choices=Generos,default='F')

	def NombreCompleto(self):
		cadena = "{0} {1}"
		return cadena.format(self.Nombre,self.Apellido)

	def __str__(self):
		return self.NombreCompleto()


class Curso(models.Model):
	id = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=50)
	Creditos = models.PositiveSmallIntegerField()
	Estado = models.BooleanField(default=True)

	def InformacionCurso(self):
		return "{0} ({1})".format(self.Nombre,self.Creditos)

	def __str__(self):
		return self.InformacionCurso()
		
class Matricula(models.Model):

	Alumno=models.ForeignKey(Alumno,null=False,blank=False,on_delete=models.CASCADE)
	Curso=models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
	FechaMatricula = models.DateField(auto_now_add=True)

	def InformacionMatricula(self):
		cadena = "{0} => {1}"
		return cadena.format(self.Alumno,self.Curso.Nombre)

	def __str__(self):
		return self.InformacionMatricula()