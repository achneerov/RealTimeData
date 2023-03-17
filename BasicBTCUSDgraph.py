## I used this to see if my chart is even accurate

import requests
import time
import datetime
from inputimeout import inputimeout, TimeoutOccurred
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import xlim

bitcoinList = []
ethereumList = []
count = 0
count2 = 0

# from the visualizer
x_data, y_data = [], []
figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')



def update(frame):
        x_data.append(datetime.now())
        
        try:
            user_input = inputimeout(prompt='q?', timeout=1)
            if user_input == 'q':
                print("the length of the bitcoin list is " + str(len(bitcoinList)))
                print("the first value in the list is " + str(bitcoinList[0]))
                print("the last value in the list is " + str(bitcoinList[len(bitcoinList)-1]))
                quit()
        
        except TimeoutOccurred:
            pass
            
        url = "http://api.coincap.io/v2/assets/bitcoin/"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        bitcoinPrice = response.json()['data']['priceUsd']
        
        bitcoinList.append(float(bitcoinPrice))
        while len(bitcoinList) >  60:
            bitcoinList.pop(0)
        currentPrice = bitcoinList[len(bitcoinList)-1]
   
        
        print(currentPrice)
        y_data.append(currentPrice)
        

        line.set_data(x_data, y_data)
        figure.gca().relim()
        figure.gca().autoscale_view()
        return line,

while (True and count < 500):
    animation = FuncAnimation(figure, update, interval=1000) 

    if count2 == 0:
        pyplot.show()
        count2 += 1
    
    count +=1

    ######## from visualizer

    

