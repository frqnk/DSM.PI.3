from .models import Doacao
from .forms import DoacaoForm, ProdutoForm
from . import forms
from pymongo import MongoClient
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from bson.objectid import ObjectId
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
import re


# Configurar a conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Conexao_alimentar']
collection = db['doacoes']


def home(request):
    return render(request, 'home.html')


def registro(request):
    if request.method == 'POST':
        doacao_form = DoacaoForm(request.POST)
        produto_forms = [ProdutoForm(request.POST, prefix=str(i))
                         for i in range(5)]  # Permitir 5 produtos

        if doacao_form.is_valid() and all([pf.is_valid() for pf in produto_forms]):
            dados_doacao = doacao_form.cleaned_data
            produtos = []
            for pf in produto_forms:
                produto = {
                    'nome': pf.cleaned_data['nome'],
                    'quantidade': pf.cleaned_data['quantidade']
                }
                produtos.append(produto)

            # Monta o objeto de nova doação incluindo o local_destino
            nova_doacao = {
                'nome': dados_doacao['nome'],
                'data_doacao': timezone.now(),
                'produtos': produtos,
                'documento': dados_doacao['documento'],
                'local_destino': request.POST.get('local_destino', '')
            }

            # Insere a nova doação no MongoDB
            collection.insert_one(nova_doacao)

            return redirect('sucesso')
        else:
            # Se o formulário não for válido, renderiza o template com os formulários preenchidos e os erros
            return render(request, 'registro.html', {'doacao_form': doacao_form, 'produto_forms': produto_forms})
    else:
        # Se for uma requisição GET, cria os formulários vazios para exibição inicial
        doacao_form = DoacaoForm()
        produto_forms = [ProdutoForm(prefix=str(i)) for i in range(5)]

    # Renderiza o template de registro com os formulários vazios ou preenchidos
    return render(request, 'registro.html', {'doacao_form': doacao_form, 'produto_forms': produto_forms})


def pagina_sucesso(request):
    return render(request, 'sucesso.html')


def listar_doacoes(request):
    doacoes = list(collection.find())
    for doacao in doacoes:
        doacao['id'] = str(doacao['_id'])
    return render(request, 'listar.html', {'doacoes': doacoes})


def excluir_doacao(request, doacao_id):
    if request.method == 'POST':
        collection.delete_one({'_id': ObjectId(doacao_id)})
        return redirect('listar')  # Corrigido para 'listar'
    return render(request, 'listar.html')


def editar_doacao(request, doacao_id):
    doacao = collection.find_one({'_id': ObjectId(doacao_id)})

    if doacao is None:
        # Redirecionar se a doação não for encontrada
        return redirect('listar')

    if request.method == 'POST':
        doacao_form = DoacaoForm(request.POST)
        produto_forms = [ProdutoForm(request.POST, prefix=str(i))
                         for i in range(5)]

        if doacao_form.is_valid() and all([pf.is_valid() for pf in produto_forms]):
            dados_doacao = doacao_form.cleaned_data
            produtos = []
            for pf in produto_forms:
                produto = {
                    'nome': pf.cleaned_data['nome'],
                    'quantidade': pf.cleaned_data['quantidade']
                }
                produtos.append(produto)

            nova_doacao = {
                'nome': dados_doacao['nome'],
                'data_doacao': timezone.now(),
                'produtos': produtos,
                'documento': dados_doacao['documento']
            }
            collection.update_one({'_id': ObjectId(doacao_id)}, {
                                  '$set': nova_doacao})
            return redirect('listar')

    else:
        initial_data = {
            'nome': doacao.get('nome', ''),
            'documento': doacao.get('documento', '')
        }
        doacao_form = DoacaoForm(initial=initial_data)
        produto_forms = [ProdutoForm(initial={'nome': produto.get('nome', ''), 'quantidade': produto.get('quantidade', 1)}, prefix=str(i))
                         for i, produto in enumerate(doacao.get('produtos', []))]

    return render(request, 'editar_doacao.html', {'doacao_form': doacao_form, 'produto_forms': produto_forms})
