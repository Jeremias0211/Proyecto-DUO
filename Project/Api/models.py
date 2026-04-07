from django.db import models

# Create your models here.
class Producto(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=20)
    Precio=models.FloatField()
    Cantidad=models.IntegerField()
    Descripcion=models.TextField(max_length=50)
    Categoria= models.TextField(max_length=20)
    Fecha=models.DateField()
    Imagen= models.ImageField(upload_to='Productos',null=True)
    # --> En este caso retornamos el nombre del producto.
    def __str__(self):
        return self.Nombre