import sqlite3

conn = sqlite3.connect('testdrill103.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_info TEXT \
        col_dtype VARCHAR \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('testdrill103.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('information.', 'docx'))
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('Hello.', 'txt'))
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('myImage.', 'png'))
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('myMovie.', 'mpg'))
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('World.', 'txt'))
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('data.', 'pdf'))
    cur.execute("INSERT INTO tbl_files(col_info, col_dtype) VALUES (?,?)", \
                ('myPhoto.', 'jpg'))
    conn.commit()
conn.close()


conn = sqlite3.connect('testdrill103.db')

with conn:
    cur = conn.cursor()
    cur.execute("Select col_info,col_dtype From tbl_files WHERE col_dtype = 'txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "Info Type: {}{}".format(item[0],item[1])
        print(msg)
        
       
    

