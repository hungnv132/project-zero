from datetime import datetime
from django.contrib import admin
from .models import Industry, Company, TradingDaily
from .filters import DateFilter


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created_at']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'exchange', 'symbol', 'name', 'industry', 'created_at']
    readonly_fields = ['slug']


@admin.register(TradingDaily)
class TradingDailyAdmin(admin.ModelAdmin):
    red_dark = 'red'
    green_dark = '#1dc14d'
    yellow = '#fc0'

    red_light = '#FFD2D2'
    green_light = '#D3FFD3'
    yellow_light = '#ffefb2'
    
    list_display = ['id', 'date', 'industry_', 'company_', 'volume_', 'ref_',
                    'open_', 'close_', 'change_', 'percent_',  'high_', 'low_',
                    'foreign_buy_', 'foreign_sell_']
    search_fields = ['company__symbol']
    list_filter = [DateFilter]

    def get_queryset(self, request):
        queryset = super(TradingDailyAdmin, self).get_queryset(request)
        return queryset.order_by('company__industry__name')

    def span_tag(self, value, color='black', float='right', weight='normal'):
        span = "<span style=\"color: {color};font-weight:{weight};float:{float};\">" \
               "{value}" \
               "</span>"
        return span.format(value=value, color=color, float=float, weight=weight)
    
    def div_tag(self, value, styles):
        css = ';'.join(['{}: {}'.format(key, value)
                        for key, value in styles.items()])

        div = "<div style=\"{css}\">{value}</div>"
        return div.format(value=value, css=css)

    def add_link(self, url, name):
        link = "<a href=\"{url}\" target=\"_blank\">{name}</a>"
        return link.format(url=url, name=name)

    def get_dark_color(self, obj):
        color = self.green_dark if obj.close > obj.ref else\
            (self.red_dark if obj.close < obj.ref else self.yellow)
        return color

    def get_light_color(self, obj):
        color = self.green_light if obj.close > obj.ref else\
            (self.red_light if obj.close < obj.ref else self.yellow_light)
        return color

    def industry_(self, obj):
        styles = {
            'background-color': obj.company.industry.color,
            'text-align': 'right',
            'line-height': '32px',
            'padding-right': '10px',
            'font-weight': 'bold',
            'font-size': '16px'
        }
        return self.div_tag(value=obj.company.industry, styles=styles)
    industry_.admin_order_field = 'company__industry__name'
    industry_.allow_tags = True

    def company_(self, obj):
        color = self.get_light_color(obj)
        styles = {
            'background-color': color,
            'line-height': '32px',
            'font-weight': 'bold',
            'text-align': 'center',
        }
        return self.div_tag(value=obj.company.symbol, styles=styles)
        # return self.add_link(url=obj.company.url, name=name)
    company_.allow_tags = True
    company_.admin_order_field = 'company__name'

    def volume_(self, obj):
        return self.span_tag(value=obj.volume, weight='bold')
    volume_.allow_tags = True

    def foreign_buy_(self, obj):
        return self.span_tag(value=obj.foreign_buy_volume)
    foreign_buy_.allow_tags = True
    foreign_buy_.admin_order_field = 'foreign_buy'

    def foreign_sell_(self, obj):
        return self.span_tag(value=obj.foreign_sell_volume)
    foreign_sell_.allow_tags = True
    foreign_sell_.admin_order_field = 'foreign_sell'

    def ref_(self, obj):
        return self.span_tag(value=obj.ref_price, color=self.yellow)
    ref_.allow_tags = True

    def open_(self, obj):
        return self.span_tag(value=obj.open_price)
    open_.allow_tags = True

    def close_(self, obj):
        color = self.get_dark_color(obj)
        return self.span_tag(value=obj.close_price, color=color, weight='bold')
    close_.allow_tags = True

    def high_(self, obj):
        return self.span_tag(value=obj.high_price)
    high_.allow_tags = True

    def low_(self, obj):
        return self.span_tag(value=obj.close_price)
    low_.allow_tags = True

    def change_(self, obj):
        color = self.get_dark_color(obj)
        value = "{:,}".format(obj.close - obj.ref)
        return self.span_tag(value=value, color=color, weight='bold')
    change_.allow_tags = True

    def percent_(self, obj):
        color = self.get_dark_color(obj)
        change = (obj.close - obj.ref)/float(obj.ref)*100
        percent = "{:+.2f}%".format(change)
        return self.span_tag(value=percent, color=color, weight='bold')
    percent_.allow_tags = True

    class Media:
        css = {
            "all": ("trading_daily.css",)
        }