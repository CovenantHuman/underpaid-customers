MELON_COST = 1.00 #global variable for melon price

def order_discrepancies(file): #function declaration

    orders = open(file) #opening the relevant file
    for line in orders: #loops through each line in the file
        line = line.rstrip() #removes unnecessary whitespace on the right
        order_id, customer_name, melons, paid = line.split('|') #splits on | and assigns results to named variables

        first_name = customer_name.split(" ")[0] #getting just the customer's first name
        melons = int(melons) #make melons an int(because we don't currently sell partial melons)
        paid = float(paid) #make amount paid into a float because it's money

        expected = melons * MELON_COST #calculated expected payment for melons in this line
        
        print(f"{customer_name} paid ${paid:.2f},", #a summary of what the customer paid ...
        f"expected ${expected:.2f}" #...and what they should have paid 
        ) #parenthesis on a seperate line for style reasons

        if expected > paid: #check if customer underpaid
            print(f"{first_name} underpaid by ${expected-paid:.2f}") #a statement of who underpaid and by how much
        elif expected < paid: #check if customer overpaid
            print(f"{first_name} overpaid by ${paid-expected:.2f}") #a statement of who overpaid and by how much

    orders.close() #closing the document politely

order_discrepancies("customer-orders.txt") #calling the function with the provided file