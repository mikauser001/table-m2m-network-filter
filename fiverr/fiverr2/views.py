from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, MultiTableMixin
from .models import Exchange
from .tables import ExchangeTable
from .filter import ExchangeFilter
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)


class FilterTableView(SingleTableMixin, FilterView):
        model = Exchange
        table_class = ExchangeTable
        template_name = 'template.html'
        filterset_class = ExchangeFilter



