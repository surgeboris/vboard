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

**For arch-based distributions:**  
```bash
yay -S python-uinput steam-devices
```


### **2. Download vboard**  
Retrieve the latest version of `vboard.py` using `wget`:  
```bash
wget https://github.com/mdev588/vboard/releases/download/v1.12/vboard.py
```



### **3. Run**  

```bash
python3 vboard.py
```


## Troubleshooting
### 1. Error: 'no such device'
 Make sure uinput kernel module is loded with
```bash
sudo modprobe uinput
```

to make sure it auto load on boot create file with
```bash
echo 'uinput' | sudo tee /etc/modules-load.d/module-uinput.conf
```
---
### 2. Error: 'Permission Denied'
Reload udev rules with
```bash
sudo udevadm control --reload-rules && sudo udevadm trigger
```
---
### 3. Error: 'steam-devices package not found'. Fedora only
Make sure the RPM Fusion repository is enabled. You can follow the guide here:
https://rpmfusion.org/Configuration
