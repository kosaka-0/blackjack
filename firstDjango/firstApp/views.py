from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
import random
import BJGame.redis_helper as r
import BJGame.blackjack as bj

# Create your views here.

def hello(request):
    return HttpResponse('konnnitiwa')

def card(request):
    return render(request, 'card.html')

def welcome(request):
    name = '田中'
    dictionary = {'name' : name}
    return render(request, 'name.html', dictionary)

def welcome2(request, name):
    dictionary = {'name' : name}
    return render(request, 'name.html', dictionary)

def cards(request):
    rank_str = [str(i).zfill(2) for i in range(1, 14)]
    return render(request, 'cards.html', {'card_rank': rank_str})

def random_cards(request):
    suits = ['S', 'H', 'D', 'C']
    ranks = range(1, 14)
    deck = [(x, y) for x in ranks for y in suits]
    random.shuffle(deck)
    card1 = deck.pop()
    card2 = deck.pop()

    dictionary = {
        'suit' : card1[1],
        'rank' : str(card1[0]).zfill(2),
        'suit2' : card2[1],
        'rank2' : str(card2[0]).zfill(2),
    }
    return render(request, 'display_cards.html', dictionary)

def form_test(request):
    if request.method == 'POST':
        print(request.POST)
        return welcome2(request, request.POST['name'])
    elif request.method == 'GET':
        dictionary = {}
        dictionary.update(csrf(request))
        return render(request, 'form.html', dictionary)

def form_card(request):
    if request.method == 'GET':
        rank_list = [str(i) for i in range(1, 14)]
        dictionary = {'rank_list' : rank_list}
        dictionary.update(csrf(request))
        return render(request, 'select_card.html', dictionary)

    if request.method == 'POST':
        suit = request.POST['suit']
        rank = request.POST['rank'].zfill(2)
        dictionary = {'suit':suit, 'rank':rank}
        print(suit, rank)
        return render(request, 'display_card2.html', dictionary)

def login(request):
    if request.method == 'GET':
        if request.session.get('token', False):
            token = request.session['token']
            name = r.get_value(token)
            return welcome2(request, name)
        else:
            request.session['token'] = str(random.random())
            dictionary = {}
            dictionary.update(csrf(request))
            return render(request, 'form.html', dictionary)

    elif request.method == 'POST':
        token = request.session['token']
        name = request.POST['name']
        r.set_value(token, name)
        return welcome2(request, name)