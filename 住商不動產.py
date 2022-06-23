response = []
i = 2 
while i < 22:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'Referer': 'https://www.hbhousing.com.tw/BuyHouse/%E5%8F%B0%E5%8C%97%E5%B8%82/116',}
    params = {'job': 'search','path': 'house',}

    payload = {
    'q':"^1^3^116^^^1_9^2_3_4_5^^^^^^^^^^^0^^{}^0".format(i),
    'rlg': '0'
    }

    i += 1
    response2 = requests.post('https://www.hbhousing.com.tw/ajax/dataService.aspx', params=params, headers=headers, data=payload)
    x=response2.json()
    response.append(x)    

title = []
address = []
house_type = []
age = []
area = []
price = []
room = []
floor = []
total_floor = []

dd = {i:v for i,v in enumerate(response)}
for z in dd.values():
    for t in z['data']:
        title.append(t["n"])
        address.append(t["x"])
        house_type.append(t["t"])
        age.append(t["k"])
        area.append(t["a"])
        price.append(t["np"])
        room.append(t["p"])
        floor.append(t["w"])
        total_floor.append(t["z"])



ave = [int(a) / float(b) for a, b in zip(price, area)] 
ave = [round(i,2) for i in ave]

data1=[]
for n in range(len(title)):
    d={}
    d['title']=title[n]
    d['address']=address[n]
    d['house_type']= house_type[n]
    d['age']=age[n]
    d['area']=area[n]
    d['price']=price[n]
    d['perprice']=ave[n]
    d['room']=room[n][0]
    d['hall']=room[n][1]
    d['bathroom']=room[n][2]
    d['floor']=floor[n]
    d['total_floor']=total_floor[n]
    data1.append(d)
    
df = pd.DataFrame(data1)
df.to_csv("test.csv",encoding='utf8')