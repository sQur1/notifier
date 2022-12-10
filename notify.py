from batteryloop import batteryLoop
from bluetoothloop import bluetoothLoop
from multiprocessing import Process

if __name__ == '__main__':
    proc1 = Process(target=batteryLoop)
    proc1.start()

    proc2 = Process(target=bluetoothLoop)
    proc2.start()