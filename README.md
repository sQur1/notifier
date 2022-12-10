# MacOS Notifier
## Battery and Bluetooth notifications for MacOS laptops

While running the script:
    1. You will receive a notification at 1% battery to plug in your laptop and the same at 100% to unplug it.
    2. You will receive a notification if Bluetooth is On and is NOT connected to a device.
    
###### Those 2 notifications are persistent so long as the conditions are not met. E.g.: If you don't unplug your laptop at 100%, it will nudge you until you do.

Installation:

    1. Clone repo and unzip
    2. Open Automator
        2.A. Click New
        2.B. Choose Workflow
        2.C. Double-click "Run Shell Script"
        2.D. Paste the following:
            cd "path/to/files"
            python3 notify.py
        2.E. Click File/Save and Save the script as a .app (File Format)
    3. Under System Settings/General/Login Items add the .app script you just saved
