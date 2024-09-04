# Find-Max-ID
# ArcGIS Python Script: Maximum Facility ID Finder

## Overview

This script is designed to find the current maximum numeric value in the "FACILITYID" field of a specific feature class within an ArcGIS geodatabase. This can be useful for maintaining unique identifiers in a geographic dataset, especially when adding new features and ensuring they have unique "FACILITYID" values.

## Requirements

ArcGIS Pro: This script uses the arcpy library, which is part of the ArcGIS software suite. Make sure ArcGIS Pro is installed and licensed on your system.
Python 3.x: Ensure Python is installed, and the arcpy package is available. This script also imports pandas, although it's not used in the provided snippet.
ArcGIS Environment: The script should be run within an environment that has access to ArcGIS geoprocessing tools.
## Installation

ArcGIS Pro: Install ArcGIS Pro from ESRI and ensure you have a valid license.
Python Environment: Use the Python environment that comes with ArcGIS Pro, which includes arcpy. You can manage your environment through the ArcGIS Pro interface or by using conda.
## Usage

Specify the Feature Class:

Modify the feature_class variable in the script to point to your specific feature class. ```python feature_class = r"Your\Path\To\FeatureClass.gdb\FeatureClassName" ```
The feature class path should be an absolute path pointing to a feature class within a geodatabase (.gdb).
Run the Script:

Execute the script in an environment where arcpy is available. The script will output the current maximum numeric value in the "FACILITYID" field.
Output:

The script prints the current maximum value in the "FACILITYID" field to the console: ``` Current Max ID <max_id> ``` Replace <max_id> with the actual maximum value.
## Example

Here's an example of how the script might be used:

```python import arcpy import pandas

Path to your feature class
feature_class = r"C:\Users\YourUserName\Documents\ArcGIS\Projects\YourProject\YourGeodatabase.gdb\YourFeatureClass"

Get the current maximum value in the FACILITYID field
max_id = max([int(row[0]) for row in arcpy.da.SearchCursor(feature_class, "FACILITYID") if row[0] is not None and row[0].isdigit()])

Print the result
print('Current Max ID') print(max_id) ```

## License

This script is provided "as-is" without any warranty. You are free to modify and distribute it as needed. Please ensure you have the appropriate licenses for any software used with this script.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.