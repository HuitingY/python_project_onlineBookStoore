import copy
from tabulate import tabulate
from datetime import date
today = date.today().strftime("%Y/%m/%d")

##initial_prepare
#期中專題相關函式I_Q1: 分割字串並將其儲存.
#期中專題相關函式II_Q1: 讀取inventory.txt檔案, 並一行一行讀取檔案將每一個元素存成偏好的資料結構-list
#初始畫面之讀取檔案函式,可讀取'inventory.txt'檔案,為了於後續使用者介面上呈現書籍排行及書籍列表。
def read_file(file):
    f = open(file, 'r')
    while True:
        str1 = f.readline()
        if ( str1 != ''):
            str1_split = str1.split(';')
            book_name.append(str1_split[0])
            price.append(int(str1_split[1]))
            cost.append(int(str1_split[2]))
            inventory.append(int(str1_split[3]))
            publication_date.append(str1_split[4])
            if ( len(str1_split) == 6):
                sales_unit.append(int(str1_split[5]))
        else:
            break
    f.close()
    return book_name, price, cost, inventory, publication_date, sales_unit

#初始畫面之書本號碼及書名顯示
def show_book_user():
    for i in range(1, len(book_name)+1):
        print(f'{i}. {book_name[i-1]} (${price[i-1]})', end='\n')

#每進行一次資料更新後,重新撰寫'inventory.txt'檔案
def write_inv(file):
    f = open(file, 'w')
    if sales_unit != []:
        for i in range(0, len(book_name)):
            f.write(f'{book_name[i]};{price[i]};{cost[i]};{inventory[i]};{publication_date[i].strip()};{sales_unit[i]}\n')
    else:
        for i in range(0, len(book_name)):
            f.write(f'{book_name[i]};{price[i]};{cost[i]};{inventory[i]};{publication_date[i]}')
    f.close()

#期中專題相關函式I_Q2: 書籍銷售排行函式,若使用者第一次使用因為沒有銷售紀錄故不會顯示排行;
#若使用者開始於書城購買任一本書之後則會開始於初始畫面顯示書籍銷售排行列表，若銷售書量相同時則照書本號碼排序。
def bookRanking(book_name, book_sale):
    table = []
    book_ranking = []
    index_list = []
    copy_list = copy.deepcopy(book_sale)
    copy_list2 = copy.deepcopy(book_sale)
    for i in range(1, len(copy_list)):
        for j in range(len(copy_list)-i):
            if copy_list[j] < copy_list[j+1]:
                tmp = copy_list[j]
                copy_list[j] = copy_list[j+1]
                copy_list[j+1] = tmp
    for i in copy_list:
        index = copy_list2.index(i)
        copy_list2[index] = -1
        index_list.append(index)
    for i in index_list:
        book_ranking.append(book_name[i])
    for i in range(3):
        table.append([])
        table[i].append(book_ranking[i])
        table[i].append(copy_list[i])

    return tabulate(table, ["Book Name", "Sales Volume"], tablefmt="psql")

##for_user(使用者功能)

#期中專題相關函式I_Q3: 若讀者欲購買之書本無庫存，則會顯示"售完"。
#讀者進行購買書本之函式，當讀者輸入相對應書號後，若書號有效則會自動更新'inventroy.txt'檔案中之庫存。
#若該書號庫存為0的話則會顯示售完並返回主畫面。
def buyBook(book_item):
    if inventory[int(book_item)-1] == 0:
        back = input('售完, 按任一鍵回到初始畫面 ')
    else:
        inventory[int(book_item)-1] -= 1
        if sales_unit != []:
            sales_unit[int(book_item)-1] += 1
        else:
            for i in range(len(book_name)):
                sales_unit.append(0)
            sales_unit[int(book_item)-1] = 1
        write_inv('inventory.txt')
        back = input('Successful transaction!\n'
                     '按任一鍵返回主畫面! ')
        profit_report(book_item)

#期中專題相關函式II_Q4: 該報表會顯示利潤以及所有交易紀錄.
#若讀者購書成功之後則會自動延續此函式，該報表的profit是書城開幕以來所有的書本價格減去書本成本所合計之總利潤;
#總利潤下方列表則顯示至今所有交易。
def profit_report(book_item):
    profit_thisTrade = price[int(book_item) - 1] - cost[int(book_item) - 1]
    f = open('FinStat.txt', 'a+')
    f.seek(0)
    tmp = f.readlines()
    if ( tmp != []):
        ct = 0
        profit = 0
        f.seek(0)
        while True:
            ct = ct + 1
            str1 = f.readline()
            if ( ct > 1):
                if (str1 !=  ""):
                    str1_split = str1.split(';')
                    profit = profit + (int(str1_split[1]) - int(str1_split[2]))
                else:
                    break
        f.close()
        f = open('FinStat.txt', 'w')
        profit_total = profit + profit_thisTrade
        f.write(f'** Profit of Online Book store: ${profit_total} **\n')
        f.writelines(tmp[1:])
        f.write(f'{book_name[int(book_item) - 1]};{price[int(book_item) - 1]};'
                f'{cost[int(book_item) - 1]};{today}\n')
        f.close()
    else:
        f.write(f'** Profit of Online Book store: ${profit_thisTrade} **\n')
        f.write(f'{book_name[int(book_item) - 1]};{price[int(book_item) - 1]};'
                f'{cost[int(book_item) - 1]};{today}\n')
        f.close()

