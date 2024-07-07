'''import streamlit as st


st.title("تطبيق برمجة Python")

# نص ترحيبي
st.write("مرحبًا بك في تطبيق البرمجة التفاعلي باستخدام Streamlit!")

# منطقة نص لكتابة الكود مع مفتاح فريد
code_area = st.text_area("اكتب الكود الخاص بك هنا:", key="code_area", height=200)

# زر لتنفيذ الكود
exec_button = st.button("تنفيذ الكود")

# تنفيذ الكود وعرض النتائج
if exec_button:
    try:
        exec(code_area)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")'''


#VIN
#streamlit run "D:\one drive\OneDrive\Desktop\Pro\Car_Price\Car_Prediction_Price.py"
#ctrl + c for stoping the terminal

import streamlit as st
import pandas as pd
import pickle



# Load the model
data = pickle.load(open(r"D:\one drive\OneDrive\Desktop\Pro\Car_Price\Car_Predictions.sav", 'rb'))

# Streamlit Page
st.title("Car Price Prediction")

# Display the loaded data
#st.write("Loaded model data:")
#st.write(data)

st.sidebar.header("Feature selection")
st.sidebar.info('Easy Application For Predicting Cares_Price')
st.image("D:\one drive\OneDrive\Desktop\Pro\Car_Price\car.jpg")

#----------------------------------------------


m1 = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
     'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
     'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
     'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
     'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
     'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
     'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
     'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
     'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
     'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
     'PONTIAC', 'SATURN', 'ASTON MARTIN']

m2 = [16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
      11, 42, 24, 32,  2,  8, 29, 10, 23, 20,  0, 44, 19, 39,  7, 25,  4,
      33, 47, 15,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]

manu_mapping = dict(zip(m1, m2))

manu1 = st.selectbox("Manufacturer", m1)
manu2 = manu_mapping[manu1]  # استخدام قيمة manu1 كمفتاح مباشرة

st.write(f"You selected: {manu1} with code {manu2}")

#--------------------------------------------------------

c1= ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup']
c2= [3, 4, 8, 9, 6, 0, 1, 5, 2, 7]

Category_mapping= dict(zip(c1,c2))
Category1= st.selectbox('Category',c1)
Category= Category_mapping[Category1]

#------------------------------------------------------------------------


l1= ['Yes', 'No']
l2= [0, 1]

Leather_interior_mapping= dict(zip(l1,l2))
Leather_interior1= st.selectbox('Leather interior',l1)
Leather_interior= Leather_interior_mapping[Leather_interior1]

#-------------------------------------------------------------------------

f1= ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG',
       'Hydrogen']
f2= [4, 2, 1, 5, 3, 0]

Fuel_type_mapping= dict(zip(f1,f2))
Fuel_type1= st.selectbox('Fuel type',f1)
Fuel_type= Fuel_type_mapping[Fuel_type1]

#-------------------------------------------------------------------------

g1= ['Automatic', 'Tiptronic', 'Variator', 'Manual']
g2= [3, 0, 2, 1]

Gear_box_type_mapping= dict(zip(g1,g2))
Gear_box_type1= st.selectbox('Gear box type',g1)
Gear_box_type= Gear_box_type_mapping[Gear_box_type1]

#-------------------------------------------------------------------------

d1= ['4x4', 'Front', 'Rear']
d2= [1, 0, 2]

Drive_wheels_mapping= dict(zip(d1,d2))
Drive_wheels1= st.selectbox('Drive wheels',d1)
Drive_wheels= Drive_wheels_mapping[Drive_wheels1]

#-------------------------------------------------------------------------

w1= ['Left wheel', 'Right-hand drive']
w2= [1, 0, 2]

Wheel_mapping= dict(zip(w1,w2))
Wheel1= st.selectbox('Wheel',w1)
Wheel= Wheel_mapping[Wheel1]


#---------------------------------------------------------------------

co1= ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
co2= [ 1, 14, 12,  7,  2, 13, 11,  8,  6, 15,  3,  5,  0,  4, 10,  9]

Color_mapping= dict(zip(co1,co2))
Color1= st.selectbox('Color',co1)
Color= Color_mapping[Color1]

#--------------------------------------------------------------------

Engine_volume= st.selectbox("Engine volume",[1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
       1.9, 2.7, 3.5, 2.1, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1])

#--------------------------------------------------------------------

Airbags = st.selectbox("Airbags",[ 2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13])

#--------------------------------------------------------------------

Age= st.number_input("Age")
Mileage= st.number_input("Mileage")
Levy= st.number_input("Levy")

# Data Frame with all data

df=pd.DataFrame({"Manufacturer":manu2,
              "Category":Category,
              "Leather interior":Leather_interior,
              "Fuel type":Fuel_type,
              "Gear box type":Gear_box_type,
              "Drive wheels":Drive_wheels,
              "Wheel":Wheel,
              "Color":Color,
              "Engine volume":Engine_volume,
              "Airbags":Airbags,
              "Age":Age,
              "Mileage":Mileage,
              "Levy":Levy},index=[0])

st.write("Feature names used during training:")
st.write(data.feature_names_in_)
st.write("Feature names used during prediction:")
st.write(df.columns)

# Predict Price
p = st.sidebar.button("Predict Price")
if p:
    try:
        pre = data.predict(df)
        st.sidebar.write("Price is:", pre)
    except ValueError as e:
        st.sidebar.error(f"Error: {e}")