from django.db import models
from datetime import datetime
from django.utils.timezone import now


class ProfileManager(models.Manager):
    def get_all(self):
        self.all()


class Profile(models.Model):
    login = models.CharField(max_length=255, verbose_name='Login')
    name = models.CharField(max_length=255, verbose_name='Name')
    rating = models.IntegerField(default=0, verbose_name='Rating')
    birthday = models.DateField(default=now(), verbose_name='Birthday')
    email = models.EmailField(verbose_name="Email")
    avatar = models.ImageField(verbose_name="Avatar", blank=True)
    likes = models.ManyToManyField('Like', related_name='Profile_like', blank=True)
    dislikes = models.ManyToManyField('DisLike', related_name='Profile_dislike', blank=True)
    manager = ProfileManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class QuestionManager(models.Manager):
    def get_all(self):
        return self.all()

    def get_by_id(self, index):
        return self.get(id=index)

    def filter_by_tag_name(self, name):
        return self.filter(tags__name=name)


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    tags = models.ManyToManyField('Tag', blank=True, related_name='question')
    datetime_published = models.DateTimeField(verbose_name='Published Date')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='User')

    like = models.ManyToManyField('Like', related_name='question_like', blank=True)
    dislike = models.ManyToManyField('DisLike', related_name='question_dislike', blank=True)
    manager = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class AnswerManager(models.Manager):
    def get_all(self):
        self.all()


class Answer(models.Model):
    text = models.TextField(verbose_name='Text')
    is_correct = models.BooleanField(default=False)
    datetime_published = models.DateTimeField(verbose_name='Published Date')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='User')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name='Question', related_name='answers'
    )
    likes = models.ForeignKey('Like', on_delete=models.CASCADE, verbose_name='likes', related_name='answer_likes',
                              blank=True, null=True)
    dislikes = models.ForeignKey('DisLike', on_delete=models.CASCADE, verbose_name='dislikes',
                                 related_name='answer_dislikes', blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class TagManager(models.Manager):
    def get_all(self):
        self.all()


class Tag(models.Model):  # TODO поле amount при добавлении нового вопроса с данным тегом увеличивать на 1
    name = models.CharField(max_length=15, verbose_name='Name')

    amount = models.IntegerField(max_length=255, default=0)

    manager = TagManager()

    #
    # objects = TagManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class TopTagManager(models.Manager):
    def get_all(self):
        self.all()


class TopTag(models.Model):
    name = models.CharField(max_length=15, verbose_name='Name')
    amount = models.IntegerField(max_length=255, default=0)
    manager = TopTagManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "TopTag"
        verbose_name_plural = "TopTags"


class TopUserManager(models.Manager):
    def get_all(self):
        self.all()


class TopUser(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    top_id = models.IntegerField(verbose_name='UserId')
    manager = TopUserManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "TopUser"
        verbose_name_plural = "TopUsers"


class LikeManager(models.Manager):
    def get_all(self):
        self.all()


class Like(models.Model):
    manager = LikeManager()


    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"


class DisLike(models.Model):
    manager = LikeManager()

    class Meta:
        verbose_name = "DisLike"
        verbose_name_plural = "DisLikes"
