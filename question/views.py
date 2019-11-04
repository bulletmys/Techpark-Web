from django.shortcuts import render
from django.http import HttpResponse
from question import models
from django.core.paginator import Paginator


# Create your views here.
def list_of_question(request, page=1):
    users = models.Profile.objects.all()
    tags = models.Tag.objects.all()
    questions = models.Question.objects.all()

    paginator = Paginator(questions, 2)
    page_questions = paginator.get_page(page)

    top_tags = models.TopTag.objects.all()

    return render(request, "question/questions.html",
                  {"Tags": tags, "Questions": page_questions, "Users": users, "Paginator": paginator,
                   "TopTags": top_tags})


def new_question(request):
    questions = models.Question.objects.all()
    users = models.Profile.objects.all()
    tags = models.Tag.objects.all()
    return render(request, "question/new-question.html", {"Tags": tags, "Questions": questions, "Users": users})


def login(request):
    return render(request, "question/login.html")


def answers(request, num=1):
    questions = models.Question.objects.get(id=num)

    users = models.Profile.objects.all()
    tags = models.Tag.objects.all()
    return render(request, "question/answers.html",
                  {"ID": questions, "Tags": tags, "Questions": questions, "Users": users})


def registration(request):
    questions = models.Question.objects.all()
    users = models.Profile.objects.all()
    tags = models.Tag.objects.all()
    top_tags = models.TopTag.objects.all()
    return render(request, "question/signup.html",
                  {"Tags": tags, "Questions": questions, "Users": users, "TopTags": top_tags})


def settings(request):
    questions = models.Question.objects.all()
    users = models.Profile.objects.all()
    tags = models.Tag.objects.all()
    top_tags = models.TopTag.objects.all()
    return render(request, "question/settings.html",
                  {"Tags": tags, "Questions": questions, "Users": users, "TopTags": top_tags})


def tags_list(request, name='', page=1):
    users = models.Profile.objects.all()
    tags = models.Tag.objects.all()
    questions = models.Question.objects.filter(tags__name=name)

    paginator = Paginator(questions, 20)
    page_questions = paginator.get_page(page)

    top_tags = models.TopTag.objects.all()

    return render(request, "question/question_by_tag.html",
                  {"Tags": tags, "Questions": page_questions, "Users": users, "Paginator": paginator,
                   "TopTags": top_tags, "CurTag": name})

