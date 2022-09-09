import django_tables2 as tables
from .models import Exchange, Network, Coins
from django.utils.safestring import mark_safe

class ExchangeTable(tables.Table):

    # coin Template Column

    coins = tables.TemplateColumn('{% for i in record.coins.all %}<img class="coin_logo" style="margin-bottom: 2px; margin-left: 0rem; max-height: 32px;" '
        'width="" title={{i.name}} src="/media/{{i.logo_c}}"/> {% endfor %} ', orderable=False)


    logo = tables.TemplateColumn(
        '{% if record.logo %} <img class="logo" style="margin-bottom: 2px; margin-left: 0rem; max-height: 32px;" '
        'width=""  src="/media/{{record.logo}}"/> {% endif %}'
        , orderable=False)
    dex = tables.BooleanColumn()
    name = tables.Column()


    class Meta:
        model = Exchange
        template_name = "django_tables2/bootstrap.html"
        fields = ('name', 'logo', 'coins', 'dex', 'kyc', 'maker_fee')
