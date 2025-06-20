# By weight and value ratio first
# Knapsack problem using Greedy approach
def  Knapsack (wt , val , cap):
    items = [(i, wt[i], val[i] , val[i]/wt[i]) for i in range (len(wt))]
    items.sort(key = lambda x:x[3], reverse=True)
    
    total_profit = 0
    include_items = []
    
    
    for i , wt, profit, ratio in items:
        if cap >= wt:
            include_items.append((i,1))
            total_profit =total_profit+ profit
            cap = cap-wt
        else:
            frac = cap/wt
            total_profit = total_profit + (frac* profit)
            include_items.append((i, frac))
            
            
    return total_profit , include_items
        
    
    
wt = [30,20,10] 
val = [60,50,40]
cap = 50
   
print("By weight and value ratio first")
total_profit , include_items =Knapsack(wt ,val , cap)
print("total_profit is", total_profit)
print("include_items are", include_items)

# By highest profit first

def  Knapsack (wt , val, cap):
    items = [(i, wt[i], val[i] , wt[i]/val[i]) for i in range (len(wt))]
    items.sort(key = lambda x:x[2] ,reverse=True)
    
    total_profit = 0
    include_items = []
    
    
    for i , wt, profit, ratio in items:
        if cap >= wt:
            include_items.append((i,1))
            total_profit =total_profit+ profit
            cap = cap-wt
        else:
            frac = cap/wt
            total_profit = total_profit + (frac* profit)
            include_items.append((i, frac))
            
            
    return total_profit , include_items
        
    
    
wt = [30,20,10] 
val = [60,50,40]
cap = 50
   
print("By highest profit first")
total_profit , include_items =Knapsack(wt ,val , cap)
print("total_profit is", total_profit)
print("include_items are", include_items)


# By lowest weight first

def  Knapsack (wt , val , cap):
    items = [(i, wt[i], val[i] , wt[i]/val[i]) for i in range (len(wt))]
    items.sort(key = lambda x:x[1])
    
    total_profit = 0
    include_items = []
    
    
    for i , wt, profit, ratio in items:
        if cap >= wt:
            include_items.append((i,1))
            total_profit =total_profit+ profit
            cap = cap-wt
        else:
            frac = cap/wt
            total_profit = total_profit + (frac* profit)
            include_items.append((i, frac))
            
            
    return total_profit , include_items
        
    
    
wt = [30,20,10] 
val = [60,50,40]
cap = 50
   
print("By lowest weight first")
total_profit , include_items =Knapsack(wt ,val , cap)
print("total_profit is", total_profit)
print("include_items are", include_items)

