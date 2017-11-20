import os
import sys
import csv
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zero.settings.local")
django.setup()

from stock.models import Company


def import_companies():
    filename = 'companies.csv'
    lookup = 'https://www.stockbiz.vn/Stocks/{}/Overview.aspx'
    with open(filename, 'r') as csvfile:
        # reader = csv.reader(csvfile, delimiter=',')
        reader = csv.DictReader(csvfile)
        for row in reader:
            symbol = row['symbol']
            row['vn30'] = True if row['vn30'] == 'True' else False
            row['url'] = lookup.format(symbol)
            company, created = Company.objects.get_or_create(symbol=symbol,
                                                             defaults=row)
            if created:
                print(' + [{}] is created.'.format(symbol))
            else:
                print(' - [{}] is existed.'.format(symbol))

if __name__ == '__main__':
    import_companies()