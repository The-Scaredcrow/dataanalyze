import diagram
from data import create_data 

data_list = create_data()

print("amount of points in res:", len(data_list))
print("Första tio värdena:", data_list[:10])
