
from flask import Flask,jsonify,request,render_template,redirect
import pandas as pd
import json
df=pd.read_excel(r"C:\Users\u27t43\Documents\Electrical Calculations for APFC System_30032022_WIP.xlsx",sheet_name="DATA")
print(df.columns)
connPow=df[['Stage No.','Total Running Power Factor','Total kVAr-Running','Efficiency','Status']]
connPow.columns =['Stage_No.','Total_Running_Power_Factor', 'Total_kVAr_Running','Efficiency','Status']
#print(connPow)
connPow= connPow.set_index('Stage_No.')
#print(df)
my_dictionary = connPow.to_dict()
print(df.columns)
app=Flask(__name__)
 
@app.route('/',methods=['GET','POST'])
def user():
    if request.method == 'POST':
        json_data =request.get_json()
        print(json_data['stages'])
        stages=json_data['stages']
        if (stages > 12): stages = 12    
        x1=list(my_dictionary["Total_Running_Power_Factor"].items())
        x2=list(my_dictionary["Total_kVAr_Running"].items())
        x3=list(my_dictionary["Efficiency"].items())
        x4=list(my_dictionary["Status"].items())
        
        X1=[]
        for j in range(stages):
         X1.append(x1[j])
                     
        X2=[]
        for j in range(stages):
         X2.append(x2[j])
        X3=[]
        for j in range(stages):
         X3.append(x3[j])
        X4=[]
        for j in range(stages):
         X4.append(x4[j])
        X=[X1,X2,X3,X4]
        dict1={}
        dict2={}
        dict3={}
        dict4={}
        a=[]
        b=[]
    
        for i in range(1):
            for j in range(stages):
               
              a.append(X1[j][i])
              b.append(X1[j][i+1])
       
        c=[]
        d=[] 
        for i in range(1):
            for j in range(stages): 
              c.append(X2[j][i])
              d.append(X2[j][i+1])
        e=[]
        f=[]
        for i in range(1):
            for j in range(stages): 
              e.append(X3[j][i])
              f.append(X3[j][i+1])
        g=[]
        h=[]
        for i in range(1):
            for j in range(stages): 
              g.append(X4[j][i])
              h.append(X4[j][i+1])
        for i in range(stages):
            if(a[i]==c[i]):
                a[i]=i+1
                c[i]=i+1
                e[i]=i+1
                g[i]=i+1    
        for i in range(stages):      
              dict1[a[i]] = b[i]
              dict2[c[i]] = d[i]
              dict3[e[i]] = f[i]
              dict4[g[i]] = h[i]
       
        keys={"Total_Running_Power_Factor":dict1,"Total_kVAr_Running":dict2,"Efficiency":dict3,"Status":dict4}
        
        return jsonify(keys)

        
    return "invalid method"   
 
if __name__=='__main__':
     app.run(debug=True,port=10)    