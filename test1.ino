const int intA = 8;
const int intB = 9;
const int enA = 10;
String r;
char c;
int flag = 0;

#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);



void setup()
{  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.print("Sum is ");
  
}

void loop()
{
  if(Serial.available()){
    int x = Serial.read();
    if(x=='A'){
    if(flag == 0){
      flag =1;
      delay(2650);
    }
    digitalWrite(intA,HIGH);
    digitalWrite(intB,LOW);
    analogWrite(enA,120);
    delay(650);
    digitalWrite(intA,LOW);
    digitalWrite(intB,LOW);
    delay(2010);
  }
  else if(x=='B'){
    digitalWrite(intA,LOW);
    digitalWrite(intB,LOW);
    
    lcd.setCursor(0,1);
    while(Serial.available())
    {
      delay(50);
      if(Serial.available() > 0){
          c = Serial.read();
          r+=c;
          Serial.flush();
    }
   // Serial.println(r);
    lcd.print(c);
    Serial.flush();
  }
  }
  

  }
  else{
    digitalWrite(intA,LOW);
    digitalWrite(intB,LOW);
  }
}
