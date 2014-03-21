void setup() {
  Serial.begin(9600);
//  system("/etc/init.d/networking restart");
//  if(!SD.exists("playerdata"))
//  {
//    dataFile = SD.open("playerdata", FILE_WRITE);
//    dataFile.close();
//  }
}

void loop() {
//  system("touch /afile");
//  system("echo -n \"this is a string\" /afile");
//  Serial.print(system("cat /afile"));
  int rfidVal = getRFIDVal();
  if(rfidVal != 0)
  {
//    system("/etc/init.d/networking restart");
    while() {
      String command = String("python /home/root/send_string.py ") + String("192.168.1.229"/*dataFile.read()*/) + rfidVal;
      char cmd[command.length() + 1];
      command.toCharArray(cmd, command.length());
      system(cmd);
    }
  }
}

int getRFIDVal() {
  return 1337; //use real RFID code later
}
