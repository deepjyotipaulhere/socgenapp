from  flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import pymysql
import sys

app=Flask(__name__)
CORS(app)

def connection():
    client=pymysql.connect(host='localhost',user='root',password='1234',db='socgen',cursorclass=pymysql.cursors.DictCursor)
    return client

@app.route("/insertsgfiles",methods=['POST'])
def insertsgfiles():
    try:
        con=connection()
        cur=con.cursor()       
        file = request.files['file']
        data=file.read()
        p=data.splitlines()[1:]
        print(p[0][4:].decode())
        query="insert into onetoone_sg values('"+p[0][4:].decode()+"','"+p[1][5:].decode()+"','"+p[2][5:].decode()+"','"+p[3][5:].decode()+"','"+p[4][5:].decode()+"','"+p[5][5:].decode()+"','"+p[6][5:].decode()+"','"+p[7][5:].decode()+"','"+p[8][5:].decode()+"','"+p[9][4:].decode()+"','"+p[10][5:].decode()+"','"+p[11][5:].decode()+"','"+p[12][5:].decode()+"','"+p[13][5:].decode()+"','"+p[14][4:].decode()+"','"+p[15][5:].decode()+"','"+p[16][5:].decode()+"','"+p[17][5:].decode()+"')"
        cur.execute(query)
        con.commit()
        return "ok"
    except Exception as e:
        print(str(e))
        a,b,c=sys.exc_info()
        print(c.tb_lineno)
        return make_response(str(e),500)


@app.route("/insertcpfiles",methods=['POST'])
def insertcpfiles():
    try:
        con=connection()
        cur=con.cursor()       
        file = request.files['file']
        data=file.read()
        p=data.splitlines()[1:]
        print(p[0][4:].decode())
        query="insert into onetoone_cp values('"+p[0][4:].decode()+"','"+p[1][5:].decode()+"','"+p[2][5:].decode()+"','"+p[3][5:].decode()+"','"+p[4][5:].decode()+"','"+p[5][5:].decode()+"','"+p[6][5:].decode()+"','"+p[7][5:].decode()+"','"+p[8][5:].decode()+"','"+p[9][4:].decode()+"','"+p[10][5:].decode()+"','"+p[11][5:].decode()+"','"+p[12][5:].decode()+"','"+p[13][5:].decode()+"','"+p[14][4:].decode()+"','"+p[15][5:].decode()+"','"+p[16][5:].decode()+"','"+p[17][5:].decode()+"')"
        cur.execute(query)
        con.commit()
        return "ok"
    except Exception as e:
        print(str(e))
        a,b,c=sys.exc_info()
        print(c.tb_lineno)
        return make_response(str(e),500)

@app.route("/match",methods=['GET'])
def match():
    try:
        con=connection()
        cur=con.cursor()
        q1="select * from onetoone_sg"
        cur.execute(q1)
        res1=cur.fetchall()
        q2="select * from onetoone_cp"
        cur.execute(q2)
        res2=cur.fetchall()
        a=[]
        for i in res1:
            for j in res2:
                if i[':32B']==j[':33B'] and i[':33B']==j[':32B'] and i[':82A']==j[':87A'] and i[':87A']==j[':82A'] and i[':77H']==j[':77H'] and i[':30T']==j[':30T'] and i[':30V']==j[':30V'] and i[':36']==j[':36'] and i[':56']==j[':56']: #and i[':57A']==j[':57A'] and i[':58']==j[':58']:
                    a.append((i[':20'],j[':20']))
        print(len(a))
        return jsonify(a)
    except Exception as e:
        print(str(e))

if __name__=='__main__':
    app.run(debug=True)