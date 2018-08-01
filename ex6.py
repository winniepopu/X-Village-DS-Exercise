#將sorted好的PTT dicionart寫入sorted_PTT.json
import json

with open('ptt_0726_s.json',encoding='utf-8-sig') as f:
    article = json.load(f)
    list=[]    

    for i in range(len(article)):
        if 'all' in article[i]["h_推文總數"].keys():
            list.append(article[i])

    result =sorted(list,key=lambda k: k["h_推文總數"]['all'],reverse=True)
    with open('sorted_PTT.json','w+',encoding='utf-8-sig') as g:
        result=json.dumps(result, indent=4,ensure_ascii=False)
        g.write(result)





