from django.db import models
from datetime import datetime
from django.utils.timezone import now


# Create your models here.

class Profile(models.Model):
    login = models.CharField(max_length=255, verbose_name='Login')
    name = models.CharField(max_length=255, verbose_name='Name')
    rating = models.IntegerField(default=0, verbose_name='Rating')
    birthday = models.DateField(default=now(), verbose_name='Birthday')
    email = models.EmailField(verbose_name="Email")
    avatar = models.ImageField(verbose_name="Avatar")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    tags = models.ManyToManyField('Tag', blank=True, related_name='question')
    thumbs_up = models.IntegerField(verbose_name="Num_of_likes", default=0)
    thumbs_down = models.IntegerField(verbose_name="Num_of_dislikes", default=0)
    datetime_published = models.DateTimeField(verbose_name='Published Date')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(models.Model):
    text = models.TextField(verbose_name='Text')
    is_correct = models.BooleanField(default=False)
    datetime_published = models.DateTimeField(verbose_name='Published Date')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='User')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name='Question', related_name='answers'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class Tag(models.Model):  # TODO поле amount при добавлении нового вопроса с данным тегом увеличивать на 1
    name = models.CharField(max_length=15, verbose_name='Name')

    amount = models.IntegerField(max_length=255, default=0)

    #
    # objects = TagManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class TopTag(models.Model):
    name = models.CharField(max_length=15, verbose_name='Name')
    amount = models.IntegerField(max_length=255, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "TopTag"
        verbose_name_plural = "TopTags"


class TopUser(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    top_id = models.IntegerField(verbose_name='UserId')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "TopUser"
        verbose_name_plural = "TopUsers"