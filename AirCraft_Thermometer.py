import serial
import time
import datetime
import matplotlib.pyplot as plt
import csv

plotbuffer = [[],[]]
serial0 = serial.Serial('COM3', 115200,timeout=2.0)
with open('temperture.csv','w',newline='') as f:
    writer = csv.writer(f)
    while(True):
        serial0.reset_input_buffer()
        valr = serial0.readline()
        print(valr)
        vald = float(valr)
        #ここでもしXXX,XXX,XXXの形式で飛んできたら、先に,で分解すればfloatで数値を抽出できる
        dt_now = datetime.datetime.now()
        
        print(dt_now,vald)
        writer.writerow([dt_now,vald])
        plotbuffer[0].append(dt_now)
        plotbuffer[1].append(vald)

        plt.plot(plotbuffer[0], plotbuffer[1])
        plt.pause(5)
        plt.clf() 