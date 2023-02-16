# import relevant libraries
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# read the csv file

df = pd.read_csv('Certification.csv')
df['Date_Issued'] = pd.to_datetime(df['Date_Issued'], format="%Y-%m-%d")
df.sort_values(by='Date_Issued', ascending=False, inplace=True)
df.Issuing_Organization = df.Issuing_Organization.str.title().str.strip()
df.Certificate_Name = df.Certificate_Name.str.strip()
df.Credential_URL = df.Credential_URL.str.strip()
df.Certificate_ID = df.Certificate_ID.str.strip()


# saving the cleaned data to csv file 

df.to_csv('Certification.csv', index=False)

print("--- Certificate.csv is cleaned and saved ---")

df_output = df.copy()
df_output['Date_Issued'] = pd.to_datetime(df['Date_Issued'], format="%b %d, %Y").dt.strftime("%B %d, %Y")
df_output.Expiry_Date = df_output.Expiry_Date.fillna('NA')
df_output.Credential_URL = df_output.Credential_URL.apply(lambda x: "[Link]({})".format(x) if x else "NA")
df_output.Certificate_ID = df_output.Certificate_ID.fillna('NA')



output = ["| " for _ in range(df_output.shape[0] + 2)]

for col, label in [    
                   ('Certificate_Name', 'Certificate Name'), 
                   ('Issuing_Organization', 'Issuing Organization'), 
                   ('Date_Issued', 'Date Issued '),    
                   ('Expiry_Date','Expiry date'),  
                   ('Credential_URL', 'Credential URL'), 
                   ('Certificate_ID', 'Certificate ID')]:
    maximum_length = max(len(label), df_output[col].str.len().max())
  
    output[0] += str.ljust(label, maximum_length) + " | "
    output[1] += "-" * maximum_length +  " | "
    
    for n, val in enumerate(df_output[col].values):
        output[n+2] += str.ljust(val, maximum_length) + " | "





with open("README.md", 'w') as file:
    file.writelines("""# Certifications\n\n A platform where I park my bragging rights, safely stored for future reference and spontaneous show-and-tell sessions. Welcome to the station where my certificates catch the spotlight \n## Completed Courses\n\n""")
    file.writelines("\n".join(output))
    # to make the links open a new tab
    file.writelines("\n\n<base target='_blank'>")

print("--- New Certificates generated ---")