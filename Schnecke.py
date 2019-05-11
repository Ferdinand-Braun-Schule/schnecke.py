import random			#2 dictionary
import numpy


def FalleVergraben():				#def kommt immer vor dem Programm
	Falle = random.randint(0,26)	#0-26 = 27 Zahlen
	return(Falle)					#Ausgabe
	
def Abfrage_Feld():
        Feld = -1						#Wert der nicht wahr ist also der nicht zwischen 1-27
	
    while Feld<1 or Feld>6: #Würfel gibt es 6 Zahlen
		try:
			Feld = int(input("Bitte geben sie die gewürfelte Zahl ein: "))
		except Value Error:
			print("Das war keine Zahl von 1-6! Bitte nochmals versuchen ...")
	return(Feld) 			#Überprüfung des Feldes
	
def Auswahl_Antwort():
	Antwort: random.randint(0,26) #sucht einKommentar aus welche er ausgibt randomAntworten = [
	Antworten = ['Nur weiter so, bald hast Dus geschafft!', 'Pech, aber einmal wirds schon klappen!', 'Lass Dich nicht so verdriessen!','Versuchs noch einmal!','Als Schatzgräber muss man Ausdauer haben!', 'Du übernimmst Dich noch, mach mal eine Pause!','Ich glaube, Du schaffst es doch nicht allein!']
	return(Antworten[Antwort])
		
i=0 					#Falle vergraben, Funktionen starten hier sowie das Programm
Falle = Fallegelegt()
print("Die Falle ist gelegt")
print(Falle)
Feld = numpy.full ((27),False)
print("Das Feld besteht aus 27 Feldern!")

abbruch=0
while abbruch==0:
	Feld = Abfrage_Feld()
	i=i+1					#zählt die Versuche mit
	print (Feld)
	if ((Schatz[1] == Feld[1])):  		# wo ist der Schatz 
        print("Du hast die Falle gefunden! Vielen Dank für das Spiel")
        i=i-1									# ist der wert wieder auf 0 und ist beendet
        print("Du hast {}\t Versuche gebraucht!".format(i))
        abbruch=1
											# Schatz nicht gefunden
    elif (Feld[Feld[0],Feld[1]]==True):
        print("Hier hast Du bereits gegraben!")
    else:    
        Feld[Feld[0],Feld[1]]=True
        print(Auswahl_Antwort())	
