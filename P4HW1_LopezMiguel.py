# CTI-110 
# P4HW1 - Distance traveled
# Miguel Lopez 
# 3/25/2018
#

def main():
    # Set variables

    vehicleSpeed = float( input( "What is the speed of the vehicle in mph? "))
    timeTraveled = int( input( "How many hours has it traveled? "))
    print("Hour   ", "Distance Traveled")
    print("--------------------------")
    
    # Formula and loop
    
    for hour in range(1, timeTraveled + 1):
            
        distanceTraveled = vehicleSpeed * hour
        print( hour, "         ", distanceTraveled)


main()
        
        


