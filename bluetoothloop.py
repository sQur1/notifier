import subprocess
import time
import signal

def bluetoothLoop():
    while True:
        time.sleep(5)
        sound = "Blow"
        title = "TURN OFF BLUETOOTH"
        message = "-------------------------"
        bluetooth = subprocess.Popen(['''system_profiler SPBluetoothDataType'''], stdout=subprocess.PIPE, shell=True, encoding="utf", errors="ignore")
        bluetooth_state = bluetooth.communicate()
        if "State: On" in bluetooth_state[0] and not "  Connected:" in bluetooth_state[0]:
            bluetooth.send_signal(signal.SIGINT)
            time.sleep(10)
            bluetooth = subprocess.Popen(['''system_profiler SPBluetoothDataType'''], stdout=subprocess.PIPE, shell=True, encoding="utf", errors="ignore")
            bluetooth_state = bluetooth.communicate()
            if "State: On" in bluetooth_state[0] and not "  Connected:" in bluetooth_state:
                bluetooth.send_signal(signal.SIGINT)
                command = f'''
                osascript -e 'display notification "{message}" with title "{title}" sound name "{sound}"'
                '''
                notify = subprocess.Popen(command, shell=True)
                time.sleep(20)
                notify.send_signal(signal.SIGINT)
    return notify