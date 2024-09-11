import streamlit as st
import requests
import json

# Function to send requests to the API
def send_request(payload):
    url = "http://localhost:5000/invocations"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# Layout the Streamlit app
st.title('Obesity Prediction')

# User input fields
age = st.slider("Age", 14, 61, 21)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.slider("Height in centi-meters", 100, 200, 100)
weight = st.slider("Weight in lbs", 30, 200, 168)
calc = st.selectbox("How often do you drink alcohol ?", ["no", "Sometimes", "Frequently", "Always"])
favc = st.selectbox("Do you eat High caloric Food ?", ["no", "yes"])
family_history_with_overweight = st.selectbox("Do you have Family History with over weight ?", ["no", "yes"])
fcvc = st.selectbox("Do you eat vegetables ?", ["yes", "no"])
ncp = st.slider("How many main meals do you take ?", 1,4,3)
caec = st.selectbox("Do you consume food between meals ?", ["no", "Sometimes", "Frequently", "Always"])
scc = st.selectbox("Do you monitor calorie consumption ?", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do you smoke ?", ["yes", "no"])
ch20 = st.slider("How many Litres of water do you drink daily", 1, 4, 2)
faf = st.slider("Physical activity frequency ?", 0,3,1)
tue = st.slider("Time Using Technology Devices ?",0,2,1)
mtrans = st.selectbox("Transportation Used",["Automobile","Motorbike","Bike","Public_Transportation","Walking"])

options_to_values = {
    "no": 2,
    "Sometimes": 3,
    "Frequently": 4,
    "Always": 5
}

options_trans= {
    "Automobile": 2,
    "Motorbike": 3,
    "Bike": 4,
    "Public_Transportation": 5,
    "Walking": 6
}

# Construct the payload
payload = {
    'inputs': {
        'Age': age, 
        'Gender': 2 if gender == "Female" else 3, 
        'Height': height/100, 
        'Weight': weight, 
        'CALC': options_to_values[calc], 
        'FAVC': 2 if favc == "no" else 3,
        'FCVC': 2 if fcvc == "no" else 3,
        'NCP': ncp,
        'SCC': options_to_values[scc], 
        'SMOKE': 2 if smoke == "no" else 3, 
        'CH2O': ch20,
        'family_history_with_overweight':  2 if family_history_with_overweight == "no" else 3, 
        'FAF': faf, 
        'TUE': tue,
        'CAEC': options_to_values[caec], 
        'MTRANS': options_trans[mtrans],
    }
}

prediction_map = {
        2: "Normal_Weight", 
        3: "Overweight_Level_I",
        4: "Overweight_Level_II",
        5: "Obesity_Type_I",
        6: "Insufficient_Weight",
        7: "Obesity_Type_II",
        8: "Obesity_Type_III"
    }

# Button to send the payload to the API
if st.button('Predict'):
    response = send_request(payload)
    number = response['predictions'][0]
    st.write(f"Result: {prediction_map[response['predictions'][0]]}")
    st.write("Recommendations:")
    if(number==2):
        st.write("""Diet: Maintain a balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats. Ensure adequate intake of essential nutrients to support overall health.
\n Exercise: Continue regular physical activity, including a mix of aerobic exercises (e.g., running, cycling) and strength training exercises (e.g., weightlifting).
\n Lifestyle: Maintain healthy habits such as regular sleep patterns, stress management, and avoiding smoking or excessive alcohol consumption.
\n Monitoring: Regularly monitor weight and BMI to ensure it remains within the normal range. Annual health check-ups are recommended.
""")
    if(number==3):
        st.write("""Diet: Adopt a balanced, calorie-controlled diet. Reduce the intake of processed foods, sugary beverages, and high-fat foods. Focus on whole foods such as fruits, vegetables, lean proteins, and whole grains.
\n Exercise: Increase physical activity with a combination of aerobic exercises and strength training. Aim for at least 150 minutes of moderate-intensity exercise per week.
\n Lifestyle: Develop healthy eating habits, manage stress, and ensure regular sleep. Avoid smoking and limit alcohol consumption.
\n Monitoring: Regularly monitor weight, BMI, and other health indicators. Consider seeking support from a nutritionist or dietitian.
""")
    if(number==4):
        st.write("""Diet: Follow a structured meal plan focusing on nutrient-dense foods and portion control. Limit intake of high-calorie, high-fat, and high-sugar foods.
\n Exercise: Engage in regular physical activity, including both aerobic exercises and strength training. Aim to increase exercise duration and intensity gradually.
\n Lifestyle: Adopt a healthy lifestyle with regular sleep, stress management, and avoidance of smoking and excessive alcohol consumption.
\n Monitoring: Regularly monitor weight, BMI, and other health metrics. Work with a healthcare provider to create a personalized weight management plan.
""")
    if(number==5):
        st.write("""Diet: Follow a medically supervised diet plan designed to reduce calorie intake while ensuring nutritional adequacy. Emphasize whole, unprocessed foods.
\n Exercise: Engage in a structured exercise program with a focus on both aerobic and strength training exercises. Aim for 200-300 minutes of moderate-intensity exercise per week.
\n Lifestyle: Implement lifestyle changes such as regular sleep patterns, stress reduction techniques, and avoiding smoking and alcohol.
\n Monitoring: Regularly monitor weight, BMI, blood pressure, and other relevant health indicators. Consult with healthcare providers regularly for ongoing support and adjustment of the plan.
""")
    if(number==6):
        st.write("""Diet: Increase caloric intake with nutrient-dense foods. Focus on incorporating healthy fats (e.g., avocados, nuts), complex carbohydrates (e.g., whole grains), and proteins (e.g., lean meats, dairy).
\n Exercise: Engage in strength training exercises to build muscle mass. Avoid excessive cardiovascular exercise that may lead to further weight loss.
\n Lifestyle: Ensure adequate sleep and reduce stress levels. Avoid smoking and excessive alcohol consumption.
\n Monitoring: Regularly monitor weight and BMI. Consult with a healthcare provider to rule out any underlying health conditions.
""")
    if(number==7):
        st.write("""Diet: Follow a comprehensive, medically supervised diet plan that includes calorie restriction and nutrient-dense foods. Consider working with a dietitian for personalized guidance.
\n Exercise: Increase physical activity with a combination of aerobic exercises, strength training, and flexibility exercises. Aim for consistent and gradually increasing exercise routines.
\n Lifestyle: Adopt significant lifestyle changes including regular sleep, effective stress management, and cessation of smoking and alcohol.
\n Monitoring: Regularly monitor weight, BMI, and other health markers. Engage with healthcare providers for ongoing support and adjustments to the weight management plan.
""")
    if(number==8):
        st.write("""Diet: Implement a medically supervised, very-low-calorie diet (VLCD) if recommended by a healthcare provider. Focus on nutrient-dense, low-calorie foods.
\n Exercise: Engage in a carefully structured exercise program tailored to individual capabilities, with a focus on low-impact aerobic exercises and gradual introduction of strength training.
\n Lifestyle: Make substantial lifestyle modifications, including regular sleep, stress management, smoking cessation, and minimal alcohol consumption.
\n Monitoring: Regularly monitor weight, BMI, blood pressure, and other critical health indicators. Frequent consultations with healthcare providers are essential for ongoing support, potential medical interventions, and necessary adjustments to the weight management plan.
""")
    # Assuming the response contains a 'prediction' key and its value is a list with at least one item
   
# Run the Streamlit app by navigating to the directory containing the script
# and run: streamlit run app.py
