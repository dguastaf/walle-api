from command import sendCommand

DEVICE_NAME = "samsung"

# Command constants
COMMAND_POWER = "KEY_POWER"
COMMAND_VOL_UP = "KEY_VOLUMEUP"
COMMAND_VOL_DOWN = "KEY_VOLUMEDOWN"

# Action constants
ACTION_POWER = "power"
ACTION_VOL_UP = "volume_up"
ACTION_VOL_DOWN = "volume_down"


def handleAction(actionName):
  if actionName == ACTION_POWER:
    __commandPower()
  elif actionName == ACTION_VOL_UP:
    __commandVolUp()
  elif actionName == ACTION_VOL_DOWN:
    __commandVolDown()

def __commandPower():
  sendCommand(DEVICE_NAME, COMMAND_POWER, 2)

def __commandVolUp():
  sendCommand(DEVICE_NAME, COMMAND_VOL_UP, 2)

def __commandVolDown():
  sendCommand(DEVICE_NAME, COMMAND_VOL_DOWN, 2)
