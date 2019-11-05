from django.shortcuts import render
from question import models
from django.core.paginator import Paginator


def paginate(objects_list, objects_per_page, num_of_page):
    paginator = Paginator(objects_list, objects_per_page)
    objects_page = paginator.get_page(num_of_page)
    return objects_page, paginator


def list_of_question(request, page=1):
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    questions = models.Question.manager.get_all()
    top_tags = models.TopTag.manager.get_all()
    page_questions, paginator = paginate(questions, 20, page)

    return render(request, "question/questions.html",
                  {"Tags": tags, "Questions": page_questions, "Users": users, "Paginator": paginator,
                   "TopTags": top_tags})


def new_question(request):
    questions = models.Question.manager.get_all()
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    return render(request, "question/new-question.html", {"Tags": tags, "Questions": questions, "Users": users})


def login(request):
    questions = models.Question.manager.get_all()
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    return render(request, "question/login.html", {"Tags": tags, "Questions": questions, "Users": users})


def answers(request, num=1):
    questions = models.Question.manager.get_by_id(num)
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    return render(request, "question/answers.html",
                  {"ID": questions, "Tags": tags, "Questions": questions, "Users": users})


def registration(request):
    questions = models.Question.manager.get_all()
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    top_tags = models.TopTag.manager.get_all()
    return render(request, "question/signup.html",
                  {"Tags": tags, "Questions": questions, "Users": users, "TopTags": top_tags})


def settings(request):
    questions = models.Question.manager.get_all()
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    top_tags = models.TopTag.manager.get_all()
    return render(request, "question/settings.html",
                  {"Tags": tags, "Questions": questions, "Users": users, "TopTags": top_tags})


def tags_list(request, name='', page=1):
    users = models.Profile.manager.get_all()
    tags = models.Tag.manager.get_all()
    questions = models.Question.manager.filter_by_tag_name(name)

    top_tags = models.TopTag.manager.get_all()

    page_questions, paginator = paginate(questions, 20, page)

    return render(request, "question/question_by_tag.html",
                  {"Tags": tags, "Questions": page_questions, "Users": users, "Paginator": paginator,
                   "TopTags": top_tags, "CurTag": name})
