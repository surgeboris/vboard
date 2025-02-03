# vboard
Virtual keyboard for Linux that support wayland

First install python uinput library with
```bash
sudo apt install python-uinput
```
or 
```bash
sudo dnf install python-uinput
```
Then download app

```bash
wget https://raw.githubusercontent.com/mdev588/vboard/refs/heads/main/vboard.py
```
Then you can run with 
```bash
sudo python3 vboard.py
```

it is recommanded to run without sudo so you have to add a udev rule with this command then reboot

run as user
```bash
echo "KERNEL==\"uinput\", MODE=\"0660\", GROUP=\"$(id -gn)\", OPTIONS+=\"static_node=uinput\"" | sudo tee /usr/lib/udev/rules.d/99-uinput.rules`
```
then you should able to run with
```bash
python3 vboard
