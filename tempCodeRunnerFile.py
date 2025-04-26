import pandas as pd
# from sqlalchemy import  create_engine

# # Correct connection string with port
# conn_string = 'postgresql://postgres:ganpatibappamouriya@localhost/Creditcard_P'  
# db = create_engine(conn_string)
# conn = db.connect()

# # List of files to import
# Files = ["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", 
#  "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", 
#  "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", 
#  "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"]

# for file in Files:
#     # Corrected file path
#     file_path = f'C:\\Users\\muska\\Desktop\\Power Bi\\Credit_Card_Dashboard{file}.csv'
#     df = pd.read_csv(file_path)
#     df.to_sql(file,con=conn,if_exists='replace',index=False)
