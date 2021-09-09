from tkinter import *
win= Tk()
win.geometry("600x450")

def main_fun():
    ipaddress = ip.get()
    subnet=int(sub.get())
    iplist = list(ipaddress.split("."))
    maskaddress = str("1"*subnet+"0"*(32-subnet)) 
    netmask1 = [int(maskaddress[i:i+8],2) for i in range(0,len(maskaddress),8)]
    #networkaddress
    subnet_mask_ipv4 =".".join(map(str, netmask1))
    network_address= [int(iplist[i])&netmask1[i] for i in range(4)]
    n =".".join(map(str, network_address))
    #broad cast
    inverted_subnet = str("0"*subnet+"1"*(32-subnet))
    inverted = [int(inverted_subnet[i:i+8],2) for i in range(0,len(inverted_subnet),8)]
    broadcast_address= [network_address[i]|inverted[i] for i in range(4)]
    b =".".join(map(str, broadcast_address))
    broadcast_lst = []
    for i in broadcast_address:
        broadcast_lst.append(i)
    #no of ip 2^n
    no_of_ip= pow(2, 32-subnet)
    usable = no_of_ip - 2
    network_address[3] = network_address[3] + 1
    start_range = ".".join(map(str, network_address))
    broadcast_lst[3] = int(broadcast_lst[3]) - 1
    end_range = ".".join(map(str, broadcast_lst))
    iprange = start_range + " - " + end_range
    #to print     
    Label(win, text="IP address").grid(row=31,column=1)
    Label(win, text=ipaddress).grid(row=31,column=2)
    Label(win, text="Subnet mask").grid(row=32,column=1)
    Label(win, text=subnet_mask_ipv4).grid(row=32,column=2)
    Label(win, text="Network address").grid(row=33,column=1)
    Label(win, text=n).grid(row=33,column=2)
    Label(win, text="Broadcast address").grid(row=34,column=1)
    Label(win, text=b).grid(row=34,column=2)
    Label(win, text="Available IP addresses:").grid(row=35,column=1)
    Label(win, text=usable).grid(row=35,column=2)
    Label(win, text="Range ").grid(row=36,column=1)
    Label(win, text=iprange).grid(row=36,column=2)

def clear():
	ip.set('')
    
	sub.set('')	
#main 
win.title('Subnet Calculator')
Label(win,text="Subnet calculator      ").grid(row=1,column=0)
Label(win, text="Enter the ip address  ").grid(row=10,column=0)
Label(win, text="Enter the subnetmask  ").grid(row=11,column=0)
ip = StringVar(win)
sub=StringVar(win)
ip_addr = Entry(win, textvariable=ip).grid(row=10,column=1)
sub_net_mask = Entry(win,textvariable=sub).grid(row=11,column=1)
Label(win,text="").grid(row=12,column=0)
Button(win,text="Calculate",command=main_fun).grid(row=20,column=1)
Button(win,text="clear",command=clear).grid(row=20,column=3)
win.mainloop()