import os

def printDownMost(path):
    ind = 0
    lst = []
    total = 0
    x = True
    for dirpath, dirnames, filenames in os.walk(path):
        if dirnames:
            temp = dirnames
            ind=0
            x=True
        else:
            if ind>=(len(temp)):
                ind=0
            else:
                currentFolder = temp[ind]
                if not currentFolder in ["Fizik","Kimya","Fizyoloji veya Tip","Edebiyat","Baris","Ekonomi"]:
                    if currentFolder in lst:
                        if x == True:
                            lst.append(currentFolder)
                            print(lst[len(lst)-1])
                            total = total + 1
                            x=False
                    else:
                        lst.append(currentFolder)
                        print(lst[len(lst)-1])
                        total = total + 1
                        x=False
                    ind = ind + 1        
                       
    print("Total number of root directories is {}!".format(total))
    
               
    
