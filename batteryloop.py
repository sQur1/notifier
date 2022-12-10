import subprocess
import time
import signal

def batteryLoop():
    while True:
        time.sleep(5)
        power_state_proc = subprocess.Popen(["pmset -g ps"], shell=True, stdout=subprocess.PIPE, encoding="utf", errors="ignore")
        power_state = power_state_proc.communicate()[0]
        sound = "Blow"
        bat_level_proc = subprocess.Popen(['''pmset -g batt | grep -Eo "\d+%" | cut -d% -f1'''], shell=True, stdout=subprocess.PIPE, encoding="utf", errors="ignore")
        bat_level = bat_level_proc.communicate()
        bat_level = int((str(bat_level[0]).strip('\n')))
        if bat_level == 1 and "discharging" in power_state:
            command = f'''osascript -e 'display notification "Plug in the power cable" with title "LOW BATTERY" sound name "{sound}"'
            '''
            notify = subprocess.Popen(command, shell=True)
            time.sleep(30)
            notify.send_signal(signal.SIGINT)
        elif bat_level == 100 and (" charging" in power_state or "finishing charge" in power_state or "charged" in power_state):
            command = f'''osascript -e 'display notification "Unplug the power cable" with title "BATTERY FULL" sound name "{sound}"'
            '''
            notify = subprocess.Popen(command, shell=True)
            time.sleep(30)
            notify.send_signal(signal.SIGINT)
        power_state_proc.send_signal(signal.SIGINT)
        bat_level_proc.send_signal(signal.SIGINT)
    return notify