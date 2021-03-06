from django.shortcuts import render
import json

from .models import Pessoa
from .forms import PessoaForm, SearchForm

def pessoa(request):
   form = PessoaForm(request.POST or None)
   listagem = Pessoa.objects.using('pessoas_db').all()
   search = SearchForm(request.POST or None)

   if request.method == 'POST':
      if form.is_valid():
         form.save()

   busca = request.GET.get('search')
   if busca:
      listagem = Pessoa.objects.using('pessoas_db').filter(nome__icontains = busca)
      
      rows = len(listagem)
      if rows == 0:
         print("Sem registros!")
      else:
         for busca in listagem:
            print(busca.profissao)
            
   params = {
      'form': form,
      'listagem': listagem,
      'search': search
   }

   return render(request, 'pessoa.html', params)
