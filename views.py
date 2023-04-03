from django.shortcuts import render
import mysql.connector
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def postTasks(request,id,task):

    #tasks=request.POST
    mydb=mysql.connector.connect(host='localhost',user='root',password='password0',database='dbs_1')
    mydb2 = mysql.connector.connect(host='localhost', user='root', password='password0', database='dbs_2')
    cursor=mydb.cursor()
    cursor2=mydb2.cursor()
    print(cursor)
    if(id%2 == 0):
         cursor.execute('insert into to_do_app values (%s,%s);',[id,task])
         mydb.commit()
         cursor.close()
    else:
        cursor2.execute('insert into to_do_app values (%s,%s);',[id,task])
        mydb2.commit()
        cursor2.close()

    return HttpResponse(1)



