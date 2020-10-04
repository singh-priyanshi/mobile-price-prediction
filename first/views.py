# import sys
# sys.path.append('E:\\django_project\\first\\files')

from . import price_prediction as pp
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from django_tables2.tables import Table

# Create your views here.

from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from django.template import RequestContext
import os
#from django.shortcuts import render_to_response


def jqueryserver(request):
    print("in jqueryserver")
    response_string="hello"
    if request.is_ajax()== True:
            print("ajaxxx")
            print(response_string)
            plt.plot(range(10))
            buf = BytesIO()
            plt.savefig(buf, format='png')
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
            # print("image base64" + image_base64)
            # print("home")
            buf.close()
            # return render(request,'home1.html',{'data1':image_base64})
            # return render_to_response('home1.html', {'data1': image_base64}, RequestContext(request))
            data = {'data1':['ssas',],'data2':["Dsdsd",]}

            print(data)
            # data = render_to_string('home1.html', {'data1': "hello"})
            return HttpResponse(data)
            # return render_to_response('jqueryserver.html',data)

def predict_price_lr(request):
    print('redirecitng')
    return  render(request,'predict_price_lr.html')


def predict_price_nbc(request):
    print('redirecitng')
    return  render(request,'predict_price_nbc.html')
def home(request):

    knn = pp.KNN()
    lr = pp.LR()
    nbc = pp.NBC()
    # print("type of "+type(knn)+"\n\n")
    plt = knn.elbow()

    buf = BytesIO()
    plt.savefig(buf,format = 'png')
    elbow = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()

    KNNscore =knn.score
    print(KNNscore)
    # plt.plot(range(10))
    # buf = BytesIO()
    # plt.savefig(buf, format='png')
    # image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    # # print("image base64" + image_base64)
    # print("home")
    # buf.close()
    mycwd = os.getcwd()

    df = pd.read_csv(os.path.join(os.getcwd() + '\\new_data.csv'))
    os.chdir(mycwd)

    # df = pd.read_csv('D:\\django_project\\new_data.csv')
    # html_table = df.head().to_html()
    html_table = pp.showhead().to_html()
    print(df.head())
    # df_table = Table(df.head().to_dict(orient='list'))

    print(df.head())
    # return render(request, "home1.html", {'df_table': df_table})
    return render(request,'home.html', {'html_table': html_table,'elbow':elbow,'KNNscore':KNNscore,'NBCscore':nbc.score,'LRscore':lr.score})


def predictlr(request):
    if request.method =="POST":
        spec = pp.Specs()
        delattr(spec,'price_range')
        spec.battery_power= request.POST['BATTERY_POWER']
        spec.blue = request.POST['BLUETOOTH']
        spec.clock_speed = request.POST['CLOCK_SPEED']
        spec.dual_sim  = request.POST['DUAL_SIM']
        spec.fc  =request.POST['FRONT_CAMERA']
        spec.four_g = request.POST['FOUR_G']
        spec.int_memory = request.POST['INTERNAL_MEMORY']
        spec.m_dep =request.POST['MOBILE_DEPTH']
        spec.mobile_wt = request.POST['MOBILE_WEIGHT']
        spec.n_cores = request.POST['NUMBER_OF_CORES']
        spec.pc = request.POST['PRIMARY_CAMERA']
        spec.px_height=request.POST["PIXEL_HEIGHT"]
        spec.px_width = request.POST['PIXEL_WIDTH']
        spec.ram =request.POST['RAM']
        spec.sc_h = request.POST['SCREEN_HEIGHT']
        spec.sc_w = request.POST['SCREEN_WIDTH']
        spec.talk_time = request.POST['BATTERY_LIFE']
        spec.three_g = request.POST['THREE_G']
        spec.touch_screen = request.POST["TOUCH_SCREEN"]
        spec.wifi  = request.POST["WIFI"]


        lr  = pp.LR()
        price = lr.LRpredict(spec)
        print(price)

        # nbc = pp.NBC()
        # price = nbc.NBCpredict(spec)
        #
        # if  price <=1 :
        #     res = "0-10,000"
        # elif price >=  1 and price <= 2:
        #     res = "10,000- 20,000"
        # elif price >=2 and price <= 3 :
        #     res = "20,000 - 35,000"
        # else:
        #     res ="Grester than 35,000"

    # return render(request, 'predict_price.html', {'price':price})
    return HttpResponse(price)

def predictnbc(request):
    if request.method == "POST":
        spec = pp.Specs()
        delattr(spec, 'price_range')
        spec.battery_power = request.POST['BATTERY_POWER']
        spec.blue = request.POST['BLUETOOTH']
        spec.clock_speed = request.POST['CLOCK_SPEED']
        spec.dual_sim = request.POST['DUAL_SIM']
        spec.fc = request.POST['FRONT_CAMERA']
        spec.four_g = request.POST['FOUR_G']
        spec.int_memory = request.POST['INTERNAL_MEMORY']
        spec.m_dep = request.POST['MOBILE_DEPTH']
        spec.mobile_wt = request.POST['MOBILE_WEIGHT']
        spec.n_cores = request.POST['NUMBER_OF_CORES']
        spec.pc = request.POST['PRIMARY_CAMERA']
        spec.px_height = request.POST["PIXEL_HEIGHT"]
        spec.px_width = request.POST['PIXEL_WIDTH']
        spec.ram = request.POST['RAM']
        spec.sc_h = request.POST['SCREEN_HEIGHT']
        spec.sc_w = request.POST['SCREEN_WIDTH']
        spec.talk_time = request.POST['BATTERY_LIFE']
        spec.three_g = request.POST['THREE_G']
        spec.touch_screen = request.POST["TOUCH_SCREEN"]
        spec.wifi = request.POST["WIFI"]

        nbc = pp.NBC()
        price = nbc.NBCpredict(spec)

        if  price <=1 :
            res = "0-10,000"
        elif price >=  1 and price <= 2:
            res = "10,000- 20,000"
        elif price >=2 and price <= 3 :
            res = "20,000 - 35,000"
        else:
            res ="Grester than 35,000"

    return HttpResponse(res)

    # return render(request, 'home.html', {'image_base64':  image_base64 })
    # return render_to_response('home1.html', {'html_table': html_table}, RequestContext(request))
#
# def plot(request4)):
#     # # Data for plotting
#     # t = np.arange(0.0, 2.0, 0.01)
#     # s = 1 + np.sin(2 * np.pi * t)
#     #
#     # fig, ax = plt.subplots()
#     # ax.plot(t, s)
#     #
#     # ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#     #        title='About as simple as it gets, folks')
#     # ax.grid()
#     #
#     # response = HttpResponse(content_type = 'image/png')
#     # canvas = FigureCanvasAgg(fig)
#     # canvas.print_png(response)
#     # #return render(request,'home.html',canvas)
#     # return response
#     plot = figure()
#     plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")
#
#     script, div = components(plot)
#
#     return render(request, 'home.html', {'script': script, 'div': div})

def showhead(request):


    df = pd.read_csv('D:\\django_project\\new_data.csv')
    html_table = df.head().to_html()
    print(df.head())
    df_table = Table(df.head().to_dict(orient='list'))
    print(df.head())
    # return render(request, "home1.html", {'df_table': df_table})
    return render_to_response('home.html', {'html_table': html_table}, RequestContext(request))

def plot(request):
    list = {
        'data':[1,2,3,4,6]
    }
    return render(request,'home.html',list)