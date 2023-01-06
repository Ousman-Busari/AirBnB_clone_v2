#!/usr/bin/python3

def main():
    classes = [
               'BaseModel', 'User', 'Place',
               'State', 'City', 'Amenity',
               'Review']

    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    args = "Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297"

    # scan for parameter inputing format i.e key="value" and
    # check if the first token in line is present in classes
    if "=" in args and args.split()[0] in classes:
        # extract the name of the class from the line
        _cls = args.split()[0]

        # create a list of parameters with the rest of the line
        params_list = args.split()[1:]

        # create am empty to dict to add the key-value pair after\
        # partitioning of each parameter from the list of parameters 
        params_dict = {}

        # partition each parameter into key and value and add the dict of parameters
        for param in params_list:
            key = param[:param.find("=")]
            value = param[param.find("=") + 1:]

            # replace underscores in value with spaces and remove the quotations
            value = value.replace("_", " ").replace('\"', "")

            # typecast the value to the right type
            if key in types:
                value = types[key](value)
                # print(type(value), value)

            # add the key-value pair to parameter dict
            params_dict[key] = value
        
        dic = {}
        if dic:
            print(params_dict)
      


if __name__ == "__main__":
    main()



        # initialize variables, extract the name of the class, and 
        # creat an empty dict where to keep the paramneters
        _cls = args.split()[0]
        params_dict = {} 

        # scan for parameter inputing format i.e key="value" and
        try:
            # create a list of parameters with and exclude the name class
            params_list = args.split()[1:]

            # partition each parameter into key and value and add the dict of parameters
            for param in params_list:
                if "=" in param:
                    key = param[:param.find("=")]
                    value = param[param.find("=") + 1:]

                    # replace underscores in value with spaces and remove the quotations
                    value = value.replace("_", " ").replace('\"', "")

                    # typecast the value to the right type
                    if key in HBNBCommand.types:
                        value = types[key](value)

                    # add the key-value pair to parameter dict
                    params_dict[key] = value
        except Exception as e:
            pass
        
        if params_dict == {}:
            new_instance = eval(_cls)()
        else:
            new_instance = eval(_cls)(**params_dict)
            