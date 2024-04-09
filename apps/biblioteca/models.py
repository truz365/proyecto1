from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=255)
    
    

    def __str__(self):
        return self.nombre
    
class editorial(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class genero(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
            return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    ano_edicion = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    Autor = models.ManyToManyField(Autor, blank=True, null=True)
    genero = models.ManyToManyField(genero)
    editorial = models.ForeignKey(editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    


                              
