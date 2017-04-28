#!/usr/bin/python

import sys
import time
import serial

def Mute(cmd_data='status') :
  send_cmd = GenCommand('power', 'status')
  return SendCommand(send_cmd)

def Volume(cmd_data='status') :
  send_cmd = GenCommand('volume', cmd_data)
  return SendCommand(send_cmd)

def Power(cmd_data='status') :
  send_cmd = GenCommand('power', cmd_data)
  return SendCommand(send_cmd)


def GenCommand(cmd1, cmd_data) :
  send_cmd = ""
  if(cmd1=="power") :
    if cmd_data=="on" :
      send_cmd = "ka 00 01\r"
    elif cmd_data=="off" :
      send_cmd = "ka 00 00\r"
    elif cmd_data=="status" :
      send_cmd = "ka 00 ff\r"
    else :
      return None
  elif(cmd1=="volume") :
    if cmd_data=="status" :
      send_cmd = "kf 00 ff\r"
    elif isNumber(cmd_data) :
      vol = int(cmd_data)
      if vol<0 or vol>25 :
        print "wrong volume."
        return None
      str_vol = "%02x" % vol
      send_cmd = "kf 00 " + str_vol + "\r"
    else :
        return None
  elif(cmd1=="mute") :
    if cmd_data=="on" :
     send_cmd = "ke 00 00\r"
    elif cmd_data=="off" :
      send_cmd = "ke 00 01\r"
    elif cmd_data=="status" :
      send_cmd = "ke 00 ff\r"
    else :
      return None
  return send_cmd

def parse_recv(resp) :
  row = resp.split(' ')
  if len(row) < 3 :
    print "error response : " + resp
    return None
  elif resp[-1] != "x" :
    print "error response : " + resp
    return None
  elif row[2][0:2] != "OK" :
    print "error response from tv : " + resp
    return None

  r1 = ""
  r2 = ""
  if(row[0]=="a") : # power
    r1 = "power"
    if row[2][3]=="0" :
      r2 = "off"
    elif row[2][3]=="1" :
      r2 = "on"
  elif(row[0]=="e") : # mute
    r1 = "mute"
    if row[2][3]=="1" :
      r2 = "on"
    elif row[2][3]=="0" :
      r2 = "off"
  elif(row[0]=="f") : # volume
    r1 = "volume"
    r2 = int(row[2][3:4], 16)
  else :
    #print "other response : " + resp
    #return None
    r1 = "other"
    r2 = resp
  return {'cmd':r1, 'status':r2}


def SendCommand(send_cmd) :
  ser = serial.Serial()
  ser.port = "/dev/ttyUSB0"
  ser.baudrate = 9600
  ser.bytesize = serial.EIGHTBITS #number of bits per bytes
  ser.parity = serial.PARITY_NONE #set parity check: no parity
  ser.stopbits = serial.STOPBITS_ONE #number of stop bits
  #ser.timeout = None          #block read
  #ser.timeout = 0            #non-block read
  ser.timeout = 0.5              #timeout block read
  ser.xonxoff = False     #disable software flow control
  ser.rtscts = False     #disable hardware (RTS/CTS) flow control
  ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
  ser.writeTimeout = 1     #timeout for write

  try: 
    ser.open()
  except Exception, e:
    print "error open serial port: " + str(e)
    return None

  resp_val = None
  if ser.isOpen():
    try:
      ser.flushInput()  #flush input buffer, discarding all its contents
      ser.flushOutput() #flush output buffer, aborting current output 
                        #and discard all that is in buffer
      #write data
      ser.write(send_cmd)
      #print("write data: " + send_cmd)
    
      numOfLines = 0
      numOfTry = 0
      while True:
        time.sleep(0.01)  #give the serial port sometime to receive the data
        resp = ser.readline()
        if len(resp) < 1 :
          continue
        #print("read data: " + resp)
        resp_val = parse_recv(resp)
        #print "resp : " + resp + "\n"
        numOfLines = numOfLines + 1
      
        if (numOfLines >= 1):
          break
        if (numOfTry>10) :
          break
        numOfTry = numOfTry + 1
     
      ser.close()
    except Exception, e1:
      print "error communicating...: " + str(e1)
      return None
  else:
    print "cannot open serial port "
    return None
  return resp_val

    
