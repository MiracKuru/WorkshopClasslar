#Sınıflar-- claslar
#constructor
#initalize
class Human:
    name= "Halit"
    #constructor
    #initalize
    def __init__(self,name):
        self.name=name
        print("Bir human instance'ı üretildi")
    
    def __str__(self)
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    


    def talk(self,sentence):
        name="Ercan"
        print(f"{self.name}: {sentence}")
        
    def walk(self):
        print(f"{self.name}: is walking")
    
#Instance-- örnek
human1=Human("Enes")

human1.talk("Merhaba")
human1.walk()
print(human1)

human2= Human("Halit")

human2.talk("Selam")
human2.walk()
print(human2)

 
 