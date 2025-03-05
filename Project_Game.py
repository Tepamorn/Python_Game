import datetime
import random





# จำนวนเงินเริ่มต้น
money = 1000
# menu หลัก


def mainmenu():
    print("\n[เมนูหลัก]")
    print("1.ตี๋วเครื่องบิน")
    print("2.เล่นเกมส์")
    print("0.ออกจากโปรแกรม\n")


# เที่ยวนรก
def menu_trip(name):
    global money
    data = {
        1: {'Name': 'ท่าอากาศยานสุวรรณภูมิ (BKK)', 'Price': 200},
        2: {'Name': 'ท่าอากาศยานดอนเมือง (DMK)', 'Price': 100},
        3: {'Name': 'ท่าอากาศยานแม่ฟ้าหลวง เชียงราย (CEI)', 'Price': 100},
        4: {'Name': 'ท่าอากาศยานแม่ฮ่องสอน (HGN) ', 'Price': 100}, 
        5: {'Name': 'ท่าอากาศยานเชียงใหม่ (CNX))', 'Price': 100}, 
        6: {'Name': 'ท่าอากาศยานขอนแก่น (KKC)', 'Price': 100}, 
        7: {'Name': 'ท่าอากาศยานนานาชาติอุบลราชธานี (UBP)', 'Price': 100}, 
        8: {'Name': 'ท่าอากาศยานภูเก็ต (HKT)', 'Price': 100}, 
        9: {'Name': 'ท่าอากาศยานนานาชาติกระบี่ (KBV)', 'Price': 100}, 
        10: {'Name': 'ท่าอากาศยานนานาชาติหาดใหญ่ (HDY)', 'Price': 100}
    }
    j = 1
    print(f'สวัสดี {name} คุณมีเงิน {money}')
    for i in data.keys():
        print(j, ".", data[i]['Name'], data[i]['Price'])
        j += 1
    choose = int(input('ไปเที่ยวที่ : '))
    d_name = data[choose]['Name']
    price = data[choose]['Price']
    money = money - price
    print(f'คุณไป {d_name} ด้วยราคา {price} ตอนนี้คุณเหลือเงิน', money)
    return fail(money)

# เกม


def menu_game():
    global money
    while True:
        print("\nอยากเล่นเกมอะไรหรอครับ")
        print("1.เป่ายิ่งฉุบ")
        print("2.ทายเลข")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม\n")
        try:
            work = int(input("อยากเล่นเกมไหนครับ :"))
        except:
            print("\nระบบใส่ได้แค่ตัวเลขเท่านั้น")
            return menu_game()
        if work == 1:
            return pao()
        elif work == 2:
            return tai()
        elif work == 9:
            return 9
        elif work == 0:
            return 0
        else:
            print("ไม่รู้จัก:", work)


def fail(money):
    if money <= 0:
        print("\nล้มละลาย")
        farewell(name)
        return exit()


def menu_pao():
    print("\n[เป่ายิ่งฉุบ]")
    print("1.ค้อน")
    print("2.กระดาษ")
    print("3.กรรไกร")
    print("9.กลับเมนูเกม")
    print("0.ออกเกม\n")


