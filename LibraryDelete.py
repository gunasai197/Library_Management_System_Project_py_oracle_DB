import oracledb as odb
def deletebook():
    try:
        conn=odb.connect("gunasai/sai@localhost/orcl")
        cur=conn.cursor()
        bno=int(input("Enter the book no:"))
        qr="delete from  library where b_no=%d" %(bno)
        cur.execute(qr)
        conn.commit()
        if(cur.rowcount>0):
            print("-" * 50)
            print("\t{} book is delete successfully".format(cur.rowcount))
            print("-"*50)
        else:
            print("-" * 50)
            print("\tBook no is not found:{} Please try again".format(bno))
            print("-" * 50)
    except odb.DatabaseError as db:
        print("Problem in database:",db)
    except ValueError:
        print("Don't enter str,symbol for book no.")
