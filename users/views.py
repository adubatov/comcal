from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
import urllib3

from .forms import CustomUserCreationForm
from .models import CustomUser

import requests

from pprint import pprint

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # model = CustomUser
    template_name = 'users/signup.html'


class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = get_user_model()
    context_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.user = context['object']
        context['deal'] = self.get_deal_details()
        context['deals'] = self.get_user_deals()
        return context
    
    def get_deal_details(self):
        url = 'https://mirni.bitrix24.ru/rest/23/rpgxs100qycfzutf/'
        method = 'crm.deal.get'
        params = {'id': 31}
        url = f'{url}/{method}'
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()['result']
        else:
            return response.json()['error_description']

    def get_user_deals(self):
        url = 'https://mirni.bitrix24.ru/rest/23/rpgxs100qycfzutf'
        method = 'crm.deal.list'
        params = {
            'order[]': {'ID': 'ASC'},
            'filter[STAGE_ID]': ['C5:WON'],
            'filter[STAGE_ID]': ['C5:UC_LRLFKL'], #Закрытие документов 
            'filter[UF_CRM_1588922563]': [0], # Комиссионные выплачены?
            'filter[ASSIGNED_BY_ID]': self.user.bitrix_user_id,
            'select[]': ['ID', 'TITLE', 'ASSIGNED_BY_ID', 'STAGE_ID', 'OPPORTUNITY']
        }
        url = f'{url}/{method}'
        response = requests.get(url, params=params)
        pprint(response.json())
        pprint(response.__dict__['url'])
        if not response.error:
            return response.json()['result']
        else:
            return response.json()['error_description']
        



class UserUpdateView(UpdateView):
    # form_class = CustomUserChangeForm
    model = get_user_model()
    context_name = 'user'
    template_name = 'users/user_update.html'
    fields = [
        'first_name', 
        'last_name',
        ]

    # def test_func(self):
    #     return self.get_object() == self.request.user

    def get_success_url(self) -> str:
        return reverse_lazy('user_detail', kwargs={'pk': self.request.user.pk})

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)