from admin2 import Admin2

cafe_menus1 = [
    {
        "name" : "아메리카노",
        "price" : 2700,
        "time" : 60
    },
    {
        "name" : "카페라떼",
        "price" : 3200,
        "time" : 60
    }
]


def store() :
    print("⚠️ALL MENU⚠️")
    for menu in cafe_menus1 :
        print(menu["name"])
        print(menu["price"])
        print(menu["time"])
        print("☕️☕️☕️☕️☕️☕️☕️☕️☕️☕️☕️☕️☕️☕️☕️")

    print("다음 중 원하는 탭을 선택해주세요.")
    print("1. 음료주문하기")
    print("2. 관리자모드")
    print("99. 종료하기")

    answer = int(input(">> "))

    if(answer == 1) :
        print("음료주문하기")
    elif(answer == 2) :
        print("관리자모드")
        ans = Admin2.selectMenu()
        if(ans == 1) :
            prev_data = Admin2.addMenu()

            cafe_menus1.append(prev_data)
            print("새로운 메뉴가 추가되었습니다.")

            store()
        else :
            print("‼️존재하지 않는 탭을 선택하셨습니다. 다시 선택해주세요.")
            store()

    elif(answer == 99) :
        print("종료하기")
    else :
        print("‼️존재하지 않는 탭을 선택하셨습니다. 다시 선택해주세요.")
        store()
store()



