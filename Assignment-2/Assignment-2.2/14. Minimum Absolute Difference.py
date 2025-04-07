#Problem 1200

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini = abs(arr[0]-arr[1])   
        
        lst =[[arr[0],arr[1]]]      
        
        i,j = 1,2
        
        while(i<len(arr)-1):                     
            
            diff=abs(arr[i]-arr[j])               
            
            if diff<mini:
                lst=[[arr[i],arr[j]]]            
                mini=diff
                
            elif diff == mini:
                lst+=[[arr[i],arr[j]]]          
