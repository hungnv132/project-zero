from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from core.utils import crawl_data
from stock.models import Company, TradingDaily
from datetime import date


class Command(BaseCommand):
    help = 'Crawl data of the stock'

    def get_object(self):
        return Company.objects.all()

    def handle(self, *args, **options):
        today = date.today()
        for obj in self.get_object():
            symbol = obj.symbol
            print(" - Crawling {}: ".format(symbol))
            data = crawl_data(symbol=symbol)
            if data:
                data.update({
                    'company': obj
                })
                print(" - [{}]: {}".format(symbol, data))
                try:
                    trading, created = TradingDaily.objects.update_or_create(
                        company__symbol=symbol,
                        date=today,
                        defaults=data
                    )
                    if created:
                        print(' + [{}] is recorded.'.format(symbol))
                    else:
                        print(' - [{}] is update.'.format(symbol))

                except IntegrityError:
                    print('{} is updated today.'.format(obj.symbol))
            else:
                print("========> {}: Empty")


