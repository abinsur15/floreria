from django.db import models

# Create your models here.
class Estado(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    name=models.CharField(max_length=100,)

    def __str__(self):
        return self.id

class Flor(models.Model):
    codigo=models.CharField(primary_key=True,max_length=100)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=150)
    valor=models.IntegerField()
    stock=models.IntegerField()
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="flores",null=True)

    def __str__(self):
        return self.codigo