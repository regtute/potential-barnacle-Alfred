import socket
import pyperclip
# 获取主机名
hostname = socket.gethostname()

# 获取本地IP地址
ip_address = socket.gethostbyname(hostname)

pyperclip.copy(ip_address)
