
import pyodbc

# Replace 'your_html_file.html' with the actual path to your HTML file
# Assuming your ACCDB file is named 'your_database.accdb'
database_path = r'tacnch\t\Tanakh.accdb'
def find_pasuk_by_name(name):
    # Extract first and last letters
    first_letter = name[0].upper()
    last_letter = name[-1].upper()

    # Connect to the Tanakh database
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+database_path+''
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # SQL query to find a verse that starts and ends with the specified letters
    sql_query = """
                SELECT *
FROM Tanakh
WHERE LEFT(pasuk_value, 2) =  ? AND RIGHT(pasuk_value, 1) = ?;

                """

    # Parameters for the SQL query
    params = (f' {first_letter}', f'{last_letter}')

    # Execute the query
    cursor.execute(sql_query, params)

    # Fetch the result
    results = cursor.fetchall()
    for result in results:
        result1=[]
        for res in result:
            result1.append(str(res).replace("\xa0\xa0",""))
        print(result1)
    # Close the database connection
    connection.close()

name=input("enter name\n")
find_pasuk_by_name(name)
