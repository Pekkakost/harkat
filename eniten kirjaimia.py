def eniten_kirjainta(mjono):
    eniten=""
    maara=0
    for i in mjono:
      
        if mjono.count(i)>eniten.count(""):
            eniten=i
       # elif mjono.count(i)==eniten.count(""):
       #     eniten=""+i

    return eniten





if __name__=="__main__":
    mjono = "abcccbddddd"
    print(eniten_kirjainta(mjono))
