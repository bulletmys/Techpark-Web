from django.core.management.base import BaseCommand, CommandError
from question.models import Tag, TopTag, Question
from django.core.paginator import Paginator


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            tags = Tag.objects.order_by('amount').reverse()[0:20]
        except Tag.DoesNotExist:
            raise CommandError('Tags does not exist')

        TopTag.objects.all().delete()
        for tag in tags:
            t = TopTag(name=tag.name, amount=tag.amount)
            t.save()

        # self.stdout.write(self.style.SUCCESS('Successfully added top 20 tags "%s"' % tags))
        self.stdout.write(self.style.SUCCESS('Successfully added top 20 tags "%s"' % Question.objects.filter(tags__id=1)))
