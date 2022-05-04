from django.db import models
from django.urls import reverse

# Create your models here.


class Categoria(models.Model):
    categoria_nome = models.CharField(max_length=65, unique=True)


class PortfolioDetail(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    descricao = models.TextField(max_length=700)
    detalhe = models.TextField()
    link_github = models.URLField(blank=True,
        default=None,)
    link_demo = models.URLField(blank=True,
        default=None,)
    categoria_nome = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    img_portfolio = models.ImageField(
        upload_to='portapp/img/', blank=True, default='portapp/img/img-placeholder.webp')

    img_prev = models.ImageField(
        upload_to='portapp/img/', blank=True, default='portapp/img/img-placeholder.jpg')

    def get_absolute_url(self):
        return reverse('portapp:portfolio_detail',  args=[self.slug])
