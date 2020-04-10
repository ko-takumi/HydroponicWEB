from django.shortcuts import render
from .forms import WateringForm, TemperatureForm, HumidityForm, PictureForm, GrowForm, SettingForm
from .models import WateringLog, TemperatureLog, HumidityLog, PictureLog, ColorLog
from .models import Temperature, Humidity, Growth
from .models import TimeSetting, LineSetting, WaterSetting

from django.http import HttpResponse
from django.views.generic import View

import matplotlib.pyplot as plt
import numpy as np
import io
import os

def index(request):
    tempre = Temperature.objects.get(id=1)
    humidity = Humidity.objects.get(id=1)
    growh_1 = Growth.objects.get(id=1)

    params = {
            'title': 'Hydroponic',
            'temperature': tempre.value,
            'humidity': int(humidity.value),
            'growh_1': growh_1.value
        }
    return render(request, 'Hydroponic/index.html', params)

def rebootCmd(request):
    os.system('/home/pi/reboot.sh &') # 再起動

    tempre = Temperature.objects.get(id=1)
    humidity = Humidity.objects.get(id=1)
    growh_1 = Growth.objects.get(id=1)

    params = {
            'title': 'Hydroponic',
            'temperature': tempre.value,
            'humidity': int(humidity.value),
            'growh_1': growh_1.value
        }
    return render(request, 'Hydroponic/index.html', params)


class temperature(View):
    def get(self, request):
        # 初期値を決定
        # データ数が10未満の場合は、データ数
        items = TemperatureLog.objects.count()
        if(items < 10):
            num = items
        else:
            num = 10

        initial_data = {
            'dataNum': num
            }
        data = TemperatureLog.objects.all()[len(TemperatureLog.objects.all())-num:]
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': TemperatureForm(request.POST or None, initial=initial_data),
            }
        return render(request, 'Hydroponic/Log/temperature.html', params)

    def post(self, request):
        num = int(request.POST['dataNum'])
        data = TemperatureLog.objects.all()[len(TemperatureLog.objects.all())-num:]

        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': TemperatureForm(request.POST),
            }
        return render(request, 'Hydroponic/Log/temperature.html', params)

class humidity(View):
    def get(self, request):
        # 初期値を決定
        # データ数が10未満の場合は、データ数
        items = HumidityLog.objects.count()
        if(items < 10):
            num = items
        else:
            num = 10

        initial_data = {
            'dataNum': num
            }
        data = HumidityLog.objects.all()[len(HumidityLog.objects.all())-num:]
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': HumidityForm(request.POST or None, initial=initial_data),
            }
        return render(request, 'Hydroponic/Log/humidity.html', params)

    def post(self, request):
        num = int(request.POST['dataNum'])
        data = HumidityLog.objects.all()[len(HumidityLog.objects.all())-num:]
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': HumidityForm(request.POST),
            }
        return render(request, 'Hydroponic/Log/humidity.html', params)

class picture(View):
    def get(self, request):
        # 初期値を決定
        # データ数が10未満の場合は、データ数
        items = PictureLog.objects.count()
        if(items < 5):
            num = items
        else:
            num = 5
        initial_data = {
            'dataNum': num
            }

        data = PictureLog.objects.all()[len(PictureLog.objects.all())-num:]
        for item in data:
            item.fileName = "Hydroponic/images/" + item.fileName
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': PictureForm(request.POST or None, initial=initial_data),
            }
        return render(request, 'Hydroponic/Log/picture.html', params)

    def post(self, request):
        print(request.POST)
        num = int(request.POST['dataNum'])
        data = PictureLog.objects.all()[len(PictureLog.objects.all())-num:]
        for item in data:
            item.fileName = "Hydroponic/images/" + item.fileName
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': PictureForm(request.POST),
            }
        return render(request, 'Hydroponic/Log/picture.html', params)

class grow(View):
    def get(self, request):
        # 初期値を決定
        # データ数が10未満の場合は、データ数
        items = ColorLog.objects.count()
        if(items < 5):
            num = items
        else:
            num = 5
        initial_data = {
            'dataNum': num
            }

        data = ColorLog.objects.all()[len(ColorLog.objects.all())-num:]
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': GrowForm(request.POST or None, initial=initial_data),
            }
        return render(request, 'Hydroponic/Log/grow.html', params)

    def post(self, request):
        num = int(request.POST['dataNum'])
        data = ColorLog.objects.all()[len(ColorLog.objects.all())-num:]
        params = {
                'title': 'Hydroponic',
                'data': data,
                'dataNum': num,
                'form': GrowForm(request.POST),
            }
        return render(request, 'Hydroponic/Log/grow.html', params)

