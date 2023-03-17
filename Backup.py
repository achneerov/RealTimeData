import requests
import time
from inputimeout import inputimeout, TimeoutOccurred
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation



bitcoinList = []
ethereumList = []
count = 0
count2 = 0

# from the visualizer
x_data, y_data = [], []
figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')
# from the visualizer

#TestList = ["21666.096434195875", "21666.096434195875", "21654.701921178068", "21654.701921178068", "21654.701921178068", "21654.153910142228", "21654.153910142228", "21654.153910142228", "21654.153910142228", "21654.153910142228", "21654.153910142228", "21652.72347584858", "21652.72347584858", "21652.72347584858", "21652.255619286407", "21652.255619286407", "21652.255619286407", "21652.14718688133"]


def update(frame):
        x_data.append(datetime.now())
        #y_data.append(randrange(0, 100)) THIS WAS WHAT IS ORIGINALLY IN THIS FUNCTION
        
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
        #print(len(bitcoinList))
        
        #time.sleep(0)
        while len(bitcoinList) >  60:
            bitcoinList.pop(0)
        
        barHeight = (bitcoinList[len(bitcoinList)-1] - bitcoinList[0])/bitcoinList[0]
        #print(barHeight)
        barHeightPerc = barHeight*100
        print(barHeightPerc)

        y_data.append(barHeightPerc)
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

    

