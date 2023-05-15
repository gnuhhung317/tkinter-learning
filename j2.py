from time import sleep
def main():
    with open("C:/Users/Acer/Downloads/input_for_project_2.txt", "r", encoding="utf-8") as file:
        file =file.read()
        file= file.split("\n\n")
    return file
data=main()
start=data[1]
print(start)
sleep(4)
questions=[]
score = 0
for i in range(1,11):
  cau=[data[3*i],data[3*i+1],data[3*i+2]]
  questions.append(cau)
  question=data[3*i]
  options=data[3*i+1]
  answer= data[3*i+2]
  real_ans=answer.split()[2]
  print(question)
  sleep(1)
  print(options)
  ans=input("Choose your answer: ")
  while ans not in list("abcABC"):
    ans=input("Choose your valid answer: ")
  if ans.lower()==real_ans.lower():
    score+=1
print(data[34])
sleep(4)
enddata=data[35::]
enddata=" ".join(enddata).split("\n")
for i in enddata:
  line=i.split()
  if score>=int(line[2]) and score <= int(line[3]):
    line=" ".join(line[4::])
    print(line)
sleep(7)
  