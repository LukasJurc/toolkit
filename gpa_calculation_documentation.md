## GPA calculation

### Calculate your GPA
 First, the input. Type at least a number from 3 to 10 in.
 
 ``
 def input_subjects():
    global number_answer
    counter = 3
    counter2 = 10
    print("Wie viele Fächer wollen sie eintragen?: ")
    number_answer = input()
    while int(counter)> int(number_answer) or int(counter2)< int(number_answer):
        print("""Der Durchschnitt kann nur mit mindestens 3 Fächern berechnet werden.
          Bitte geben sie eine Zahl zwischen 3-10 ein.""")
        number_answer = input()
 ``
 > It starts with 3 because calculating it with 2 points would be pointless. Also, you simply wouldn't need to know your GPA with 2 subjects
 
  
  ``
  spoints = input("Geben sie ihre Punktzahl ein: ")
        list_points.insert(0,int(spoints))
  ``
 > Let`s say you typed in "3" at the very beginning; this would mean you'll have to type the points from those 3 subjects in.
  
  ``
  def gpa():
    global list_points
    if len(list_points) ==3
        x1 = (list_points[0] + list_points[1] + list_points[2])/3
        print("Punktedurchschnitt:", round(x1,2))
 ``
 
  > The script now recalls the list with the points you typed in, in `global list_points`. Depending on how many you chose, the script sees it
    
   (list_points[0] + list_points[1] + list_points[2])/3
   > It automatically summarizes the 3 points you typed in and divides them with 3.
  
    `print("Punktedurchschnitt:", round(x1,2))`
    > The message afterwards is your GPA, rounded to 2 decimal places after the decimal.
  
  ``
  def gpamarks():
    global list_marks
    if len(list_marks) == 3:
        y1 = (list_marks[0] + list_marks[1] + list_marks[2])/3
        print("Notendurchschnitt:", round(y1,2))
 ``
 
  > The last step is to calculate the grades/marks average. The scipt recalls the list including your calculated marks.
  > `list_marks.insert(0, 1)` inserted them back then when you typed your points in, converted them to marks and sorted them in a list.
 
   `y1 = (list_marks[0] + list_marks[1] + list_marks[2])/3`
  > This part does the same thing as the scipt does with the points.
   It summarizes your marks and divides them through the amount of points you typed in.
 
   `print("Notendurchschnitt:", round(y1,2))`
   > The final message shown is your GPA for your marks, rounded to 2 decimal places after the decimal.
 
