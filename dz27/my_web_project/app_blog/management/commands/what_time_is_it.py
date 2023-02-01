from datetime import datetime

import pytz
from django.core.management.base import BaseCommand
from django.utils import timezone

from my_web_project.settings import TIME_ZONE, USE_TZ


class Command(BaseCommand):
    help = 'Отображает текущее время'

    def handle(self, *args, **kwargs):
        # datetime.datetime.now() зависит от settings.TIME_ZONE
        # django.utils.timezone.now() всегда возвращает время UTC.
        # Это не зависит от settings.TIME_ZONE. Это дает собственный
        # или осведомленный объект datetime в зависимости от
        # значений settings.USE_TZ
        tz_New_York = 'America/New_York'
        self.stdout.write(f"\nsettings.TIME_ZONE: '{TIME_ZONE}'.")
        self.stdout.write(f"\nsettings.USE_TZ: {USE_TZ}.")
        self.stdout.write(f"\ntz_New_York: '{tz_New_York}'.")

        self.stdout.write("\nЭксперимент 1. Временная зона не активирована.\n\n")

        time1 = timezone.now()
        self.stdout.write("Используется django.utils.timezone.now()")
        self.stdout.write(f"Текущее время: {time1.strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {time1.strftime('%z')}")
        self.stdout.write(f"Временная зона: {time1.tzinfo}")

        time2_1 = datetime.now(pytz.timezone(tz_New_York))
        self.stdout.write(f"\nЧасовой пояс: '{tz_New_York}'.")
        self.stdout.write(f"\nИспользуется datetime.datetime.now()")
        self.stdout.write(f"Текущее время: {datetime.now().strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {datetime.now().strftime('%z')}")
        self.stdout.write(f"Временная зона: {datetime.now().tzinfo}")
        self.stdout.write(f"\nИспользуется datetime.now(pytz.timezone('{tz_New_York}'))")
        self.stdout.write(f"Текущее время: {time2_1.strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {time2_1.strftime('%z')}")
        self.stdout.write(f"Временная зона: {time2_1.tzinfo}")

        time2_2 = datetime.now(pytz.timezone(TIME_ZONE))
        self.stdout.write(f"\nЧасовой пояс: '{TIME_ZONE}'.")
        self.stdout.write(f"\nИспользуется datetime.datetime.now()")
        self.stdout.write(f"Текущее время: {datetime.now().strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {datetime.now().strftime('%z')}")
        self.stdout.write(f"Временная зона: {datetime.now().tzinfo}")
        self.stdout.write(f"\nИспользуется datetime.now(pytz.timezone('{TIME_ZONE}'))")
        self.stdout.write(f"Текущее время: {time2_2.strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {time2_2.strftime('%z')}")
        self.stdout.write(f"Временная зона: {time2_2.tzinfo}")

        self.stdout.write(f"\nЭксперимент 2. Активирована временная зона '{tz_New_York}'.")
        self.stdout.write(f"Оператор: timezone.activate(pytz.timezone('{tz_New_York}'))\n\n")
        timezone.activate(pytz.timezone(tz_New_York))

        time3 = timezone.now()
        self.stdout.write("Используется django.utils.timezone.now()")
        self.stdout.write(f"Текущее время: {time3.strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {time3.strftime('%z')}")
        self.stdout.write(f"Временная зона: {time3.tzinfo}")

        time4 = datetime.now()
        self.stdout.write(f"\nИспользуется datetime.datetime.now()")
        self.stdout.write(f"Текущее время: {time4.strftime('%X')}")
        self.stdout.write(f"Смещение к Гривинчу: {time4.strftime('%z')}")
        self.stdout.write(f"Временная зона: {time4.tzinfo}")
