import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from numpy.random import seed
from numpy.random import randint

def operationOfCurrentPoint(sumOfSurviver, i, j):  
    if(orgGrid[i, j] == 255): # current point survive
        if(sumOfSurviver <= 1):
            tmpGrid[i, j] = 0        
        elif(sumOfSurviver <= 3):
            pass
        else:
            tmpGrid[i, j] = 0
    else:
        if(sumOfSurviver == 3):
            tmpGrid[i, j] = 255
        else:
            pass    

def checkSurrounding(i, j):
    sumOfSurviver = 0
    
    if(i-1 >= 0 and j-1 >= 0 and orgGrid[i-1, j-1] == 255): # left-up
        sumOfSurviver += 1
    if(i-1 >= 0 and orgGrid[i-1, j] == 255): # up
        sumOfSurviver += 1
    if(i-1 >= 0 and j+1 < gridSize and orgGrid[i-1, j+1] == 255): # right-up
        sumOfSurviver += 1
    if(j-1 >= 0 and orgGrid[i, j-1] == 255): # left
        sumOfSurviver += 1
    if(j+1 < gridSize and orgGrid[i, j+1] == 255): # right      
        sumOfSurviver += 1
    if(i+1 < gridSize and j-1 >= 0 and orgGrid[i+1, j-1] == 255): # left-down
        sumOfSurviver += 1
    if(i+1 < gridSize and orgGrid[i+1, j] == 255): # down
        sumOfSurviver += 1
    if(i+1 < gridSize and j+1 < gridSize and orgGrid[i+1, j+1] == 255): # right-down  
        sumOfSurviver += 1 
   
    operationOfCurrentPoint(sumOfSurviver, i, j)
    
def update(self):
    #sumOfSurviver = 0
    global orgGrid, tmpGrid
    tmpGrid = orgGrid.copy()
    for i in range(gridSize):
        for j in range(gridSize):
            checkSurrounding(i, j)
            
    mat.set_data(tmpGrid)
    orgGrid = tmpGrid 
    return [mat]    
    
def main():
    global mat, orgGrid, gridSize
    
    gridSize = 100
    vals = [255, 0]
    orgGrid = np.random.choice(vals, gridSize*gridSize, p=[0.2, 0.8]).reshape(gridSize, gridSize)
    
    figure, axes = plt.subplots()
    mat = axes.matshow(orgGrid)
    ani = animation.FuncAnimation(figure, update, interval=50, save_count=50)
    plt.show()          
                
        

if __name__ == "__main__":
    main()
