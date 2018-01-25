from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import QuestionForm
from .models import *


def index(request):
    if request.method == 'GET':
        question_form = QuestionForm
    else:
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return redirect('index')
    person = PersonalInfo.objects.first()
    home_images = Home.objects.all()
    before_after = BeforeAfter.objects.all().order_by('?')[:6]
    categories = CategoryWorkOut.objects.all()
    question_pagenator = Paginator(Question.objects.all(), 5)

    page = request.GET.get('page')
    question = question_pagenator.get_page(page)

    ctx = {
        'person': person,
        'home_images': home_images,
        'before_after': before_after,
        'categories': categories,
        'questions': question,
        'question_form': question_form,
    }
    return render(request, 'blog/index.html', ctx)

