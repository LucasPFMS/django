from django.db.models import Sum
from .models import Question, Choice
def minimax():
    questions = Question.objects.all()
    min = max = (questions[0], 0)
    for q in questions:
        n = q.choice_set.aggregate(sum=Sum('votes'))['sum']
        if n > max[1]:
            max = (q, n)
        if n < min[1]:
            min = (q, n)
    return (min[0], max[0])
