class HashTable:
    
    def __init__(self):
        self.m = 10
        self.arr = [None for i in range(self.m)]
    
    def hashFunction(self,data):
        m = 10
        value_sum = 0
        # loop through the data
        for char in data:
        # find the ascii for each character
        # summation of all the ascii values
            value_sum+=ord(char)
        # Finally finding key --> value%m
        key_value = value_sum%m
        
        return key_value 
    
    def set_item(self,data):
        # send the data to the hashfunction and get the key 
        hash_key = self.hashFunction(data)
        # Now using the key insert the data into the hash table
        self.arr[hash_key] = data
        return
    
    def get_item(self,data):
        # send the data to the hashfunction and get the key 
        hash_key = self.hashFunction(data)
        return self.arr[hash_key]
    
    
        
result = HashTable()
print(result.arr)
result.set_item('March 2025')
print(result.arr)
print(result.get_item('March 2025'))