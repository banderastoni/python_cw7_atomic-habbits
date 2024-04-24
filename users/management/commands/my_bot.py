from django.core.management import BaseCommand

from config import settings
from habits.services import send_telegram_message


class Command(BaseCommand):

    def handle(self, *args, **options):
        chat_id = settings.telegram_id  # Здесь мог бы быть ваш chat_id ;)
        message = "Have a nice day, buddy! Cheers in my awesome coursework?"
        return send_telegram_message(chat_id, message)
