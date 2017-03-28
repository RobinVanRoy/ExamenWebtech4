from django.shortcuts import render
import random

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=2)
# r.set('vraag:1', 'Am I lucky')
# r.sadd('antwoord:1', 'Yes definitely')
# r.sadd('antwoord:1', 'Most likely')
# r.sadd('antwoord:1', 'Ask again later')
# r.sadd('antwoord:1', 'Do not count on it')

# r.set('vraag:2', 'Will I pass my exam')
# r.sadd('antwoord:2', 'Without a doubt')
# r.sadd('antwoord:2', 'Yes')
# r.sadd('antwoord:2', 'Concentrate and ask again')
# r.sadd('antwoord:2', 'My sources say no')


def index(request):
    return render(request, 'eightball/index.html', None)


def anwser(request):
    question = request.POST.get('question')
    questions = r.keys('vraag*')
    questions.sort()
    for q in questions:
        value = r.get(q)
        if value == question:
            i = str.split(q, ':')[1]
            anwsers = r.smembers('antwoord:' + i)
            anwsers_list = []
            for a in anwsers:
                anwsers_list.append(a)
            print (anwsers_list)
            # anwser = random.choice(anwsers_list)
            anwser = anwsers_list[0]
            context = {'anwser': anwser}

    return render(request, 'eightball/anwser.html', context)
