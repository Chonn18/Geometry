from rest_framework.views import APIView
from rest_framework.response import Response
from .model import Problem
from .serializers import ProblemSerializer
from .run_alpha import run
import pyrebase
from rest_framework import status
import uuid
import requests
import base64
import os
import json


url = "https://93e0-2001-ee0-4b4a-ca30-f97f-7b1e-1071-f8cc.ngrok-free.app/predict"

firebaseConfig = {
  'apiKey': "AIzaSyCPhj5bXvZsPTipxQ9TOog_d-1TBuv7W0M",
  'authDomain': "bcn-geometry.firebaseapp.com",
  'databaseURL': "https://bcn-geometry-default-rtdb.firebaseio.com",
  'projectId': "bcn-geometry",
  'storageBucket': "bcn-geometry.appspot.com",
  'messagingSenderId': "1062126520617",
  'appId': "1:1062126520617:web:92db7aef26e253b38b8f38",
  'measurementId': "G-N4QEY0VMYG"
}


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()

# problems = db.child("problems").get()

# class ProblemListView2(APIView):
#     def get(self, request):
#         try:
#             category_to_filter = "imo"
#             problems_ref = db.child("problems").order_by_child("category").equal_to(category_to_filter).get()
#             if problems_ref.each() is None:
#                 return Response({"detail": "No problems found"}, status=status.HTTP_404_NOT_FOUND)
#             problems = [ProblemSerializer(problem.val()).data for problem in problems_ref.each()]
#             return Response(problems, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## chua xong
class ProblemListView(APIView):
    def get(self, request):
        # Lấy các Problem có category là "imo" từ Firebase
        try:
            category_to_filter = "imo"
            problems_ref = db.child("problems").order_by_child("category").equal_to(category_to_filter).get()
            # problems_ref = db.child("problems").get()
            if problems_ref.each() is None:
                return Response({"detail": "No problems found"}, status=status.HTTP_404_NOT_FOUND)
            # problems = [problem.val() for problem in problems_ref.each()]
            problems = [ProblemSerializer(problem.val()).data for problem in problems_ref.each()]
            # print(problems[0])
            return Response(problems, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        data = request.data
        # Tạo một mẫu mới vào Firebase
        # problem_ref = db.collection('problems').document()
        problem_ref = {
            'title': data.get('title'),
            'description': data.get('description'),
            'solve': data.get('solve'),
            'image':data.get('image'),
            'image_result': data.get('image_result'),
            'category': data.get('category')
        }
        db.child("problems").child(str(uuid.uuid4())).set(problem_ref)
        return Response({'message': 'Problem created successfully'}, status=201)

class SolveProblemNoImgView(APIView):
    def post(self, request):
        try:
            data = request.data
            problem_description = data.get("description")
            print(data)
            run(problem=problem_description)
            with open('/home/duongvanchon/Documents/project/Geometry/backend/api/output/result.txt', 'r') as f:
                solve = f.read().strip()
            solve_lines = solve.split('\n')
            solve = '\n'.join(solve_lines)
            
            img = '/home/duongvanchon/Documents/project/Geometry/backend/api/output/output_image.png'
            random_filename = str(uuid.uuid4()) + ".png"
            storage.child(random_filename).put(img)
            # storage.child(img).put(img)
            image_result = storage.child(random_filename).get_url(None)
            
            problem = {
                'title': data.get('title'),
                'description': problem_description,
                'solve': solve,
                'image': "",
                'image_result': image_result,
                'category': "new_solve"
            }
            db.child("problems").child(str(uuid.uuid4())).set(problem)
            
            # problems = [ProblemSerializer(problem).data ]
            return Response(problem, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class SolveWithPSPG(APIView):
    def post (self,request):
        try:
            data = request.data
            print(data)
            text_description1 = data.get("description")
            cons_description1 = data.get("text_cons")
            image_description1 = data.get("text_image")
            # Tách chuỗi thành các dòng, loại bỏ khoảng trắng dư thừa xung quanh mỗi dòng
            text_description = linestrip(text_description1) 
            cons_description = linestrip(cons_description1)  
            image_description = linestrip(image_description1)  
        
            goal_description = data.get("text_goal")
            goal_description = multitoline(goal_description)
            
            title = data.get("title")
            # problem_answer = data.get("problem_answer")
            problem_answer = "0"
            
            # response = requests.get(url)
            
            payload = {
            "construction_cdl" : cons_description,
            "text_cdl" : text_description,
            "image_cdl": image_description,
            "goal_cdl":goal_description,
            "problem_answer": problem_answer
            }
            
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '')
                
                # Kiểm tra nếu phản hồi là dạng multipart
                if 'multipart' in content_type:
                    # Tách phản hồi thành các phần dựa trên boundary
                    boundary = content_type.split('boundary=')[-1]
                    parts = response.content.split(f"--{boundary}".encode())

                    # Xử lý từng phần
                    for part in parts:
                        if b'Content-Type: application/json' in part:
                            # Phần JSON
                            json_part = part.split(b'\r\n\r\n')[1].strip()
                            json_data = json_part.decode('utf-8')
                            print("JSON:", json_data)
                        elif b'Content-Type: image/png' in part:
                            img = '/home/duongvanchon/Documents/project/Geometry/backend/api/output/downloaded_2_hyper.png'
                            # Phần hình ảnh
                            image_part = part.split(b'\r\n\r\n')[1].strip()
                            with open(img, 'wb') as f:
                                f.write(image_part)
                            print("Ảnh đã được tải về thành công!")
                            
                            random_filename = str(uuid.uuid4()) + ".png"
                            storage.child(random_filename).put(img)
                            # storage.child(img).put(img)
                            image_result = storage.child(random_filename).get_url(None)
                    
                    problem = {
                        "title" : title,
                        "construction_cdl" : cons_description1,
                        "text_cdl" : text_description1,
                        "image_cdl": image_description1,
                        "goal_cdl":goal_description,
                        "problem_answer": problem_answer,
                        'image_result': image_result,
                        'category': "pgps_new"
                    }
                    db.child("problems_pgps").child(str(uuid.uuid4())).set(problem)
                    return Response({'image_result': image_result}, status=201)        
                            
                else:
                    print("Phản hồi không phải là dạng multipart:", response.text)
                    return Response({'text': 'Sory i can not solve this problem'}, status=201)
            else:
                print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")
                print(response.text)
                return Response({'text': 'Sory i can not solve this problem'}, status = response.status_code)
                
                
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
class Viewdata(APIView):
    def post (self,request):
        try:
            data = request.data
            text_description1 = data.get("description")
            cons_description1 = data.get("text_cons")
            image_description1 = data.get("text_image")
            # Tách chuỗi thành các dòng, loại bỏ khoảng trắng dư thừa xung quanh mỗi dòng
            text_description = linestrip(text_description1) 
            cons_description = linestrip(cons_description1)  
            image_description = linestrip(image_description1)  
        
            goal_description = data.get("text_goal")
            goal_description = multitoline(goal_description)
            title = data.get("title")
            problem_answer = data.get("problem_answer")
            
            print(text_description)
            print(cons_description)
            print(goal_description)
                
            return Response({'message': 'i got it'}, status=201)    
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
def multitoline (text):
    lines = text.splitlines()

    # Loại bỏ khoảng trắng dư thừa xung quanh mỗi dòng (nếu cần)
    lines = [line.strip() for line in lines]

    # Nối các dòng lại với nhau bằng dấu phẩy và khoảng trắng
    result = ', '.join(lines)
    
    return result

def linestrip (text):
    return [line.strip() for line in text.splitlines()]


class CheckData(APIView):
    def post (self,request):
        try:
            data = request.data
            text_description = data.get("description")
            title = data.get("title")
            image_data = data.get("image")
            payload = {
                "compact_text" : text_description
            }
            print(text_description)
            # if not text_description or not image_data: 
            #     return Response({"error": "input or image is required"}) 
            # else: print(text_description)

            image_content = base64.b64decode(image_data)

            image_path = os.path.join('/home/duongvanchon/Documents/project/Geometry/backend/api/input', 'testn.jpg')
            with open(image_path, 'wb') as f:
                f.write(image_content)
                
            file_path = '/home/duongvanchon/Documents/project/Geometry/backend/api/input/data.json'

            # Mở tệp ở chế độ ghi ('w') và ghi dữ liệu JSON vào tệp
            with open(file_path, 'w') as json_file:
                json.dump(payload, json_file, indent=2) 
            
            # url = "https://b61f-2401-d800-27c6-4f6d-a858-6574-570a-e72.ngrok-free.app/parse_file" 
            # files = {
            #     'json_file' : open(file_path,'rb'),
            #     'image_file': open(image_path, 'rb')}


            # response = requests.post(url ,files=files)
            # print(response)

            # if response.status_code == 200 : 
            #     file_path = './input/diagram.json'            
            #     diagram= response.json()
                
            #     with open(file_path, 'w') as json_file2:
            #         json.dump(diagram, json_file2, indent=2) 
                
            #     print(response.json())
            # else : 
            #     print(f"Error: {response.status_code}")
            #     print(response.text)
                
            #     print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")    
            
            return Response({'message': 'i got it'}, status=201)
        except Exception as e:
            print("error",e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SolveInter(APIView):
    def post (self,request):
        try:
            data = request.data
            text_description = data.get("description")
            title = data.get("title")
            image_data = data.get("image")
            payload = {
                "compact_text" : text_description
            }
            print(text_description)
            image_content = base64.b64decode(image_data)

            image_path = os.path.join('/home/duongvanchon/Documents/project/Geometry/backend/api/input', 'testn.jpg')
            with open(image_path, 'wb') as f:
                f.write(image_content)
                
            file_path = '/home/duongvanchon/Documents/project/Geometry/backend/api/input/data.json'

            # Mở tệp ở chế độ ghi ('w') và ghi dữ liệu JSON vào tệp
            with open(file_path, 'w') as json_file:
                json.dump(payload, json_file, indent=2) 
            
            url = "https://6d99-2401-d800-27c6-4f6d-95ad-e7e8-45c8-5457.ngrok-free.app/main_solve" 
            files = {
                'json_file' : open(file_path,'rb'),
                'image_file': open(image_path, 'rb')}


            response = requests.post(url ,files=files)
            print(response)

            if response.status_code == 200 : 
                file_path = '/home/duongvanchon/Documents/project/Geometry/backend/api/output/result_inter.json'            
                diagram= response.json()
                
                with open(file_path, 'w') as json_file2:
                    json.dump(diagram, json_file2, indent=2) 
                
                print(response.json())
                result = response.json()
                guess = result['result'][0]['guess']
                return Response({'message': 'i got it', 'result':guess}, status=201)
            else : 
                print(f"Error: {response.status_code}")
                print(response.text)
                
                print(f"Yêu cầu không thành công với mã trạng thái {response.status_code}")  
                return Response({"error": "Can not solve"})   
            
            
        except Exception as e:
            print("error",e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       

