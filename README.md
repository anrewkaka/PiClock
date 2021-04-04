# Photo Frame

## Installation

1. Ensure valid for using kivy

   ```shell
   sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
      libgstreamer1.0-dev \
      gstreamer1.0-plugins-{bad,base,good,ugly} \
      gstreamer1.0-{omx,alsa} libmtdev-dev \
      xclip xsel libjpeg-dev
   sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
   ```

1. Virtual Env

   ```shell
   python3 -m pip install --upgrade pip setuptools virtualenv
   ```

1. Create venv

   ```shell
   python3 -m virtualenv kivy_venv
   ```

1. Active venv

   ```shell
   . kivy_venv/bin/activate
   ```

1. Install kivy

   ```shell
   python3 -m pip install kivy[base] kivy_examples
   ```

1. Install dependencies

   ```shell
   pip3 install -r requirement.txt
   ```

1. Change picture folder

   Find the row bellow in the file `main.py` and change to the real path of picutre directory

   ```python
   path = 'asset' #TODO: change directory path
   ```

1. Start application

   ```shell
   python main.py
   ```

## Start on boot with Raspberry PI

```shell
$ cat /etc/systemd/system/photo_frame_trigger.service
[Unit]
Description=Start the Photo Frame app
After=multi-user.target

[Service]
Environment=DISPLAY=:0
Type=idle
User=pi
WorkingDirectory=/home/pi
Restart=always
RestartSec=2
ExecStart=/home/pi/photo_frame_clock/kivy_venv/bin/python /home/pi/photo_frame_clock/main.py
NoNewPrivileges=true
StandardOutput=syslog
StandardError=syslog

[Install]
WantedBy=multi-user.target
```

```shell
$ systemctl daemon-reload
$ systemctl enable photo_frame_trigger.service
$ sudo reboot
```