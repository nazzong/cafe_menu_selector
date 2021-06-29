

class Admin2 :

    def selectMenu() :
        print("다음중 원하는 탭을 선택해주세요.")
        print("1. 메뉴추가하기")

        answer = int(input(">>"))

        if(answer == 1) :
            return answer
        else :
            print("‼️존재하지 않는 탭을 선택하셨습니다. 다시 선택해주세요.")
            Admin.selectMenu()

    def addMenu() :
        name = input("메뉴명 : ")
        price = int(input("금액(숫자) : "))
        time = int(input("소요시간(숫자) : "))

        prev_data = {
            "name" : name,
            "price" : price,
            "time" : time
        }
        return prev_data

        