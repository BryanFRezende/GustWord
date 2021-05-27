def gen_random_index():
    city_id_arr = load('CityIdArray.npy')
    #print(city_id_arr[0])

    index = []
    for i in range(0,6):
        rand1 = np.random.choice(city_id_arr)
        rand2 = np.random.choice(city_id_arr)
        #print(rand1,rand2)

        get1 = requests.get("http://api.openweathermap.org/data/2.5/weather?id="+str(rand1)+"&appid=0b883368ad98922cf7b36a2c5b0be3a4")
        get2 = requests.get("http://api.openweathermap.org/data/2.5/weather?id="+str(rand2)+"&appid=0b883368ad98922cf7b36a2c5b0be3a4")

        full1 = get1.json()
        full2 = get2.json()
        #print(full1,full2)

        rwind1 = full1['wind']['speed'],full1['wind']['deg']
        rwind2 = full2['wind']['speed'],full2['wind']['deg']
        #print(rwind1,rwind2)

        crossprod = rwind1[0]*rwind2[0]*np.sin(rwind1[1]-rwind2[1])
        dotprod = rwind1[0]*rwind2[0]*np.cos(rwind1[1]-rwind2[1])
        genbase = crossprod + dotprod
        #print(genbase)

        if genbase < 0:
            genbase = -genbase
            #print(genbase)

        while genbase >= 10:
            genbase = genbase/random.randint(1,9)
            #print(genbase)

        gen = str(genbase)
        random_int = gen[0]
        index.append(random_int)
        #print(random_int)

    index = ''.join(index)
    return int(index)
