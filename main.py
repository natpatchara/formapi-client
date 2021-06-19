import streamlit as st
import base64
import requests
import cv2
import numpy as np

def send_base64(src,oper_type,params={}):
  url = 'https://box-detection-api.herokuapp.com/label'
  encoded_string = base64.b64encode(src).decode('utf-8')
  test = {'image':[{"base64":encoded_string}],'op_type':oper_type,'params':params}
  return requests.post(url, json=test)

def process_response(img,res):
  res = res.json()
  img = img.copy()
  if(res['status'] == 'success'):
    coords = res['result'][0]['coords']
    for coord in coords:
      x = int(coord['x'])
      y = int(coord['y'])
      w = int(coord['w'])
      h = int(coord['h'])
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    return res['status'], img

  return res['status'], None

st.title('Form api client')

operator = st.radio(label = "Choose operator type:", options = ("Radio","Checkbox"))

with st.form(key='Upload image'):
  st.text("Please select parameter:")
  if (operator == "Radio"):
    min_radius = st.number_input("Min radius:", value = 20)
    max_radius = st.number_input("Max radius:", value = 50)
    params = {"minRadius":min_radius, "maxRadius":max_radius}

  elif (operator == "Checkbox"):
    min_size = st.number_input("Min size:", value = 25)
    max_size = st.number_input("Max size:", value = -1)
    params = {"minBoxSize":min_size, "maxBoxSize":max_size}

  uploaded_file = st.file_uploader("Choose a image:", type=['png','jpeg'])
  submitted = st.form_submit_button('Submit')



if (submitted):
  if uploaded_file is not None:

    src = uploaded_file.read()
    res = send_base64(src,'Radio',params)

    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(src), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # convert server response into JSON format.
    status, processed_image = process_response(image,res)  

    st.image(image, "original image")
    st.image(processed_image, "processed image")