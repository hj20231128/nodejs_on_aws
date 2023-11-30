import pymysql as m

con = m.connect(host='3.27.174.62', port=3306, user='root-remote', 
                password='1234',db='nodejs', charset='utf8')
cur = con.cursor()
q = 'insert into t1 values(2123);'
cur.execute(q)
con.commit()
con.close()