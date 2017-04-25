from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']


class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class InscricaoResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoCientificoResource(ModelResource):
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }


class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoAutorResource(ModelResource):
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get']
        filtering = {
            "descricao": ('exact', 'startswith')
        }