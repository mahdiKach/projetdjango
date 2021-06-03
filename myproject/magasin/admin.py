from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Commande)
admin.site.register(Emballage)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)