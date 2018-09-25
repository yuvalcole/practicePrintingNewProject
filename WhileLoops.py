while True:
    gross = input("Gross:")
    kids = input("kids:")
    try:
        gross=int(gross)
    except:
        print("invalid")
        continue
        try:
            intKids=int(kids)
        except:
            print("invalid")
            continue
        if gross<0 or kids<0 or kids>50:
                print("invalid")
                continue
        if intkids!=float(kids):
            print("invalid")
            continue


      break;

