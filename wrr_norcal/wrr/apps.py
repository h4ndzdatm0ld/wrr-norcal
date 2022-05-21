from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "wrr_norcal.wrr"
    verbose_name = _("WRR")

    # def ready(self):
    #     try:
    #         import wrr_norcal.wrr.signals  # noqa F401
    #     except ImportError:
    #         pass
