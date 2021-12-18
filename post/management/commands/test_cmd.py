from django.core.management.base import BaseCommand, CommandError
from post.models import Post

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('post_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for post_id in options['post_ids']:
            try:
                poll = Post.objects.get(pk=post_id)
            except Post.DoesNotExist:
                raise CommandError('post "%s" does not exist' % post_id)

            poll.status = 'PUB'
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % post_id))