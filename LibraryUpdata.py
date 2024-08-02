import oracledb as odb
def bookupdate():
    try:
        conn=odb.connect("gunasai/sai@localhost/orcl")
        cur=conn.cursor()
        bno=int(input("Enter the book no for update book details:"))
        bname=input("Enter the book update name:")
        bprice=float(input("Enter the book update price:"))
        bp=input("Enter the book update publication name:")
        qr="update library set bname='%s',bprice='%f',publication='%s' where b_no=%d" %(bname,bprice,bp,bno)
        cur.execute(qr)
        conn.commit()
        print("-"*50)
        print("\t{} book details is update successfully ".format(cur.rowcount))
        print("-"*50)
    except odb.DatabaseError as db:
        print("Problem in database:", db)
    except ValueError:
        print("Don't enter str,symbol for book no.")
