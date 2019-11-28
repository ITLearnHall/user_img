#!/usr/bin/python
#coding:GB18030

server_ip='localhost'
server_port='5236'

FLAG_FAIL=-1
FLAG_NOCARE=0
FLAG_SUCC=1
FLAG_SUCC_WITH_RESULT=2

EXEC_SUCC_WITH_RESULT=2
EXEC_SUCC=1
EXEC_NOCARE=0
EXEC_FAIL=-1

import sys
from datetime import date
sys.path.append('/usr/local/lib/python3.3/site-packages')
import dmPython


def result_check(testname, expect_flag={},expect_set={}):
    #check flag
    result=testname()
    print ("result %s"%result[0])
    #print result[1]
    print ("expect %s"%expect_flag)
    #print expect_set
    message='success'
    if expect_flag==FLAG_NOCARE:
                test_flag=True
                #message='';         
    elif expect_flag == result[0]:
        if expect_flag==FLAG_SUCC_WITH_RESULT:
            if result[1] != expect_set:
                test_flag=False
                message='result error.\n expect result: %s\n return result: %s' %(expect_set,result[1])
            else:
                test_flag=True
                #message='';                
        else:
            test_flag=True
            #message='';
    else:
        test_flag=False
        if expect_flag == FLAG_FAIL and result[0]>=FLAG_SUCC:
            message='result error.\n except fail, exec success'
        elif expect_flag == FLAG_SUCC and result[0]==FLAG_FAIL:
            message='exec fail.\n %s' %result[1]
        elif expect_flag == FLAG_SUCC and result[0]==FLAG_SUCC_WITH_RESULT:
            message='result error.\n expect result: %s\n return result: %s' %(expect_set,result[1])
        elif expect_flag == FLAG_SUCC_WITH_RESULT and result[0]>=FLAG_SUCC:
            message='result error.\n expect result: %s\n return result: %s' %(expect_set,result[1])
        else:
            message='fail.\n %s' %result[1] 
    print ('test_flag=:%d, message= %s'%( test_flag, message ))
    
def test_dm_cursor_execute_000():
    try:
        conn = dmPython.connect(host=server_ip, port= server_port)
        cursor  = conn.cursor()
        cursor.execute ("drop table execute_test")
        flag=EXEC_NOCARE
        info=''
        conn.close()
    except (dmPython.Error, Exception) as err:
        flag=FLAG_FAIL
        info=err 
    return (flag, info)
                 
def test_dm_cursor_execute_002():
    try:
        conn = dmPython.connect(user='SYSDBA', password='SYSDBA', server=server_ip, port=server_port, autoCommit=True)
        cursor  = conn.cursor()
        d = date(2015,6,10)
        cursor.execute ("create table execute_test(c1 int, c2 varchar,c3 date)")
        cursor.execute ("insert into execute_test values(1, '23',?)",d)
        cursor.execute ("insert into execute_test values(2, '23',?)",d)
        cursor.execute ("delete from  execute_test where c1 =1")
        cursor.execute ("update execute_test set c2='ccc' where c1 =2") 
        info=''
        flag=EXEC_SUCC
        conn.close()
    except (dmPython.Error, Exception) as err:
        flag=FLAG_FAIL
        info=err 
    return (flag, info)

def test_dm_cursor_fetchone_003():
    try:
        conn = dmPython.connect(host=server_ip, port= server_port)
        cursor  = conn.cursor()
        cursor.execute("select * from execute_test")
        result = True
        i = 0
        while result!=None:
            i= i+1
            result = cursor.fetchone()
            print ("第 %d 行：\n"%i)
            print (result)
            print
        info=''
        flag=EXEC_SUCC
        conn.close()
    except (dmPython.Error, Exception) as err:
        flag=FLAG_FAIL
        info=err 
    return (flag, info)


result_check(test_dm_cursor_execute_000, expect_flag=EXEC_NOCARE) 
result_check(test_dm_cursor_execute_002, expect_flag=EXEC_SUCC)
result_check(test_dm_cursor_fetchone_003, expect_flag=EXEC_SUCC)

