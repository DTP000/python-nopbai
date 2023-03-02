import mysql.connector, openpyxl
myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "py_db")
cur = myconn.cursor()
sql = ("insert into sv(masv, ho, ten, ngaysinh, toan, ly, hoa) "
+ "values (%s, %s, %s, %s, %s, %s, %s)")
# val = ("The Mac", 10001, 25000.00, 101, "Hanoi")

wb = openpyxl.load_workbook("input.xlsx")
# print(wb.sheetnames)
ws = wb[wb.sheetnames[0]]
for i in range(12, 63):
    # print(ws.cell(row=i, column=2).value)
    val = (ws.cell(row=i, column=2).value, ws.cell(row=i, column=3).value, ws.cell(row=i, column=4).value, ws.cell(row=i, column=5).value, ws.cell(row=i, column=6).value, ws.cell(row=i, column=7).value, ws.cell(row=i, column=8).value)
    try:
        cur.execute(sql,val)
        myconn.commit()
    except:
        myconn.rollback()
# print(cur.rowcount,"record inserted!")
myconn.close()

