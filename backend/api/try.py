import requests
import os

# url = "https://93e0-2001-ee0-4b4a-ca30-f97f-7b1e-1071-f8cc.ngrok-free.app/predict"

            
# payload = {
# "construction_cdl" : [
#     "Shape(KA,AH,HK)",
#     "Shape(KH,HC,CK)",
#     "Shape(KC,CF,FK)",
#     "Shape(KF,FG,GK)",
#     "Shape(GF,FE,EG)",
#     "Collinear(AHCF)",
#     "Collinear(EGK)"
#   ],
# "text_cdl" : [
#     "Equal(MeasureOfAngle(CFK),28)",
#     "Equal(MeasureOfAngle(GKF),35)",
#     "Equal(MeasureOfAngle(KAC),25)",
#     "Equal(MeasureOfAngle(KHC),51)",
#     "PerpendicularBetweenLine(EG,FG)",
#     "PerpendicularBetweenLine(HC,KC)",
#     "PerpendicularBetweenLine(KF,EF)"
#   ],
# "image_cdl": [
#     "Equal(MeasureOfAngle(CFK),28)",
#     "Equal(MeasureOfAngle(GKF),35)",
#     "Equal(MeasureOfAngle(KAC),25)",
#     "Equal(MeasureOfAngle(KHC),51)",
#     "PerpendicularBetweenLine(EG,FG)",
#     "PerpendicularBetweenLine(HC,KC)",
#     "PerpendicularBetweenLine(KF,EF)"
#   ],
# "goal_cdl":"Value(MeasureOfAngle(FEK))",
# "problem_answer": "55"
# }

# response = requests.post(url,json=payload)

# if response.status_code == 200:
#     content_type = response.headers.get('Content-Type', '')
#     print(f"ketqua",content_type)
#     # Kiểm tra nếu phản hồi là dạng multipart
#     if 'multipart' in content_type:
#         # Tách phản hồi thành các phần dựa trên boundary
#         boundary = content_type.split('boundary=')[-1]
#         parts = response.content.split(f"--{boundary}".encode())

#         # Xử lý từng phần
#         for part in parts:
#             if b'Content-Type: application/json' in part:
#                 # Phần JSON
#                 json_part = part.split(b'\r\n\r\n')[1].strip()
#                 json_data = json_part.decode('utf-8')
#                 print("JSON:", json_data)
#             elif b'Content-Type: image/png' in part:
#                 # Phần hình ảnh
#                 image_part = part.split(b'\r\n\r\n')[1].strip()
#                 with open('/home/duongvanchon/Documents/project/Geometry/backend/api/output/downloaded_2_hyper.png', 'wb') as f:
#                     f.write(image_part)
#                 print("Ảnh đã được tải về thành công!")
#     else:
#         print("Phản hồi không phải là dạng multipart:", response.text)
# else:
#     print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")
#     print(response.text)
    
    



            
# payload = {
# "construction_cdl" : [
#     "Shape(KA,AH,HK)",
#     "Shape(KH,HC,CK)",
#     "Shape(KC,CF,FK)",
#     "Shape(KF,FG,GK)",
#     "Shape(GF,FE,EG)",
#     "Collinear(AHCF)",
#     "Collinear(EGK)"
#   ],
# "text_cdl" : [
#     "Equal(MeasureOfAngle(CFK),28)",
#     "Equal(MeasureOfAngle(GKF),35)",
#     "Equal(MeasureOfAngle(KAC),25)",
#     "Equal(MeasureOfAngle(KHC),51)",
#     "PerpendicularBetweenLine(EG,FG)",
#     "PerpendicularBetweenLine(HC,KC)",
#     "PerpendicularBetweenLine(KF,EF)"
#   ],
# "image_cdl": [
#     "Equal(MeasureOfAngle(CFK),28)",
#     "Equal(MeasureOfAngle(GKF),35)",
#     "Equal(MeasureOfAngle(KAC),25)",
#     "Equal(MeasureOfAngle(KHC),51)",
#     "PerpendicularBetweenLine(EG,FG)",
#     "PerpendicularBetweenLine(HC,KC)",
#     "PerpendicularBetweenLine(KF,EF)"
#   ],
# "goal_cdl":"Value(MeasureOfAngle(FEK))",
# "problem_answer": "55"
# }

# response = requests.post(url,json=payload)


# # Kiểm tra mã trạng thái của phản hồi
# if response.status_code == 200:
#     # Split the response content into parts
#     boundary = response.headers['Content-Type'].split('boundary=')[-1]
#     parts = response.content.split(f"--{boundary}".encode())

#     for part in parts:
#         if b'Content-Type: application/json' in part:
#             # This is the JSON part
#             json_part = part.split(b'\r\n\r\n')[1].strip()
#             print("JSON:", json_part.decode('utf-8'))
#         elif b'Content-Type: image/png' in part:
#             # This is the image part
#             image_part = part.split(b'\r\n\r\n')[1].strip()
#             with open('/home/duongvanchon/Documents/project/Geometry/backend/api/output/downloaded_1_hyper.png', 'wb') as f:
#                 f.write(image_part)
#             print("Ảnh đã được tải về thành công!")

# else:
#     print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")  
   
import json
 
# try:
        
#     text_description = "Find(x)"

#     image_path ='/home/duongvanchon/Documents/project/Geometry/backend/api/output/itc.png'
    
#     url = "https://66c8-2401-d800-27c6-4f6d-95ad-e7e8-45c8-5457.ngrok-free.app/parse_file" 
#     payload = {
#         "compact_text" : text_description
#     }
#     file_path = './input/data.json'

#     # Mở tệp ở chế độ ghi ('w') và ghi dữ liệu JSON vào tệp
#     with open(file_path, 'w') as json_file:
#         json.dump(payload, json_file, indent=2) 
        
#     files = {
#         'json_file' : open(file_path,'rb'),
#         'image_file': open(image_path, 'rb')}


#     response = requests.post(url ,files=files)
#     # print(response)

#     if response.status_code == 200 : 
#         file_path = './input/diagram.json'            
#         diagram= response.json()
        
#         with open(file_path, 'w') as json_file2:
#             json.dump(diagram, json_file2, indent=2) 
        
#         print(response.json())
#     else : 
#         print(f"Error: {response.status_code}")
#         print(response.text)
        
#         print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")  
# except Exception as e:
#     print("error request", e)


try:
        
    text_description = "Find x"

    image_path ='/home/duongvanchon/Documents/project/Geometry/backend/api/output/test1.png'
    
    url = "https://cf9d-2401-d800-27c6-4f6d-95ad-e7e8-45c8-5457.ngrok-free.app/main_solve" 
    payload = {
        "compact_text" : text_description
    }
    file_path = './input/data.json'

    # Mở tệp ở chế độ ghi ('w') và ghi dữ liệu JSON vào tệp
    with open(file_path, 'w') as json_file:
        json.dump(payload, json_file, indent=2) 
        
    files = {
        'json_file' : open(file_path,'rb'),
        'image_file': open(image_path, 'rb')}


    response = requests.post(url ,files=files)
    # print(response)

    if response.status_code == 200 : 
        file_path = './input/diagram.json'            
        diagram= response.json()
        
        with open(file_path, 'w') as json_file2:
            json.dump(diagram, json_file2, indent=2) 
        
        print(response.json())
    else : 
        print(f"Error: {response.status_code}")
        print(response.text)
        
        print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")  
except Exception as e:
    print("error request", e)