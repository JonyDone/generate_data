#!/usr/local/python3/bin/python3
import time,os,csv,random

def re_exe(cmd,inc = 60):

  while True:
    """
    print("ceshi")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    """
    createcsv()
    os.system(cmd)

    time.sleep(inc)
def createcsv():

        deviceidlist = ["x", "x", "x", "x", "x", "x", "x"]
        caridlist = ["x","x","x","x","x","x","x"]

        colorlist = ["x", "x", "x", "x", "x", "x", "x"]

        devicelocidlist = ["x", "x", "x", "x", "x", "x", "x"]

        randnum=random.randint(0,6)

        csvname='videoCsv'+str(time.strftime("%Y%m%d%H%M%S",time.localtime()))+'.csv'

        print("============生成数据为:"+caridlist[randnum]+"===========时间为:"+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))

        header = ['1','2','3','4','5','6','7','8','9','10','1']
        data = [{'1':deviceidlist[randnum],'2':'','3':'','4':'','5':caridlist[randnum],'6':'小型车','7':colorlist[randnum],'8':'','homeowner_ship':'9','10':str(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())),'11':devicelocidlist[randnum]}
        ]

        with open('/home/test1/'+csvname, 'w', encoding='utf-8', newline='') as f: 
            writer=csv.DictWriter(f,header) 
            writer.writeheader() 
            writer.writerows(data) 
        with open('/home/test2/'+csvname, 'w', encoding='utf-8', newline='') as f: 
            writer=csv.DictWriter(f,header) 
            writer.writeheader() 
            writer.writerows(data)

re_exe("echo %time%",600)
