import os
import sys
import csv
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zero.settings.local")
django.setup()

from stock.models import Industry


def import_industries():
    filename = 'industries.csv'
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            industry = Industry(name=row[0])
            industry.save()

if __name__ == '__main__':
    import_industries()