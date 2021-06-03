from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Create your models here.
from django.urls import reverse


class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballe')]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non definie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    emballage = models.OneToOneField('Emballage', on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "libelle {} description {} prix {} type{}".format(self.libelle,self.description,self.prix,self.type)

class Emballage(models.Model):
    TYPE_CHOICES=[('bl','blanc'),('rg','rouge'),('ble','bleur'),('vr','vert'),('muli','multicolore')]
    matiere=models.CharField(max_length=100)
    couleur=models.CharField(max_length=10,choices=TYPE_CHOICES,default='Transparent')
    def __str__(self):
        return "matiere {} couleur {}".format(self.matiere,self.couleur)
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "nom {} adresse {} email {} telephone {}".format(self.nom,self.adresse,self.email,self.telephone)
        _
class Commande(models.Model):
    Duree_garantie=models.CharField(max_length=100)
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    product = models.ForeignKey(Produit, null=True, on_delete= models.SET_NULL)
    def __str__(self):
        return "durre_garantie{} date de commande {} total Commandes {} produits{}".format(self.Duree_garantie,self.dateCde,self.totalCde,self.product)

class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    nom=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    def __str__(self):
        return self.nom
class Order(models.Model):
    client=models.ForeignKey(Client,on_delete=models.SET_NULL,blank=True,null=True)
    date_orderd=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)
    @property
    def get_chariot_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_chariot_items(self):
        orderitems=self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    produit=models.ForeignKey(Produit,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    @property
    def get_total(self):
        total=self.produit.prix*self.quantity
        return total


class ShippingAdress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    adresse=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    date_added = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.adresse
