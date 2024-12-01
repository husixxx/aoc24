def main():
    first = []
    second = []
    empty = 0
    odd = 0
    with open('data.txt', 'r') as file:
       obsah = file.readlines()
       for i in obsah:
            lanes = i.split()
            for lane in lanes:
                odd += 1
                if(odd % 2 == 0):
                    second.append(lane)
                else:
                    first.append(lane)
    
    rozdil = 0
    first.sort()
    second.sort()                    
    for i in first:
        similarity = 0
        
        for j in second:
            if(i == j):
                similarity += 1
                
        rozdil += similarity * int(i)
        
    print(rozdil)
                
                
                
        

if __name__ == "__main__":
    main()