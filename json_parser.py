import json

# reading JSON file
with open("SystemViewClasses.json") as file:   
    text_data = file.read()
json_data = json.loads(text_data) 

def extracting_values_from_json(dictionary, key):
    """
    Function to iterate through the given nested JSON data 
    and find to obtain values for the given key.

    Args:
        dictionary (dict): Nested JSON data to be parsed.
        key (string): Key which will be iterated throughout the 
        nested JSON data to fetch corresponding values.

    Returns: 
        values (list): List of found values of the given key.
    """
    
    output_list = []

    def actual_extraction(dictionary, output_list, key):
        """
        Function to search values for the given key 
        recursively throughout the nested JSON.

        Args:
            dictionary (dict): Nested JSON data to be parsed.
            output_list (list): Empty list to add found values
            of the given key.
            key (string): Key which will be iterated throughout 
            the nested JSON data to fetch corresponding values.

        Returns:
            output_list (list): List of found values of the given key.
        """
        
        if isinstance(dictionary, dict):
            for k, v in dictionary.items():
                if isinstance(v, (dict, list)):
                    actual_extraction(v, output_list, key)
                elif k == key:
                    output_list.append(v)

        elif isinstance(dictionary, list):
            for item in dictionary:
                actual_extraction(item, output_list, key)

        return output_list

    values = actual_extraction(dictionary, output_list, key)
    return values

# while True:
def get_user_input():
    print("\n(Press Ctrl+C to break)\n")
    key = input("Enter the name of the key : ")
    print("\nEntered key = ", key+"\n")
    result = extracting_values_from_json(json_data, key)
    if len(result) == 0:
        print("OOPS! No values found for "+key+"!")
    else:
        print("Values of the key "+'"'+key+'"'+" are "+str(result))
    
if __name__ == '__main__':
    get_user_input()
    