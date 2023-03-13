from django.db import models

# Create your models here.
class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    ingressi = models.TextField(blank=True)
    teksti = models.TextField()
    kuva = models.ImageField(upload_to='blogi/kuvat', null=True) #(null=True meinaa että ei ole pakko olla kuvaa)
    luotu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.otsikko
    
    def luo_ingressi(self):
        if self.ingressi:
            return self.ingeressi
        return self.teksti[:50] + '...'