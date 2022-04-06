# Hbase assignment 3

## Tasks

- 2) On our hbase-master container we created the table "foods" and set a column-family as "facts:". This will contain all of our food facts. We decided that the row key would be the "Food_Code" because the key has to be unique. For some alternative column families we could have implemented one called "Portion" since there are multiple columns that start with "portion", also a "ingredients" column family since a lot of these food items have several ingredients, and lastly a "nutritional" column family to highlight the nutritional values of the food item.
- 3) The code for importing the food data is located in this repository as "foods_script.py" and is coded in python. We utilize a "thrift-server" to communicate with our hbase-master container so that we can run python scripts locally on our machines. We use a python library called "Happybase" for this communication. Running this script populates our hbase database with the food data.
![scan](https://user-images.githubusercontent.com/56347030/161986330-22ebb8a8-e870-4b81-a4e8-eaa8d30f94bf.PNG)

- 4) We run a simple get query on the hbase master shell to retrieve data about a given food item. We supply the row key 55101000 which corresponds to a pancake, and we get the display name of this item.
![query](https://user-images.githubusercontent.com/56347030/161986760-ceddb183-31c8-4e46-a01e-486fed917c69.PNG)

To get the complete set of facts-data about the food item, we run the following query.
![query2](https://user-images.githubusercontent.com/56347030/161986903-6c78c64c-b62a-4ae8-bc4b-e9ee4e3ff089.PNG)

