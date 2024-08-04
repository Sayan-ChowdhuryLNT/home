
import sqlite3




def func():
    
    conn = sqlite3.connect('C:\\Users\\Sayan\\Downloads\\Vendor_Engineering\\WETDESK2-Vendor_Engineering\\instance\\database.sqlite3')
    cursor = conn.cursor()

     # the index 4 is for 'item_vendor_code'

    # Check if any row with the same job_code and item_vendor_code exists
    cursor.execute("SELECT item_vendor_code FROM pr_data__project")
    existing_row = cursor.fetchall()  
    for row in existing_row:
        for j in row:
            
            item_vendor_code = j.replace(" ", "") if j else None
            print(item_vendor_code)
            
    # print(item_vendor_code)
            cursor.execute("""
                        UPDATE pr_data__project 
                        SET item_vendor_code=?
                    """,item_vendor_code )


    conn.commit()  # Commit the changes to the database
    conn.close()
func()       
        