##for_administer-後臺介面
#期中專題相關函式I_Q3: 該報表讀入書名後會顯示該書之庫存
#KEY入AAA後進入使用者畫面，再點選1.Show information about books，系統化面會顯示
#書名、價錢、成本、庫存狀態("充足"或是"<5本")、庫存量、出版日期以及銷售量(如果該書有銷售紀錄的話)

def show_book_administer(list):
    twoD_array = []
    for i in range(len(book_name)):
        twoD_array.append([])
        twoD_array[i].append(book_name[i])
        twoD_array[i].append(price[i])
        twoD_array[i].append(cost[i])
        if int(inventory[i]) >= 5:
            twoD_array[i].append("Sufficient")
        else:
            twoD_array[i].append("< 5 units")
        twoD_array[i].append(inventory[i])
        twoD_array[i].append(publication_date[i])
        if sales_unit != []:
            twoD_array[i].append(sales_unit[i])

    if sales_unit != []:
        return tabulate(twoD_array, ["Book Name", "Price", "Cost", "Stock status",
                                     "Inventory", "Publication_date", "Sales"], tablefmt="psql")
    else:
        return tabulate(twoD_array, ["Book Name", "Price", "Cost", "Stock status",
                                     "Inventory", "Publication_date"], tablefmt="psql")

#期中專題相關函式II_Q2: 賣家輸入書名後可將售價進行調整
def modify_item_price():
    modify_book_name = input('請輸入書名: ')
    for i in book_name:
        if (modify_book_name == i):
            modify_index = book_name.index(i)
            modify_price = int(input('請輸入修改價格: '))
            price[modify_index] = modify_price
            write_inv('inventory.txt')
            back = input('修改成功, 按任一鍵返回主畫面! ')
            break
    else:
        print('查無此書')

#期中專題相關函式II_Q2: 賣家輸入書名後可將庫存量進行調整
def modify_item_stock():
    modify_book_name = input('請輸入書名: ')
    for i in book_name:
        if (modify_book_name == i):
            modify_index = book_name.index(i)
            modify_price = int(input('請輸入修改庫存: '))
            inventory[modify_index] = modify_price
            write_inv('inventory.txt')
            back = input('修改成功, 按任一鍵返回主畫面! ')
            break
    else:
        print('查無此書')

#期中專題相關函式II_Q3: 賣家可新增書名及其相關資料
def add_item(file):
    f = open(file, 'a+')
    bookName = input('請輸入書名: ')
    price = int(input('請輸入價錢: '))
    cost = int(input('請輸入成本: '))
    inventory = int(input('請輸入冊數: '))
    publication_date = input('請輸入出版日期: ')
    if sales_unit != []:
        f.write(f'{bookName};{price};{cost};{inventory};{publication_date};0')
    else:
        f.write(f'{bookName};{price};{cost};{inventory};{publication_date}')
    f.close()
    back = input('修改成功! 按任一鍵返回! ')

#bonus_按照日期排序
def sort_date(list):
    sort_date_list = sorted(publication_date, reverse=True)
    index_list = []
    date_table = []
    for i in sort_date_list:
        index_list.append(list.index(i))
    for i in range(len(book_name)):
        date_table.append([])
        date_table[i].append(book_name[index_list[i]])
        date_table[i].append(publication_date[index_list[i]])
    return tabulate(date_table, ["Book Name", "Publication Date"], tablefmt="psql")


#-----------------------------------------------------------
while True:
    book_name = []
    price = []
    cost = []
    inventory = []
    publication_date = []
    sales_unit = []
    read_file('inventory.txt')
    print(f'-----------------------------\n'
          f'Welcome to online book store!\n')
    if sales_unit != []:
        print('* * Best Seller (TOP3) * *')
        print(bookRanking(book_name, sales_unit))
    else:
        print('* Best seller: \n'
              'Buy your first book to show the best seller!!\n')
    print()
    print('* * Order By Publication Date * *')
    print(sort_date(publication_date))
    print()
    print('* * Book Number * *')
    show_book_user()
    print()
    user_type = input("Type a book number for the purchase or type “AAA” for the administrative interface: ")

    if user_type == 'AAA':
        print('* * Administrative Model: * *\n'
              '1. Show information about books\n'
              '2. Update the price of an item\n'
              '3. Update the stock of an item\n'
              '4. Add new book to the store\n'
              '5. Go back to the initial screen\n')
        mode = input('(管理員介面)請輸入執行動作: ')
        try:
            if type(int(mode)) == int:
                if int(mode) ==1:
                    print(show_book_administer('inventory.txt'))
                    back = input('按任一鍵返回主畫面! ')
                elif int(mode) ==2:
                    modify_item_price()
                elif int(mode) ==3:
                    modify_item_stock()
                elif int(mode) ==4:
                    add_item('inventory.txt')
                elif int(mode) ==5:
                    continue
                else:
                    back = input('沒有該模式, 重新返回主畫面! ')
        except Exception as e:
            back = input('輸入錯誤, 按一任鍵返回主畫面! ')
    else:
        try:
            if ( type(int(user_type)) == int ) and ( 1 <= int(user_type) <= len(book_name) ):
                buyBook(user_type)
            else:
                back = input('沒有該書號, 請重新輸入, 任意鍵返回主畫面! ')
        except Exception as e:
            back = input('輸入錯誤, 請重新輸入, 任意鍵返回主畫面! ')
