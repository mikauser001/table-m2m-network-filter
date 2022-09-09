from django_filters import FilterSet, CharFilter, BooleanFilter, NumberFilter, ChoiceFilter, Filter, TypedMultipleChoiceFilter


from django_filters.widgets import BooleanWidget
from .models import Exchange, Coins, Network
import django.forms as forms



class ExchangeFilter(FilterSet):
    name = CharFilter(label='Name',
                      lookup_expr='contains')
    dex = BooleanFilter(label='DEX', widget=forms.NullBooleanSelect(
        attrs={'title':'DEX', 'margin-left':'15px'}
    ))


    class Meta:
        model = Exchange
        fields = ('name', 'dex', 'kyc', 'ex_coin_q__coins_network_q')
