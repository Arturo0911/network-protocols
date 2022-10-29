#!/usr/bin/python3

from pwn import *
import socket
import threading


class Message:
    def __init__(self, device_id: int) -> None:
        self.device_id = device_id


class Commands:
    def __init__(self) -> None:
        self.TYPE_CUSTOM = "custom"
        self.TYPE_IDENTIFICATION = "deviceIdentification"
        self.TYPE_POSITION_SINGLE = "positionSingle"
        self.TYPE_POSITION_PERIODIC = "positionPeriodic"
        self.TYPE_POSITION_STOP = "positionStop"
        self.TYPE_ENGINE_STOP = "engineStop"
        self.TYPE_ENGINE_RESUME = "engineResume"
        self.TYPE_ALARM_ARM = "alarmArm"
        self.TYPE_ALARM_DISARM = "alarmDisarm"
        self.TYPE_ALARM_DISMISS = "alarmDismiss"
        self.TYPE_SET_TIMEZONE = "setTimezone"
        self.TYPE_REQUEST_PHOTO = "requestPhoto"
        self.TYPE_POWER_OFF = "powerOff"
        self.TYPE_REBOOT_DEVICE = "rebootDevice"
        self.TYPE_FACTORY_RESET = "factoryReset"
        self.TYPE_SEND_SMS = "sendSms"
        self.TYPE_SEND_USSD = "sendUssd"
        self.TYPE_SOS_NUMBER = "sosNumber"
        self.TYPE_SILENCE_TIME = "silenceTime"
        self.TYPE_SET_PHONEBOOK = "setPhonebook"
        self.TYPE_MESSAGE = "message"
        self.TYPE_VOICE_MESSAGE = "voiceMessage"
        self.TYPE_OUTPUT_CONTROL = "outputControl"
        self.TYPE_VOICE_MONITORING = "voiceMonitoring"
        self.TYPE_SET_AGPS = "setAgps"
        self.TYPE_SET_INDICATOR = "setIndicator"
        self.TYPE_CONFIGURATION = "configuration"
        self.TYPE_GET_VERSION = "getVersion"
        self.TYPE_FIRMWARE_UPDATE = "firmwareUpdate"
        self.TYPE_SET_CONNECTION = "setConnection"
        self.TYPE_SET_ODOMETER = "setOdometer"
        self.TYPE_GET_MODEM_STATUS = "getModemStatus"
        self.TYPE_GET_DEVICE_STATUS = "getDeviceStatus"
        self.TYPE_SET_SPEED_LIMIT = "setSpeedLimit"
        self.TYPE_MODE_POWER_SAVING = "modePowerSaving"
        self.TYPE_MODE_DEEP_SLEEP = "modeDeepSleep"
        self.TYPE_ALARM_GEOFENCE = "movementAlarm"
        self.TYPE_ALARM_BATTERY = "alarmBattery"
        self.TYPE_ALARM_SOS = "alarmSos"
        self.TYPE_ALARM_REMOVE = "alarmRemove"
        self.TYPE_ALARM_CLOCK = "alarmClock"
        self.TYPE_ALARM_SPEED = "alarmSpeed"
        self.TYPE_ALARM_FALL = "alarmFall"
        self.TYPE_ALARM_VIBRATION = "alarmVibration"
        self.KEY_UNIQUE_ID = "uniqueId"
        self.KEY_FREQUENCY = "frequency"
        self.KEY_LANGUAGE = "language"
        self.KEY_TIMEZONE = "timezone"
        self.KEY_DEVICE_PASSWORD = "devicePassword"
        self.KEY_RADIUS = "radius"
        self.KEY_MESSAGE = "message"
        self.KEY_ENABLE = "enable"
        self.KEY_DATA = "data"
        self.KEY_INDEX = "index"
        self.KEY_PHONE = "phone"
        self.KEY_SERVER = "server"
        self.KEY_PORT = "port"


def sending_commands():
    pass


def decoding_messages():
    command = b'##,imei:868166051864296,A;'
    command_encoded = '23232c696d65693a3836383136363035313836343239362c413b0a'

    return command_encoded






def handle_client(socket_client: socket.socket) -> None:
    with socket_client as sock:
        request = sock.recv(2048)
        log.info(f"Received from {str(request.decode('utf-8'))}")
        sock.send(b'23232c696d65693a3836383136363035313836343239362c413b0a')


def main():
    try:
        log.progress("Starting socket connection...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 5001))
        sock.listen(5)
        while True:
            client, address = sock.accept()
            log.info(f'Accepted connection from {str(address[0])} {str(address[1])}')
            client_thread = threading.Thread(target=handle_client, args=(client,))
            client_thread.start()
    except Exception as e:
        print(str(e))
        log.failure("Error in the connection")
        exit(1)
    except KeyboardInterrupt:
        log.info("Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
