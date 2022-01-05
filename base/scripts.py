from .models import Telegram


def save_token(token_id, request):
    obj = Telegram.objects.create()
    if Telegram.objects.filter(token__isnull=True):
        Telegram_instance = Telegram.objects.get(token__isnull=True)
        Telegram_instance.token = token_id
        Telegram_instance.save()
        if Telegram.objects.filter(token=token_id):
            current_user = request.user
            obj = Telegram.objects.get(token=token_id)
            id = obj.id
            obj_1 = Telegram.objects.get(pk=id)
            obj_1.user = current_user
            obj_1.save()




