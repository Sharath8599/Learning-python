# creating lists
first_names=["Ainsley","Ben","Chani","Depak"]
preferred_size=["Small", "Large", "Medium"]

# access, add, remove, and modify list elements
preferred_size.append("Medium")
print(preferred_size)

# create a two-dimensional list
customer_data=[["Ainsley","Small",True],["Ben","Large",False],["Chani","Medium",True],["Depak","Medium",False]]
print(customer_data)

#access and modify two-dimensional list elements
customer_data[2][2]=False
customer_data[1].remove(False)

# combining two lists
customer_data_final=customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
