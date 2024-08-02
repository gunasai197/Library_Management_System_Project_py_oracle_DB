import oracledb as odb
def addbook():
    try:
        conn=odb.connect("gunasai/sai@localhost/orcl")
        cur=conn.cursor()
        bno=int(input("Enter the new book no:"))
        bname=input("Enter the new book name:")
        bprice=float(input("Enter the book price:"))
        bp=input("Enter the book publication name:")
        qr="insert into library values(%d,'%s','%s','%s')" %(bno,bname,bprice,bp)
        cur.execute(qr)
        conn.commit()
        print("=" * 50)
        print("\t{} book saved successfully".format(cur.rowcount))
        print("=" * 50)
    except odb.DatabaseError as db:
        print("Problem in database:",db)
    except ValueError:
        print("Don't enter str,symbol for book no and book name.")
