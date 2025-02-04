# vboard
*A virtual keyboard for Linux with Wayland support.*


### **1. Install Dependencies**  
Install  `python-uinput steam-devices` packages using your package manager:  

**For Debian/Ubuntu-based distributions:**  
```bash
sudo apt install python3-uinput steam-devices
```

**For Fedora-based distributions:**  
```bash
sudo dnf install python3-uinput steam-devices
```


### **2. Download vboard**  
Retrieve the latest version of `vboard.py` using `wget`:  
```bash
wget https://raw.githubusercontent.com/mdev588/vboard/refs/heads/main/vboard.py
```



### **3. Run**  

```bash
python3 vboard.py
```


## Troubleshooting
if you get error 'no such device'. Make sure uinput kernel module is loded with
```bash
sudo modprobe uinput
```

to make sure it auto load on boot create file with
```bash
echo 'uinput' | sudo tee /etc/modules-load.d/module-uinput.conf
```
