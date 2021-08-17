from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key= True)
    nombreusuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nombreusuario


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=20)
    nombres = models.CharField(max_length=25)
    apellido = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    class Meta:
        db_table = 'clientes'


class Facturas(models.Model):
    id = models.AutoField(primary_key=True)
    Cli_id = models.ForeignKey(Clientes,on_delete=models.CASCADE,null=True)
    empresa = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    numfactura = models.CharField(max_length=60)
    class Meta:
        db_table = 'facturas'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    class Meta: 
        db_table = 'product'


class FacturasProduct(models.Model):
    id = models.AutoField(primary_key=True)
    id_fact = models.ForeignKey(Facturas,on_delete=models.CASCADE,null=True)
    id_produ = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'facturasproduct'


