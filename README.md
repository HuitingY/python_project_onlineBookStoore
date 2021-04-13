# python_project_onlineBookStoore

*使用前請安裝tabulate, datetime以及copy套件。  
*需夾帶'inventory.txt'檔案，內容如下:
Thinking python;520;300;10;2015/12/31
Introduction to Algorithms;4950;2000;20;2009/09/01
Introduction to Management Science;1420;800;15;2019/04/01


## 功能介紹
 1.初始畫面:此為線上書城購書系統，初始畫面會顯示三個表格，分別為(1).best seller-最佳銷售前三本列表、(2).order by publication date-按照出版日期排序之書籍列表以及(3).book number-書本號碼列表。
(註1:使用者若是第一次使用購書系統，Best seller因為沒有相關銷售紀錄會顯示" Buy your first book to show the best seller!! ")
(註2:若銷售數量相同時則會優先顯示書號在前的書本)

 2.購書:初始畫面下方會有"Type a book number for the purchase or type “AAA” for the administrative interface:"之提示文字，若使用者想購買書本可以參考書本號碼列表選擇欲購買之書本，若鍵入有效書號系統會自動顯示"Successful transaction!"並同時更新"inventory.txt"以及"Finstat.txt"檔案，其中"inventory.txt"會更新庫存數量以及銷售數量;"Finstat.txt"則會根據書本售價扣除書本成本計算所有已發生交易之總利潤。若使用者輸入書號錯誤或是不存在則會重返主畫面。

  example:
  ------------------------------------------------------------------------------------
  Step1:購買書號1.Thinking python:
  Type a book number for the purchase or type “AAA” for the administrative interface: 1
  Successful transaction!

  Step2:系統自動更新"inventory.txt":
  Thinking python;520;300;9;2015/12/31;1
  Introduction to Algorithms;4950;2000;20;2009/09/01;0
  Introduction to Management Science;1420;800;15;2019/04/01;0

  Step3:系統自動更新"Finstat.txt":
  ** Profit of Online Book store: $220 **
  Thinking python;520;300;2020/11/09

  ------------------------------------------------------------------------------------

 3.管理者介面:若非輸入書號而是輸入"AAA"(需大寫)則會進入管理員介面。畫面如下所示:
   ------------------------------------- 
    * * Administrative Model: * *
   1. Show information about books
   2. Update the price of an item
   3. Update the stock of an item
   4. Add new book to the store
   5. Go back to the initial screen
   -------------------------------------
   
   -1:此功能會顯示書籍相關資訊，包括書本名稱、價格、成本、庫存狀態(若大於5本會顯示"充足",而少於5本則會顯示"<5本")、庫存數量、出版日期及銷售數量等資訊。

   系統畫面:
   +------------------------------------+---------+--------+----------------+-------------+--------------------+---------+
   | Book Name                          |   Price |   Cost | Stock status   |   Inventory | Publication_date   |   Sales |
   |------------------------------------+---------+--------+----------------+-------------+--------------------+---------|
   | Thinking python                    |     520 |    300 | Sufficient     |           9 | 2015/12/31         |       1 |
   | Introduction to Algorithms         |    4950 |   2000 | Sufficient     |          20 | 2009/09/01         |       0 |
   | Introduction to Management Science |    1420 |    800 | Sufficient     |          15 | 2019/04/01         |       0 |
   +------------------------------------+---------+--------+----------------+-------------+--------------------+---------+

   -2:此功能可以讓管理員更改指定書籍之價格，並同時更新至"inventory.txt"。
   -3:此功能可以讓管理員更改指定書籍之庫存，並同時更新至"inventory.txt"。
   -4:此功能可以讓管理員新增書籍，同時須輸入價格、成本、庫存及出版日期等資訊，並同時更新至"inventory.txt"。

      example:
      ----------------------------------------------------------------------------------
      請輸入書名: Harry potter
      請輸入價錢: 9000
      請輸入成本: 100
      請輸入冊數: 50
      請輸入出版日期: 2001/10/26
      修改成功! 按任一鍵返回! 
      -----------------------------
      Welcome to online book store!

      * * Best Seller (TOP3) * *
      +------------------------------------+----------------+
      | Book Name                          |   Sales Volume |
      |------------------------------------+----------------|
      | Thinking python                    |              1 |
      | Introduction to Algorithms         |              0 |
      | Introduction to Management Science |              0 |
      +------------------------------------+----------------+

      * * Order By Publication Date * *
      +------------------------------------+--------------------+
      | Book Name                          | Publication Date   |
      |------------------------------------+--------------------|
      | Introduction to Management Science | 2019/04/01         |
      | Thinking python                    | 2015/12/31         |
      | Introduction to Algorithms         | 2009/09/01         |
      | Harry potter                       | 2001/10/26         |     <------ Harry potter新增成功
      +------------------------------------+--------------------+

      * * Book Number * *
      1. Thinking python ($520)
      2. Introduction to Algorithms ($4950)
      3. Introduction to Management Science ($1420)
      4. Harry potter ($9000)                                         <------ Harry potter新增成功
      ----------------------------------------------------------------------------

   -5:回到主畫面。

 

   

