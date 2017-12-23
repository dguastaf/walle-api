from command import sendCommand

deviceName = "tv"
powerCommand = "KEY_POWER"

def handleAction(actionName):
  if actionName == "power":
    __command_power()

def __command_power():
  sendCommand(deviceName, powerCommand, 2)

