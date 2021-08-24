import sys  
import os.path  
import win32clipboard as w    
import win32con  
import win32api  
import time

def getText():#读取剪切板  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_TEXT)  
    w.CloseClipboard()  
    return d  
def setText(aString):#写入剪切板  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardText(aString)  
    w.CloseClipboard() 
input = 0

print('replace enter')
print('Refresh every five seconds, be patient ')
while True:
    time.sleep(2)
    if getText() != input:
        input = getText().decode("utf8","ignore")
        out = input.replace('\n', ' ').replace('\r', '')
        setText(out)
    if str(input) == "007":
        break
