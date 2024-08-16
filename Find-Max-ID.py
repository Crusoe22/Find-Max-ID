#Find Max ID

import arcpy 


# Define the path to your feature class
feature_class = r"path\to\your\geodatabase.gdb\water_service_connections"

# Initialize a variable to store the highest number
max_facility_id = None

# Use a search cursor to iterate through the rows in the feature class
with arcpy.da.SearchCursor(feature_class, ["FACILITYID"]) as cursor:
    for row in cursor:
        try:
            # Convert the FACILITYID field to an integer
            facility_id = int(row[0])
            
            # Update max_facility_id if the current facility_id is higher
            if max_facility_id is None or facility_id > max_facility_id:
                max_facility_id = facility_id
        except ValueError:
            # If conversion fails, skip this row
            continue

# Print the highest FACILITYID found
if max_facility_id is not None:
    print(f"The highest FACILITYID is: {max_facility_id}")
else:
    print("No valid numeric FACILITYID values were found.")