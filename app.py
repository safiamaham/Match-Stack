# import streamlit as st #streamlit - Front end framework
# import pandas as pd #data wrangling library in python
# import plotly.express as px #Dynamic Visualization library in python


# st.title("E-commerce Sales analysis Dashboard")

# # data=pd.read_csv("supermarket_sales.csv")

# # st.dataframe(data)


# def load_data(file_path):
#     data=pd.read_csv(file_path)
#     data["Date"]=pd.to_datetime(data["Date"],errors="coerce")
#     data=data.dropna(subset=["Date"]) #remove with invalid dates
#     data["Branch"]=data["Branch"].replace("A","Gulshan")
#     data["Branch"]=data["Branch"].replace("B","Johar")
#     data["Branch"]=data["Branch"].replace("C","Saddar")
#     return data

# data_path="./supermarket_sales.csv"

# data= load_data(data_path)
# st.sidebar.header("Filters")


# #data=pd.read_csv("supermarket_sales.csv")

# #st.dataframe(data)


# select_branch=st.sidebar.multiselect("Select Branch",options=data["Branch"].unique())
# select_product=st.sidebar.multiselect("Select Product",options=data["Product line"].unique())
# select_customer=st.sidebar.multiselect("Select Customer Type",options=data["Customer type"].unique())
# select_gender=st.sidebar.multiselect("Select Gender",options=data["Gender"].unique())

# filtered_data= data[(data["Branch"].isin(select_branch)) & (data["Product line"].isin(select_product)) & (data["Customer type"].isin(select_customer)) & (data["Gender"].isin(select_gender))]

# st.dataframe(filtered_data)

# total_sales=filtered_data["Total"].sum().round(2)
# gross_income=filtered_data["gross income"].sum().round(2)
# total_cogs=filtered_data["cogs"].sum().round(2)
# ave_rating=filtered_data["Rating"].mean().round(2)
# total_quantity=filtered_data["Quantity"].sum().round(2)
# cust_count=filtered_data["Invoice ID"].nunique()

# st.subheader("Key Metrics")

# col1,col2,col3,col4,col5,col6 = st.columns(6)

# with col1:
#     st.metric(label="Customer Count",value=cust_count)

# with col2:
#     st.metric(label="Total Sales",value=total_sales)

# with col3:
#     st.metric(label="Gross Income",value=gross_income)

# with col4:  
#     st.metric(label="Average Rating",value=ave_rating)

# with col5:
#     st.metric(label="Total Quantity",value=total_quantity)

# with col6:
#     st.metric(label="Total Costs on goods",value=total_cogs)
# # sales_by_gender=filtered_data.groupby("Gender")["Total"].sum().sort_values().reset_index()
# # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By Gender::::::::::::::::::::::::::::")
# # fig_Gender=px.bar(
# #     sales_by_gender,
# #     x="Gender",
# #     y="Total",
# #     title="Total Sales By Gender",
# #     text="Total",
# #     color="Gender"
# # )
# # st.plotly_chart(fig_Gender)

# # sales_by_branch=filtered_data.groupby("Branch")["Total"].sum().sort_values().reset_index()
# # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By Branch::::::::::::::::::::::::::::")
# # fig_branch=px.bar(
# #     sales_by_branch,
# #     x="Branch",
# #     y="Total",
# #     text="Total",
# #     color="Branch"
# # )
# # st.plotly_chart(fig_branch)

# # sales_by_city=filtered_data.groupby("City")["Total"].sum().sort_values().reset_index()
# # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By City::::::::::::::::::::::::::::")
# # fig_city=px.bar(
# #     sales_by_city,
# #     x="City",
# #     y="Total",
# #     text="Total",
# #     color="City"
# # )
# # st.plotly_chart(fig_city)

# # sales_by_city = filtered_data.groupby("City")["Total"].sum().sort_values().reset_index()

# # # 2. Add the subheader
# # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By City::::::::::::::::::::::::::::")

# # # 3. Create the pie chart
# # # 'names' defines the labels for each slice, 'values' defines the size of the slices
# # fig_city_pie = px.pie(
# #     sales_by_city,
# #     values="Total",
# #     names="City",
# #     title="Sales Distribution by City",
# #     hole=0.4  # Optional: adds a center hole to make it a donut chart
# # )

# # # 4. Display the chart in Streamlit
# # st.plotly_chart(fig_city_pie, use_container_width=True)

# col7,col8=st.columns(2)

