import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings

# Load the Firebase credentials
cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

def create_problem(title, description, category):
    # Tạo một mẫu mới vào Firestore
    problem_ref = db.collection('problems').document()
    problem_ref.set({
        'title': title,
        'description': description,
        'category': category
    })

if __name__ == "__main__":
    # Điền các giá trị của một mẫu problem
    title = "Title of the problem"
    description = "Description of the problem"
    category = "imo"  # Chọn category tùy theo yêu cầu của bạn

    # Gọi hàm create_problem để tạo một mẫu mới và đẩy lên Firestore
    create_problem(title, description, category)

