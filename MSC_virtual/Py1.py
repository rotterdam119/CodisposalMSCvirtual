import pandas as pd

# Ruta del archivo Excel
archivo = r"C:\Users\rcgr1\Desktop\MSC_GeotecVar\CodisposalMSCvirtual\MSC_virtual\MSC_Variables geotecnicas_21042025.xlsx"

# Leer la hoja específica "MSC_ID"
df = pd.read_excel(archivo, sheet_name="MSC_ID")

# Mostrar las primeras filas de la hoja
print("\n--- Contenido de la hoja MSC_ID ---")
print(df.head())