from django.db import models
from slugify import slugify
from core.models import TrackingTime
from core.constants import EXCHANGE


class Industry(TrackingTime):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name, only_ascii=True)
        return super(Industry, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'


class Company(TrackingTime):
    symbol = models.CharField(max_length=4, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    url = models.URLField(blank=True, null=True)
    exchange = models.CharField(choices=EXCHANGE, default=EXCHANGE[0][0],
                                max_length=5)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL,
                                 related_name='companies',
                                 blank=True, null=True)
    vn30 = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name, only_ascii=True)
        return super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format(self.symbol, self.name)

    @staticmethod
    def find_by_symbol(symbol):
        return Company.objects.get(symbol=symbol)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class TradingDaily(TrackingTime):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                                related_name='trading_daily',
                                blank=True, null=True)
    ref = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    vol = models.IntegerField(blank=True, null=True)
    agreement = models.IntegerField(blank=True, null=True)
    foreign_buy = models.IntegerField(blank=True, null=True)
    foreign_sell = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    @property
    def open_price(self):
        return "{:,}".format(self.open)

    @property
    def close_price(self):
        return "{:,}".format(self.close)

    @property
    def high_price(self):
        return "{:,}".format(self.high)

    @property
    def low_price(self):
        return "{:,}".format(self.low)

    @property
    def ref_price(self):
        return "{:,}".format(self.ref)

    @property
    def volume(self):
        return "{:,}".format(self.vol)

    @property
    def foreign_buy_volume(self):
        return "{:,}".format(self.foreign_buy)

    @property
    def foreign_sell_volume(self):
        return "{:,}".format(self.foreign_sell)

    class Meta:
        verbose_name = 'Trading Daily'
        verbose_name_plural = 'Trading Daily'
        unique_together = ('company', 'date')
