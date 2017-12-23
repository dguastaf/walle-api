from subprocess import call

def sendCommand(device, command, num_times=1):
    call("irsend SEND_ONCE -# "+ str(num_times) + " " + device + " " + command, shell=True)