# sales_by_gender=filtered_data.groupby("Gender")["Total"].sum().sort_values().reset_index()
# # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By Gender::::::::::::::::::::::::::::")

# with col7:
# #     sales_by_gender=filtered_data.groupby("Gender")["Total"].sum().sort_values().reset_index()
# #     st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By Gender::::::::::::::::::::::::::::")
#     fig_Gender=px.bar(
#         sales_by_gender,
#         x="Gender",
#         y="Total",
#         title="Total Sales By Gender",
#         text="Total",
#         color="Gender"
#     )
#     st.plotly_chart(fig_Gender)
# sales_by_branch=filtered_data.groupby("Branch")["Total"].sum().sort_values().reset_index()
# # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By Branch::::::::::::::::::::::::::::")
# with col8:
#     # sales_by_branch=filtered_data.groupby("Branch")["Total"].sum().sort_values().reset_index()
#     # st.subheader(":::::::::::::::::::::::::::::::::::Total Sales By Branch::::::::::::::::::::::::::::")
#     fig_branch=px.bar(
#         sales_by_branch,
#         x="Branch",
#         y="Total",
#         text="Total",
#         color="Branch"
#     )
#     st.plotly_chart(fig_branch)
# # 'names' defines the labels for each slice, 'values' defines the size of the slices
# sales_by_city = filtered_data.groupby("City")["Total"].sum().sort_values().reset_index()

# fig_city_pie = px.pie(
#     sales_by_city,
#     values="Total",
#     names="City",
#     title="Sales Distribution by City",
#     hole=0.4  # Optional: adds a center hole to make it a donut chart
# )

# # 4. Display the chart in Streamlit
# st.plotly_chart(fig_city_pie, use_container_width=True)






# new data 

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
st.title("Cricket Data Analysis")
# Load the dataset
df=pd.read_csv("newfile.csv")

#---------NAVIGATION BAR----------------#
selected = option_menu(
    menu_title=None,
    options=["Home", "Player Analysis","Country Insights","Comparison","Data Explorer"],
    icons=["house","person","globe","bar-chart","table"],
    orientation="horizontal"
)
 #----- Home Page----#

if selected == "Home":
    st.title("Cricket Analysis Dashboard")
    col1,col2,col3 = st.columns(3)
    col1.metric("Total Player", df["Player"].nunique())
    col2.metric("Total Runs", df["Runs"].sum())
    col3.metric("Countries", df["Country"].nunique())
    st.dataframe(df.head())

#------ Player Analysis-------#

elif selected == "Player Analysis":
    st.title("Player Analysis")
    player = st.selectbox("Select Player", df["Player"])
    pdata = df[df["Player"]== player].reset_index()

    values=pdata[["100","50","4s","6s"]].iloc[0]

    fig=px.bar(
        x=values,
        y=values.index
    )

    fig.update_xaxes(range=[0, values.max() + 20])


    # stats=["100","50","4s","6s"]
    # chart_data =(
    #     pdata[stats]
    #     .iloc[0]
    #     .reset_index()
    # )
    # chart_data.columns = ["Stat","Value"]

    # fig=px.bar(
    #     chart_data,
    #     x="Stat",
    #     y="Value",
    # ) 
    col4,col5,col6,col7 = st.columns(4)
    total_runs = pdata["Runs"].sum()
    total_matches = pdata["Matches"]
    hundreds = pdata["100"].sum()
    sixties = pdata["6s"].sum()
    col4.metric(label="Total Runs", value=total_runs)
    col5.metric(label="Total Matches", value=total_matches)
    col6.metric(label="Total 100s", value=hundreds)
    col7.metric(label="Total 6s", value=sixties)
    st.plotly_chart(fig, use_container_width=True)
    
#------ Country Insights-------#

elif selected == "Country Insights":
    st.title("Country Insights")
    country_runs = df.groupby("Country")["Runs"].sum().reset_index()
    fig=px.pie(
        country_runs,
        names="Country",
        values="Runs",
    )
    st.plotly_chart(fig, use_container_width=True)

#------ Comparison-------#
elif selected == "Comparison":
    st.title("Player Comparison")
    players = st.multiselect(
        "Compare Players",
        df["Player"],
        default=df["Player"].head(5)
    )
    compare=df[df["Player"].isin(players)]
    fig=px.scatter(
        compare,
        x="Strike_rate",
        y="Ave",
        size="Runs",
        color="Country",
    )
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Data Explorer":
        st.title("Data Explorer")
        st.dataframe(df)