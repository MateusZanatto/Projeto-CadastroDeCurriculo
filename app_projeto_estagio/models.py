from django.db import models

class Curriculos(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=255)  
    data_nascimento = models.DateField() 
    idade = models.IntegerField()  
    email = models.EmailField()  
    telefone = models.CharField(max_length=15)  
    endereco = models.CharField(max_length=255)  
    cargo = models.CharField(max_length=255)  
    empresa = models.CharField(max_length=255)  
    inicio = models.DateField()  
    termino = models.DateField()  
    descricao = models.TextField()  
    instituicao = models.CharField(max_length=255) 
    curso = models.CharField(max_length=255)  
    periodo = models.CharField(max_length=50)  

    def __str__(self):
        return self.nome

class usuario(models.Model):
    id = models.AutoField(primary_key=True) 
    usuario = models.CharField(max_length=255)  
    senha = models.CharField(max_length=255)  

    def __str__(self):
        return self.usuario
