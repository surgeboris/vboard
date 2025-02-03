# vboard
*A virtual keyboard for Linux with Wayland support.*


### **1. Install Dependencies**  
Install the `python-uinput` library using your package manager:  

**For Debian/Ubuntu-based distributions:**  
```bash
sudo apt install python-uinput
```

**For Fedora-based distributions:**  
```bash
sudo dnf install python-uinput
```
---

### **2. Download vboard**  
Retrieve the latest version of `vboard.py` using `wget`:  
```bash
wget https://raw.githubusercontent.com/mdev588/vboard/refs/heads/main/vboard.py
```

---

### **3. Run vboard**  
Run the application using:  
```bash
sudo python3 vboard.py
```


---
However, **running as root is not recommended**. To run `vboard` without `sudo`, follow the next step.


## **Running Without sudo**  

To allow non-root execution, add a **udev rule**:  
```bash
echo "KERNEL==\"uinput\", MODE=\"0660\", GROUP=\"$(id -gn)\", OPTIONS+=\"static_node=uinput\"" | sudo tee /usr/lib/udev/rules.d/99-uinput.rules
```
Then **reboot your system**.

After rebooting, you should be able to run `vboard` without `sudo`:  
```bash
python3 vboard.py
```

---
