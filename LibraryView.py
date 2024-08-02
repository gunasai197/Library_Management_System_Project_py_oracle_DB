import oracledb as db
def viewbook():
    try:
        conn=db.connect("gunasai/sai@localhost/orcl")
        cur=conn.cursor()
        bno=int(input("Enter the book no for view book details:"))
        qr="select * from library where b_no=%d" %(bno)
        cur.execute(qr)
        records=cur.fetchone()
        print("-"*50)
        print("\tbook no:",records[0])
        print("\tbook name:",records[1])
        print("\tbook price:",records[2])
        print("\tbook publication:",records[3])
        print("-" * 50)
    except db.DatabaseError as dbe:
        print("\tProblem in database:",dbe)
    except ValueError:
        print("\tDon't enter str,symbol for book no.")
    except TypeError:
        print("\tBook no is not found:{}".format(bno))

def viewallbooks():
    try:
        conn=db.connect("gunasai/sai@localhost/orcl")
        cur=conn.cursor()
        qr="select * from library order by b_no"
        cur.execute(qr)
        records=cur.fetchall()
        cols=cur.description
        for col in cols:
            print("\t",col[0],end="\t")
        print()
        for record in records:
            for val in record:
                print("\t",val,end="\t")
            print("")
    except db.DatabaseError as dbe:
        print("Problem in database:",dbe)