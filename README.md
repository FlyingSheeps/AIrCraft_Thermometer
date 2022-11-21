# AirCraft_Thermometer

秋月とかで売ってるADT7410を使って（現状一箇所）の温度を測定する。  
pythonを使ってリアルタイムプロットとcsvログが可能。

今後需要に応じて4点検温まで拡大予定（ADT7410の仕様的にアドレスは4種類まで）。  
ラズピコとか使えばI2C二系統あるので8点まで拡大可能。  
ADT7310をSPIで繋げば結構いくらでも付けれる。

ADT7410  
I2C https://akizukidenshi.com/catalog/g/gM-06675/  
ADT7310  
SPI https://akizukidenshi.com/catalog/g/gM-06708/

耐熱範囲が150℃まであるので桁焼きに最適。

一般的なライブラリに加えてpyserialが必要。


# 使い方

1. raspberrypi picoにArduino IDEでpico_thermo.inoを書き込む。
2. マイコンがつながっているPCのポート番号を確認する（このプログラムではCOM3となっている）。
3. プログラムのポート番号を実際のポート番号に変更、ボーレートをマイコンに合わせる。
4. プログラムを実行。コマンドプロンプトでの実行でしか動作確認していないので注意。  
今後実行時に引数としてポート、ボーレート、更新頻度を追加できるようにしたい。

# 温度制御理論検討
温度制御の検討のためにMatlabで単純適応制御を一次遅れ系に適用するシミュレーションを行った．  
σ-修正法（ゲインの変動に一次遅れをかける）を用いることでゲインのバースト現象を抑えることに成功した．
シミュレーション上では時定数1sの炉に適応可能であり，時定数が大きくなるほど目標追従性能は良くなる．

![一次遅れ](/fig/rag.png)  
![温度](/fig/temp.png)  
![誤差](/fig/error.png)  
![ゲイン](/fig/gain.png)  