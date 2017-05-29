from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized

class TipoInscricaoResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        if not(TipoInscricao.objects.filter(descricao=bundle.data['descricao'])):
            tipo = TipoInscricao()
            tipo.descricao = bundle.data['descricao'].upper()
            tipo.save()
            bundle.obj = tipo
            return bundle
        else:
            raise Unauthorized("Ja existe um tipo inscrição com esse nome!")

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Não é possivel deletar toda a lista!")

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


class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class InscricaoResource(ModelResource):
    def obj_create(self, bundle, **kwargs):
        p = bundle.data['pessoa'].split("/")
        e = bundle.data['evento'].split("/")
        print(p[4])
        print(e[4])
        if not(Inscricoes.objects.filter(pessoa = p[4], evento = e[4])):
            t = bundle.data['tipo'].split("/")

            inscricao = Inscricoes()

            inscricao.pessoa = PessoaFisica.objects.get(pk = int(p[4]) )
            inscricao.evento = Evento.objects.get(pk = int(e[4]) )
            inscricao.tipoInscricao = TipoInscricao.objects.get(pk = int(t[4]) )

            inscricao.dataEHoraDaInscricao = bundle.data["dataEHoraDaInscricao"]
            inscricao.save()
            bundle.obj = inscricao
            return bundle
        else:
            raise Unauthorized("Pessoa ja cadastrada no evento!")

    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    evento = fields.ToOneField(EventoResource, 'evento')
    tipo = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class EventoCientificoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }


class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }

class ArtigoAutorResource(ModelResource):
    autor = fields.ToOneField(AutorResource, 'autor')
    artigo = fields.ToOneField(ArtigoCientificoResource, 'artigo')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith')
        }