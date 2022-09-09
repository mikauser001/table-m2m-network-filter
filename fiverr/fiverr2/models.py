from django.db import models


# Create your models here.
class Network(models.Model):
    name = models.CharField(u'Name', max_length=100)
    coins = models.ManyToManyField("Coins", blank=True, related_query_name='coins_network_q', related_name='Network')
    def __str__(self):
        return self.name


class Coins(models.Model):
    name = models.CharField(u'Name', max_length=100)
    logo_c = models.ImageField(blank=True, upload_to='user_upload/')
    logo_dark = models.ImageField(blank=True, upload_to='user_upload/')
    order = models.IntegerField(null=True)
    exchange = models.ManyToManyField("Exchange", blank=True, verbose_name='exchange', related_name='coins', related_query_name='ex_coin_q')

    def __str__(self):
        return self.name


class Tradingpairs(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Waehrung(models.Model):
    name = models.CharField(u'Name', max_length=100)
    zeichen = models.CharField(u'Zeichen', max_length=3)

    def __str__(self):
        return self.name


class Fiat(models.Model):
    name = models.CharField(u'Name', max_length=100)
    waehrung = models.ManyToManyField(Waehrung)

    def __str__(self):
        return self.name


class Exchange(models.Model):


    name = models.CharField(max_length=100, verbose_name='Exchange')
    logo = models.ImageField(blank=True, upload_to='user_upload', verbose_name='Exchange Logo')
    active = models.BooleanField(null=True, default=True)
    link = models.CharField(max_length=200, blank=True)
    withdraw_fee = models.CharField(max_length=100, blank=True)
    taker_fee = models.CharField(max_length=100, blank=True)
    maker_fee = models.CharField(max_length=100, blank=True)
    confirmations = models.CharField(max_length=100, blank=True)
    dex = models.BooleanField(verbose_name='DEX')
    kyc = models.BooleanField(default=False, verbose_name='KYC')
    kyc_info = models.CharField(max_length=300, blank=True)
    fiat = models.ManyToManyField(Fiat, blank=True)
    fiat_offramp = models.ManyToManyField(Fiat, u'ex_fiat_offramp', blank=True)
    tradingpairs = models.ManyToManyField(Tradingpairs, blank=True)
    tradinglink_pre = models.CharField(max_length=100, blank=True)
    tradinglink_mid = models.CharField(max_length=100, blank=True)
    tradinglink_post = models.CharField(max_length=100, blank=True)
    tradinglink_dfi = models.BooleanField(null=True)
    width = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(null=True)
    overview = models.BooleanField(default=False)
    basic = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def all_coin(self):
        return ', '.join([x.name for x in self.coin.all()])


    def all_coin_logo(self):
        return [x.logo for x in self.coin.all()]




class Paymentservice(models.Model):
    name = models.CharField(u'Name', max_length=100)
    logo = models.ImageField(blank=True, upload_to='user_upload/')
    link = models.CharField(max_length=200, blank=True)
    fiat_onramp = models.ManyToManyField(Fiat, u'fiat_onramp', blank=True)
    fiat_offramp = models.ManyToManyField(Fiat, u'fiat_offramp', blank=True)
    coin_onramp = models.ManyToManyField(Coins, u'coin_onramp', blank=True)
    coin_offramp = models.ManyToManyField(Coins, u'coin_offramp', blank=True)
    onramp_fees = models.CharField(max_length=200, blank=True)
    offramp_fees = models.CharField(max_length=200, blank=True)
    kyc = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(null=True)
    width = models.CharField(max_length=100, blank=True)
    overview = models.BooleanField(default=False)
    basic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Addressderivation(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Wallettype(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Functions(models.Model):
    name = models.CharField(u'Name', max_length=100)
    describtion = models.CharField(u'describtion', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Addressmode(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(u'Name', max_length=100)
    abbreviation = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name


class Wallets(models.Model):
    name = models.CharField(u'Name', max_length=100)
    logo = models.ImageField(blank=True, upload_to='user_upload/')
    order = models.IntegerField(null=True)
    link = models.CharField(max_length=200, blank=True)
    infrastructure = models.CharField(max_length=100, blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True, blank=True)
    addressmode = models.ManyToManyField(Addressmode, blank=True)
    platform = models.ManyToManyField(Platform, blank=True)
    languages = models.ManyToManyField(Languages, blank=True)
    type = models.ForeignKey(Wallettype, on_delete=models.CASCADE, null=True)
    addressderivation = models.ManyToManyField(Addressderivation, blank=True)
    walletfunctions = models.ManyToManyField(Functions, blank=True)
    width = models.CharField(max_length=100, blank=True)
    overview = models.BooleanField(default=False)
    basic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Servicetype(models.Model):
    name = models.CharField(u'Name', max_length=100)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(u'Name', max_length=100)
    fee = models.CharField(max_length=100, blank=True)
    minimal = models.CharField(max_length=100, blank=True)
    coins = models.ManyToManyField(Coins, blank=True)

    def __str__(self):
        return self.name


class Serviceplatform(models.Model):
    name = models.CharField(u'Name', max_length=100)
    logo = models.ImageField(blank=True, upload_to='user_upload/')
    link = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(null=True)
    servicetype = models.ForeignKey(Servicetype, on_delete=models.CASCADE, null=True, blank=True)
    staking = models.CharField(max_length=150, blank=True)
    liquiditymining = models.CharField(max_length=150, blank=True)
    rewardfees = models.CharField(max_length=150, blank=True)
    fees = models.CharField(max_length=150, blank=True)
    services = models.ManyToManyField(Services, blank=True)
    coin = models.ManyToManyField(Coins, blank=True)
    width = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Wrappingservice(models.Model):
    name = models.CharField(u'Name', max_length=100)
    logo = models.ImageField(blank=True, upload_to='user_upload/')
    description = models.CharField(max_length=300, blank=True)
    link = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=100, blank=True)
    coin_onwrap = models.ManyToManyField(Coins, u'coin_on', blank=True)
    coin_offwrap = models.ManyToManyField(Coins, u'coin_off', blank=True)
    coins_erc20 = models.ManyToManyField(Coins, u'coins_erc20', blank=True)
    coins_bep20 = models.ManyToManyField(Coins, u'coins_vep20', blank=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name

