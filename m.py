

def media_serie(serie:list)->float:
        serie.append(0)
        suma_total = 0
        n = len(serie)
        i = 0
        print(serie)
        while serie[i] != 0:
            suma_total += serie[i]
            i += 1
        media = suma_total/(n-1)
        return media

a = [2,4,5,7,8,3]

print(media_serie(a))
