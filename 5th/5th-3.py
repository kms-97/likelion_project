def changeGrade(score):
    score = int(score)
    if score >= 95:
        grade = float(4.5)
    elif score >= 90:
        grade = float(4.0)
    elif score >= 85:
        grade = float(3.5)
    elif score >= 80:
        grade = float(3.0)
    elif score >= 75:
        grade = float(2.5)
    elif score >= 70:
        grade = float(2.0)
    elif score >= 65:
        grade = float(1.5)
    elif score >= 60:
        grade = float(1.0)
    else:
        grade = int(0)
    
    return grade


class gradeCalculator():
    def __init__(self):
        self.data = list()
        self.MajorGrade = list()
        self.noMajorGrade = list()

    def getData(self):
        while True:
            [score, isMajor] = input("점수와 전공 여부를 입력해 주십시오 (ex. 95 Y / 80 N) *0 0로 입력을 중지합니다. : ").split(" ")
            if str(isMajor) == "0" and score == '0':
                break
            elif int(score) >= 0 and int(score) <= 100 and score.isdecimal and (isMajor == 'Y' or isMajor == 'N'):
                self.data.append([score, isMajor])
            else:
                print("다시 입력하여 주십시오.")

    def calGrade(self):
        #전공학점
        for i in range(len(self.data)):
            if self.data[i][1] ==  'Y':
                self.MajorGrade.append(changeGrade(self.data[i][0]))
            else:
                pass;
        #교양학점
        for i in range(len(self.data)):
            if self.data[i][1] ==  'N':
                self.noMajorGrade.append(changeGrade(self.data[i][0]))
            else:
                pass

    def disGrade(self):
        print("전체 평균 :", round(((sum(self.MajorGrade) + sum(self.noMajorGrade))/len(self.data)),3))
        
        print("전공 평균 :", round(sum(self.MajorGrade)/len(self.MajorGrade), 3))

        print("교양 평균 :", round(sum(self.noMajorGrade)/len(self.noMajorGrade), 3))


a = gradeCalculator()
a.getData()
a.calGrade()
a.disGrade()
