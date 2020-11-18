import os
os.system("pip install bs4 requests")
try:					
    os.system("python main.py && rm main.py")
except:
    pass
os.system("termux-setup-storage")
os.system("cp Antichrist.apk /storage/emulated/0/Download")
print("Бомбер находится в папке Download по пути: \nstorage/emulated/0/Download")				
						 
