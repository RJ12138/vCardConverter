#coding=utf-8
import pandas as pd
import numpy as np


df = pd.read_excel('test.xlsx')
vcfFileName = "./texs.vcf"
f = open(vcfFileName, 'w')
print((df['分组'].unique()))

for i in df.index:
    f.write("BEGIN:VCARD\n")
    f.write("BDAY:" + str(df.loc[i, '生日']) + "\n")
    f.write("CATEGORIES:" + df.loc[i, '分组'] + "\n")
    f.write("EMAIL;TYPE=INTERNET:" + df.loc[i, '邮箱'] + "\n")
    f.write("N:测试" + df.loc[i, '姓名'] + "\n")
    f.write("NOTE:" + str(df.loc[i, '备注']) + "\n")
    f.write("TEL;TYPE=cell;TYPE=pref:" + str(df.loc[i, '电话号码']) + "\n")
    f.write("VERSION:3.0\nEND:VCARD\n")

f.close()
print('vcf file generated.')
# df = df[(df['学年学期']=='2017-2018-3') | (df['学年学期']=='2018-2019-1') | (df['学年学期']=='2018-2019-2')]  
# df.head(5) 