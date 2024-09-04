'''Find Max ID for text field in an arcgis pro feature class'''
import arcpy

feature_class = r"C:\Users\Nolan\Documents\ArcGIS\ArcGIS Pro Projects\DateDelete\DateCleanUpDelete\GISDBSERVER22.sde\HUD_LGIM.DBO.WaterDistribution\HUD_LGIM.DBO.wServiceConnection"

# Get the current maximum value in the field

'''if row[0] is not None and row[0].isdigit(): This condition filters out any None values and ensures that only numeric strings are considered, which can be converted to integers.'''

max_id = max([int(row[0]) for row in arcpy.da.SearchCursor(feature_class, "FACILITYID") if row[0] is not None and row[0].isdigit()])

print('Current Max ID')
print(max_id)
