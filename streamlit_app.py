# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothies! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your coutomized smoothie!"""
)

title = st.text_input("Name on smoothie:")
st.write("The name on your smoothie will be:", title)
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))

ingredients_list = st.multiselect('Choose up to 5 ingreidents:',my_dataframe, max_selections=5)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    st.write(ingredients_string) 

    my_insert_stmt = """ insert into smoothies.public.orders(name_on_order,ingredients)
            values ('""" + title + """','""" + ingredients_string + """')"""

    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        if ingredients_string:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered,'+title +'!', icon="✅")

        
#my_update_stmt = """ update smoothies.public.orders set ORDER_FILLED = 1 where 
#            values ('""" + ingredients_string + """','""" + title + """')"""

#st.write(my_insert_stmt)
#time_to_insert = st.button('Submit order')

#if time_to_insert:
#        session.sql(my_insert_stmt).collect()
        
#        st.success('Your Smoothie is ordered,'+title +'!', icon="✅")