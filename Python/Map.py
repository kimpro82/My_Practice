def details(txt) :
    print("elements :", txt)
    print("type :", type(txt))
    try :
        print("elements' type :", type(txt[0]), "\n")
    except :
        print("elements' type : an error occurs.\n")

txt = "1 2 3 4 5"
details(txt)

txtsplit = txt.split()
details(txtsplit)

txtmap = map(int, txt.split())
details(txtmap) # an error occurs

txtlist = list(txtmap)
details(txtlist)
