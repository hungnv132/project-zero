from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib import admin
from stock.services import Quote


def custom_admin_view_urls():
    return [
        {
            'title': "Stock Daily",
            'url': reverse("admin:stock_daily")
        }
    ]


class CustomAdminView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(CustomAdminView, self).get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'site_header': self.site_header,
            'has_permission': admin.site.has_permission(self.request)
        })
        return context


class StockDailyView(CustomAdminView):
    template_name = 'admin/stock_daily.html'
    title = site_header = 'Stock Daily'

    def get_context_data(self, **kwargs):
        context = super(CustomAdminView, self).get_context_data(**kwargs)
        symbols = ['VNM', 'VCB', 'HPG', 'PVS']
        quotes = list()
        for symbol in symbols:
            quote = Quote(symbol)
            quote.update_prices_today()
            quotes.append(quote)
        context.update({
            'quotes': quotes,
        })
        return context
