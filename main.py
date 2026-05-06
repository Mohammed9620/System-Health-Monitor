import psutil
import time
from Email_send import Send_alert

alert_sender = Send_alert()

while True:
    cpu_per=psutil.cpu_percent(interval=1)
    Usage_RAM=psutil.virtual_memory().percent

    print(f"CPU: {cpu_per}% | RAM: {Usage_RAM}%")

    if cpu_per>80:
        with open("alerts.log.txt", mode='a') as f:
            f.write(f"Warning The Usage for CPU is High: {cpu_per}%\n")
            f.write(f"Time: {time.ctime()}\n")
    if Usage_RAM>90:
        with open("alerts.log.txt", mode='a') as f:
            print("🚨 RAM usage is high! Sending email...")
            alert_sender.send_alert(f"Warning! Your RAM usage is {Usage_RAM}%.")

            print("Waiting 5 minutes before next possible alert...")
            time.sleep(300)

    time.sleep(2)

