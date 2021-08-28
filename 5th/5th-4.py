def changeScoreToGrade(score):
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

def displayEvaluation(scoreMean):
    if scoreMean == 4.5:
        evaluation = "Perfect"
    elif scoreMean < 4.5 and scoreMean >= 4.0:
        evaluation = "Excellent"
    elif scoreMean < 4.0 and scoreMean >= 3.0:
        evaluation = "Good"
    elif scoreMean < 3.0 and scoreMean >= 2.0:
        evaluation = "Satisfactory"
    else:
        evaluation = "Bad"

    return print(evaluation)


class GradeCalculator():
    def __init__(self):
        self.data = list()
        self.majorGrade = list()
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

    def calculGrade(self):
        #전공학점
        for i in range(len(self.data)):
            if self.data[i][1] ==  'Y':
                self.majorGrade.append(changeScoreToGrade(self.data[i][0]))
            else:
                pass;
        #교양학점
        for i in range(len(self.data)):
            if self.data[i][1] ==  'N':
                self.noMajorGrade.append(changeScoreToGrade(self.data[i][0]))
            else:
                pass

    def displayGrade(self):
        print("전체 평균 :", round(((sum(self.majorGrade) + sum(self.noMajorGrade))/len(self.data)),3))
        
        print("전공 평균 :", round(sum(self.majorGrade)/len(self.majorGrade), 3))

        print("교양 평균 :", round(sum(self.noMajorGrade)/len(self.noMajorGrade), 3))


class GradeCalculator2(GradeCalculator):
    def displayGrade(self):
        allMean =  round(((sum(self.majorGrade) + sum(self.noMajorGrade))/len(self.data)), 1)
        print("전체 평균 :", allMean, end=" ")
        displayEvaluation(allMean)
        
        majorMean = round(sum(self.majorGrade)/len(self.majorGrade), 1)
        print("전공 평균 :", majorMean, end=" ")
        displayEvaluation(majorMean)

        noMajorMean = round(sum(self.noMajorGrade)/len(self.noMajorGrade), 1)
        print("교양 평균 :", noMajorMean, end=" ")
        displayEvaluation(noMajorMean)

        for i in range(len(self.data)):
            if self.data[i][0] == '0':
                print("다음에도 뵈어요, 교수님^^")
                break
            else:
                pass;


a = GradeCalculator2()
a.getData()
a.calculGrade()

a.displayGrade()