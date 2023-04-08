import requests


while True:
    response = requests.get('https://api.genelpara.com/embed/doviz.json')
    data = response.json()
    ls = []
    for i in data:
        ls.append(i) 
    print('Alınabilecek Değerler' +' : ' + 'TRY,' + ','.join(ls) + '\n' + '****************************************************************')
    doviz1 = str(input('Döviz Giriniz : ').upper().replace(' ', ''))
    doviz2 = str(input('Döviz Giriniz : ').upper().replace(' ', ''))


    if doviz2 == 'TRY':
        Para = float(data[doviz1]['satis'])
        miktar = input('Miktar Girmek İsterseniz giriniz : ')
        try:
            miktar = int(miktar)
            multiply = miktar * Para
            print("1 {0} = {1:.4f} {2}\n{3} {0} ise yaklaşık {4} {2} eder. ".format(doviz1,Para,doviz2,miktar,int(multiply)),sep='')
        except:
            print('1 {} = {} {}'.format(doviz1,Para,doviz2))
    else:
        if doviz1 == 'TRY':
            kur2 = float(data[doviz2]['satis'])

            result = 1 / kur2

            miktar = input('Miktar Girmek İsterseniz giriniz : ')
            try:
                miktar = int(miktar)
                multiply = miktar * result
                print("1 TL = {0:.4f} {1}\n{2} TL ise aşağı yukarı {3:.1f} {1} eder.".format(result,doviz2,miktar,multiply))
            except:
                print("1 TL = {:.4f} {}".format(result,doviz2))

        else:

            kur1 = float(data[doviz1]['satis'])
            kur2 = float(data[doviz2]['satis'])
            result = kur1 / kur2
            
            miktar = input('Miktar Girmek İsterseniz giriniz : ')

            try:
                miktar = int(miktar)
                multiply = miktar * result
                print("1 {0} = {1:.4f} {2}\n{3} {0} ise aşağı yukarı {4:.1f} {2} eder ".format(doviz1,result,doviz2,miktar,multiply))
            except:
                print("1 {} = {:.4f} {}".format(doviz1,result,doviz2))