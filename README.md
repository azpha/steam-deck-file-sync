# steam-deck-file-sync
This is a simple Python script to sync files to your PC from your Steam Deck. I use it to sync Decky Recorder clips to my PC to be ingested by Medal.

# Server Setup
You need [Python](https://python.org). Just need to install Flask and you're good!

I run this at startup on my Windows machine. You can configure the port & folder it runs on/stores files in by modifying server.py.

# Client Setup
Install [Python](https://python.org) on your Steam Deck via Konsole. Run `pip install requests`.

Ensure you change `local_ip` in client.py to the IP address of your primary machine. You can also change the default port (9999) by modifying the `port` variable.

To get this to run at the time of system startup so it's running even in gaming mode, I have a systemd file like so;

```
[Unit]
Description=SteamDeckFileSync
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/deck/Desktop/FileSync.py
Restart=always
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

..change `ExecStart` to match the name of the file you have. After that, just run; 
```
systemctl --user enable SteamDeckFileSync.service && systemctl --user start SteamDeckFileSync.service
```
and it should start automatically! If it doesn't, I use the `Bash Shortcuts` Decky plugin to run the above and start it manually.

