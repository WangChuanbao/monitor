import os
import channels

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitor.settings")
application = channels.asgi.get_channel_layer()