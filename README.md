# vboard
*A virtual keyboard for Linux with Wayland support.*


### **1. Install Dependencies**  
Install the `python-uinput` library using your package manager:  

**For Debian/Ubuntu-based distributions:**  
```bash
sudo apt install python3-uinput
```

**For Fedora-based distributions:**  
```bash
sudo dnf install python3-uinput
```
---

### **2. Download vboard**  
Retrieve the latest version of `vboard.py` using `wget`:  
```bash
wget https://raw.githubusercontent.com/mdev588/vboard/refs/heads/main/vboard.py
```

---

## **Running Without sudo**  

To allow non-root execution, add a **udev rule**:  
```bash
echo "KERNEL==\"uinput\", MODE=\"0660\", GROUP=\"$(id -gn)\", OPTIONS+=\"static_node=uinput\"" | sudo tee /usr/lib/udev/rules.d/99-uinput.rules
```
Then 
```bash
sudo udevadm control --reload-rules && sudo udevadm trigger
```

Now you should be able to run `vboard` without `sudo`:  
```bash
python3 vboard.py
```

---