def pao():
    global money
    w = 1
    while w != 0:
        menu_pao()
        k = random.randint(1, 3)
        try:
            gu = int(input("คุณจะออกอะไร:"))
        except:
            print("\nระบบใส่ได้แค่ตัวเลขเท่านั้น")
            return pao()
        if gu == 0:
            farewell(name)
            return exit()
        elif gu == 9:
            return menu_game()
        else:
            print("ยอดเงินคงเหลือ", money)

            try:
                derm = int(input("เดิมพัน:"))
            except:
                print("\nระบบใส่ได้แค่ตัวเลขเท่านั้น")
                return pao()
            if derm > money:
                print("เงินเดิมพันไม่สามารถมากกว่าเงินที่เหลือ")
                return pao()
            if gu == 1 and k == 3:
                print("\nบอทออกกรรไกรคุณชนะ")
                money = money + derm
                print("ยอดเงินคงเหลือ", money)
            elif gu == 2 and k == 1:
                print("\nบอทออกค้อนคุณชนะ")
                money = money + derm
                print("ยอดเงินคงเหลือ", money)
            elif gu == 3 and k == 2:
                print("\nบอทออกกระดาษคุณชนะ")
                money = money + derm
                print("ยอดเงินคงเหลือ", money)
            elif gu == 1 and k == 2:
                print("\nบอทออกกระดาษคุณแพ้")
                money = money - derm
                print("ยอดเงินคงเหลือ", money)
            elif gu == 2 and k == 3:
                print("\nบอทออกกรรไกรคุณแพ้")
                money = money - derm
                print("ยอดเงินคงเหลือ", money)
            elif gu == 3 and k == 1:
                print("\nบอทออกค้อนคุณแพ้")
                money = money - derm
                print("ยอดเงินคงเหลือ", money)
            elif gu == 1 and k == 1:
                print("\nเสมอ")
                print("ยอดเงินคงเหลือ", money)
            elif gu == 2 and k == 2:
                print("\nเสมอ")
                print("ยอดเงินคงเหลือ", money)
            elif gu == 3 and k == 3:
                print("\nเสมอ")
                print("ยอดเงินคงเหลือ", money)
            return fail(money)


def menutai():
    print("\n[ทายเลข 1-8]")
    print("9.กลับเมนูเกม")
    print("0.ออกเกม\n")


def tai():
    global money
    w = 1
    while w != 0:
        menutai()
        se = random.randint(1, 5)
        print(se)
        try:
            x = int(input("คุณจะเดาเลขอะไร:"))
        except:
            print("\nระบบใส่ได้แค่ตัวเลขเท่านั้น")
            return tai()
        if x == 0:
            farewell(name)
            return exit()
        elif x == 9:
            return menu_game()

        try:
            derm = int(input("เดิมพัน:"))
        except:
            print("\nระบบใส่ได้แค่ตัวเลขเท่านั้น")
            return tai()
        if derm > money:
            print("เงินเดิมพันไม่สามารถมากกว่าเงินที่เหลือ")
            return tai()

        if x == se :
            print("คุณเดาถูก")
            money = money + derm*2
            print("ยอดเงินคงเหลือ", money)
        else:
            print("คุณเดาผิดคำตอบคือ:",se)
            money = money - derm
            print("ยอดเงินคงเหลือ", money)
        fail(money)
        return tai()
    # ro = 0
    # ge = 0
    # while ge != se:
    #     ge = int(input("คุณเดาเลข :"))
    #     ro = ro + 1
    # else:
    #     print("คุณเดาถูก")
    #     print("เดาไป", ro, "รอบ")


def greet(name):
    thistime = datetime.datetime.now().hour
    if (thistime <= 12):
        thegreet = "ตอนเช้า"
    else:
        thegreet = "ตอนบ่าย"
    print(f"สวัสดี{thegreet} คุณ {name}")


def farewell(name):
    print(f"\n++ ลาก่อนคุณ{name}")
    print("ขอบคุณที่ใช้บริการ")
    print("--------------")


# หลัก
def main():
    while True:
        mainmenu()
        work = int(input("เลือกหัวข้อเพื่อทำงาน : "))
        if work == 0:
            farewell(name)
            break
        elif work == 1:
            worker = menu_trip(name)
            if worker == 0:
                farewell(name)
                break
            elif worker == 9:
                pass
        elif work == 2:
            worker = menu_game()
            if worker == 0:
                farewell(name)
                break
            elif worker == 9:
                pass
        else:
            pass


if __name__ == '__main__':
    print("--------------")
    name = input("ชื่อ: ")
    greet(name)
    main()
