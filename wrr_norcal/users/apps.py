from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "wrr_norcal.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import wrr_norcal.users.signals  # noqa F401
        except ImportError:
            pass
