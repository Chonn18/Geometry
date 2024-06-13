from google.cloud import storage
from google.auth import compute_engine
from django.conf import settings
import google.oauth2.service_account as service_account

import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from datetime import datetime

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/home/duongvanchon/Downloads/bcn-geometry-firebase-adminsdk-op373-6bcf2912fe.json")
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore service
database = firestore.client()

url = "https://28eb-2001-ee0-4b4a-ca30-f4e0-2c91-ac49-313c.ngrok-free.app/predict"

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


def check_and_retrieve_samples():
    date_choose = db.child("date_choose").get().val()
    
    # Query để lấy các mẫu có ngày cập nhật sau date_choose
    samples = []
    results = db.child("problem_inter").order_by_child("date").start_at(date_choose).get()
    
    for result in results.each():
        samples.append(result.val())
        # if len(samples) >= 1000:
        #     break
    
    if len(samples) >= 1000:
        print(f"Checking data ok, let training data")
        date_now = datetime.now
        db.child("date_choose").set(date_now)
        process_samples(samples)

def process_samples(samples):
    # Hàm xử lý các mẫu lấy được từ Firebase
    print(f"Processing {len(samples)} samples")
    # Thêm logic xử lý tại đây

def generate_signed_url(bucket_name, object_name, expiration_time=3600):
    """
    Generate a pre-signed URL for uploading a file to Google Cloud Storage using API key JSON.

    :param bucket_name: Name of the GCS bucket.
    :param object_name: Name of the object (file) within the bucket.
    :param expiration_time: Expiration time for the URL in seconds (default is 1 hour).
    :return: Pre-signed URL.
    """
    credentials_path = settings.CREDENTIAL_PATH  
    # Load credentials from API key JSON
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    # Create a storage client
    client = storage.Client(credentials=credentials)
    # Get the bucket
    bucket = client.bucket(bucket_name)

    # Create a blob (object) in the bucket
    blob = bucket.blob(object_name)

    # Generate a signed URL for the object
    url = blob.generate_signed_url(
        version='v4',
        expiration=expiration_time,
        method='PUT',
    )

    return url