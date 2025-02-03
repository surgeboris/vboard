# vboard
Virtual keyboard for Linux that support wayland

First install pythone uinput library with
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
sudo pythone3 vboard.py
```



```bash
echo "KERNEL==\"uinput\", MODE=\"0660\", GROUP=\"$(id -gn)\", OPTIONS+=\"static_node=uinput\"" | sudo tee /usr/lib/udev/rules.d/99-uinput.rules`
```
