from django.apps import AppConfig
import threading
from django.db.backends.signals import connection_created
from django.dispatch import receiver
from .utils import check_and_retrieve_samples


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        # Kết nối tín hiệu để kiểm tra số lượng mẫu khi server khởi động
        @receiver(connection_created)
        def start_background_task(sender, **kwargs):
            thread = threading.Thread(target=check_and_retrieve_samples)
            thread.start()
