import streamlit as st
import datetime
import pandas as pd
import sqlite3

st.title(':blue[_TravellerApp_] :sunglasses:')
d = st.date_input(
    "Date of Travel",
    datetime.date(2019, 7, 6))

number_of_travellers = int(st.number_input('Number of Travellers'))
travellers_info={}
if number_of_travellers:
    for i in range(1,number_of_travellers+1):
        name,amount= st.columns(2)
        traveller_name = st.text_input(str(i)+'name')
        name.write(traveller_name)
        contro_amount = st.number_input(str(i)+'contribution')
        amount.write(contro_amount) 
        travellers_info[traveller_name]=[contro_amount]

    df= pd.DataFrame(travellers_info)
    df1= df.copy()
    st.info('Travellers Info')
    st.write(df)
    st.write('---------')

    df['Total Spent']=df.sum(axis=1)
    st.markdown(":green[Contribution] :pencil:")
    st.write(df)

    amount_per_person= df['Total Spent'].iloc[0]/number_of_travellers
    st.write(f'Amount_per_person 💰',amount_per_person)

    df2=amount_per_person-df1

    df2['Total']=df2.sum(axis=1)
    #df2= amount_per_person- df1.loc[0:]
    st.write('--------')
    st.markdown(":black[Who has to pay how much! 💰💸]")
    st.write(df2)

    if st.button('Save this Data'):
        conn = sqlite3.connect('travellers.db')
        # Create a cursor object to execute SQL commands
        c = conn.cursor()
        
        # Create a table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS travellers_data (
            id INTEGER PRIMARY KEY,
            number_of_travellers INTEGER,
            amount_per_person FLOAT
        )
        '''
        c.execute(create_table_query)

        # Insert the data into the database
        c.execute('INSERT INTO travellers_data (number_of_travellers,amount_per_person) VALUES (?,?)', (number_of_travellers,amount_per_person))
        
        #df.to_sql('travellers_data', conn, if_exists='replace', index=False)
        #df2.to_sql('travellers_data', conn, if_exists='replace', index=False)
        # Commit the transaction (save the changes to the database)
        conn.commit()

        # Close the connection
        conn.close()
        st.success('Data Saved!')
        st.balloons()
    else:
        pass
