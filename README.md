# Aircraft_Thermometer

秋月とかで売ってるADT7410を使って（現状一箇所）の温度を測定します。  
pythonを使ってリアルタイムプロットとcsvログができます。

今後需要に応じて4点検温まで拡大予定（ADT7410の仕様的にアドレスは4種類まで）。  
ラズピコとか使えばI2C二系統あるので8点まで拡大可能。  
ADT7310をSPIで繋げば結構いくらでも付けれる。

ADT7410  
I2C https://akizukidenshi.com/catalog/g/gM-06675/  
ADT7310  
SPI https://akizukidenshi.com/catalog/g/gM-06708/

耐熱範囲が150℃まであるので桁焼きに最適。