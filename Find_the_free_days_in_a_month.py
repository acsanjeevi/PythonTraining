#Return the list of free days by using Function
total_occupied=0
booked_days=[1,3,9,12,13,18,26,27,28,29]
travel_days=[4,5,15,16,21,22]


def find_freedays():
    total_occupied=booked_days +travel_days
    total_occupied.sort()
   # print(total_occupied)
    listofdaysfree = [days for days in range(int(max(0,31)+1))
                    if days not in total_occupied]
    del listofdaysfree[0]
    print("List of free days: ", listofdaysfree)

find_freedays()
    

                
            
    

    

    


    


