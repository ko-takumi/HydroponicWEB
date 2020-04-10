# -*- coding: utf-8 -*-
from django import forms
from .models import WateringLog, TemperatureLog, HumidityLog, PictureLog, ColorLog
# from .models import Friend

class WateringForm(forms.ModelForm):
    class Meta:
        model = WateringLog
        fields = ['history']

class TemperatureForm(forms.Form):
    try:
        items = TemperatureLog.objects.count()
    except:
        items = 0
    dataNum = forms.IntegerField(
        label='グラフ対象数',
        min_value=0,
        max_value=items
        )

class HumidityForm(forms.Form):
    try:
        items = HumidityLog.objects.count()
    except:
        items = 0
    dataNum = forms.IntegerField(
        label='グラフ対象数',
        min_value=0,
        max_value=items
        )

class PictureForm(forms.Form):
    try:
        items = PictureLog.objects.count()
    except:
        items = 0
    dataNum = forms.IntegerField(
        label='表示対象数',
        min_value=0,
        max_value=items
        )

class GrowForm(forms.Form):
    try:
        items = ColorLog.objects.count()
    except:
        items = 0
    dataNum = forms.IntegerField(
        label='グラフ対象数',
        min_value=0,
        max_value=items
        )

class SettingForm(forms.Form):
    photoTime = forms.IntegerField(
        label='写真撮影間隔(ms)',
        min_value=0,
        max_value=99999
        )

    plantManagemntTime = forms.IntegerField(
        label='水やり間隔(ms)',
        min_value=0,
        max_value=99999
        )

    notifyTime = forms.IntegerField(
        label='LINE通知間隔(ms)',
        min_value=0,
        max_value=99999
        )

    temperatureSaveTime = forms.IntegerField(
        label='温度記憶間隔(ms)',
        min_value=0,
        max_value=99999
        )

    warteringTime = forms.FloatField(
        label='水量(ms)',
        min_value=0,
        max_value=10
        )

    lineToken = forms.CharField(
        label='LINE-TOKEN'
        )