class setting(View):

    def get(self, request):
        photoTime = TimeSetting.objects.get(name='photoTime')
        plantManagemntTime = TimeSetting.objects.get(name='plantManagemntTime')
        notifyTime = TimeSetting.objects.get(name='notifyTime')
        temperatureSaveTime = TimeSetting.objects.get(name='temperatureSaveTime')
        warteringTime = WaterSetting.objects.get(name='warteringTime')
        lineToken = LineSetting.objects.get(name='lineToken')
        initial_data = {
            'photoTime': photoTime.time,
            'plantManagemntTime': plantManagemntTime.time,
            'notifyTime': notifyTime.time,
            'temperatureSaveTime': temperatureSaveTime.time,
            'warteringTime': warteringTime.value,
            'lineToken': lineToken.value,
            }

        params = {
                'title': 'Hydroponic',
                'form': SettingForm(request.POST or None, initial=initial_data),
            }

        return render(request, 'Hydroponic/Setting/index.html', params)

    def post(self, request):
        print(request.POST)
        # 撮影間隔を保存
        photoTime = TimeSetting.objects.get(name='photoTime')
        photoTime.time = request.POST['photoTime']
        photoTime.save()

        # 水やり間隔を保存
        plantManagemntTime = TimeSetting.objects.get(name='plantManagemntTime')
        plantManagemntTime.time = request.POST['plantManagemntTime']
        plantManagemntTime.save()

        # LINE通知間隔を保存
        notifyTime = TimeSetting.objects.get(name='notifyTime')
        notifyTime.time = request.POST['notifyTime']
        notifyTime.save()

        # 環境保存間隔を保存
        temperatureSaveTime = TimeSetting.objects.get(name='temperatureSaveTime')
        temperatureSaveTime.time = request.POST['temperatureSaveTime']
        temperatureSaveTime.save()

        # 水量を保存
        warteringTime = WaterSetting.objects.get(name='warteringTime')
        warteringTime.value = request.POST['warteringTime']
        warteringTime.save()

        # LINETOKENを保存
        lineToken = LineSetting.objects.get(name='lineToken')
        lineToken.value = request.POST['lineToken']
        lineToken.save()

        os.system('/home/pi/reboot.sh &') # 再起動
        return HttpResponse("<script> alert('5秒後に再起動します'); window.location.href = '.'; </script>")

class plotGraph(View):
    
    def get(self, request):
                
        yList = []
        xList = []
        plotMax = 0.0
        plotMin = 0.0
            
        if('tmperature' == request.GET['msg']):
            dataNum = int(request.GET['num'])   # グラフ対象のデータ数を取得      
            
            data = TemperatureLog.objects.all()[len(TemperatureLog.objects.all())-dataNum:]
            
            for item in data:
                yList.append(float(item.temperature))
                history = item.history.split()
                history = history[1][:8]    # 日付,時間のみを抽出
                xList.append(history)
            
            plotMin = 0
            plotMax = 40

        elif('humidity' == request.GET['msg']):
            dataNum = int(request.GET['num'])   # グラフ対象のデータ数を取得
            data = HumidityLog.objects.all()[len(HumidityLog.objects.all())-dataNum:]
            
            for item in data:
                yList.append(float(item.humidity))
                history = item.history.split()
                history = history[1][:8]    # 日付,時間のみを抽出
                xList.append(history)
                
            plotMin = 0
            plotMax = 100

        elif('grow' == request.GET['msg']):
            dataNum = int(request.GET['num'])   # グラフ対象のデータ数を取得
            data = ColorLog.objects.all()[len(ColorLog.objects.all())-dataNum:]
            
            for item in data:
                yList.append(float(item.green))
                history = item.history.split()
                history = history[1][:8]    # 日付,時間のみを抽出
                xList.append(history)
                
            plotMin = 0
            plotMax = 300

        self.__setPlt(xList, yList, plotMin, plotMax)       # create the plot
        svg = self.__pltToSvg() # convert plot to SVG
        plt.cla()        # clean up plt so it can be re-used
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def __setPlt(self, xList, yList, plotMin, plotMax):
        x = np.array(xList)
        y = np.array(yList)
        plt.subplots(figsize=(10,4))
        plt.ylim(plotMin,plotMax)
        plt.plot(x, y, color="k", label="data")
        
    def __pltToSvg(self):
        buf = io.BytesIO()
        plt.savefig(buf, format='svg', bbox_inches='tight')
        s = buf.getvalue()
        buf.close()
        return s
