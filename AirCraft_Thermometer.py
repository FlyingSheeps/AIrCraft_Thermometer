import serial #You need pyserial
import time
import datetime
import matplotlib.pyplot as plt
import csv

plotbuffer = [[],[]] #プロット用のバッファー
serial0 = serial.Serial('COM3', 9600,timeout=2.0) #シリアル通信を開く ポート名とボーレートは自分でチェックして
with open('temperture.csv','w',newline='') as f: #ログ用CSV開く
    writer = csv.writer(f) #CSVライタ
    while(True):
        serial0.reset_input_buffer() #最新のデータを読むために一度バッファを消す
        valr = serial0.readline() #シリアル通信を一行読む
        print(valr) #デバッグ
        vald = float(valr) #文字越で来るので数値に変換
        #ここでもしXXX,XXX,XXXの形式で飛んできたら、先に,で分解すればfloatで数値を抽出できる
        dt_now = datetime.datetime.now() #時間を取得
        
        print(dt_now,vald) #デバッグ
        writer.writerow([dt_now,vald]) #CSV書き込み
        plotbuffer[0].append(dt_now) #バッファ格納
        plotbuffer[1].append(vald) 

        plt.plot(plotbuffer[0], plotbuffer[1]) #グラフ更新
        plt.pause(5) #グラフを保持する時間。ここで更新頻度（秒）を設定できる
        plt.clf() #グラフを削除