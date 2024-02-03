import requests
import random

def send_verification_sms(phone_number):
  """
  Mengirim spam verifikasi ke nomor SMS.

  Args:
    phone_number: Nomor telepon (tanpa awalan +62).

  Returns:
    Response dari server SMS.
  """

  url = "https://api.smsgateway.com/v1/messages"
  headers = {
    "Content-Type": "application/json",
  }
  data = {
    "phone_number": phone_number,
    "message": "Kode verifikasi Anda adalah: XXXX",
  }

  # Generate random verification code
  verification_code = str(random.randint(100000, 999999))

  # Replace the "XXXX" placeholder in the message with the verification code
  data["message"] = data["message"].replace("XXXX", verification_code)

  response = requests.post(url, headers=headers, json=data)

  return response

# Masukkan nomor telepon di sini
phone_number = "81234567890"

# Kirim spam verifikasi
response = send_verification_sms(phone_number)

# Periksa status response
if response.status_code == 200:
  print("Spam verifikasi berhasil terkirim.")
else:
  print("Terjadi kesalahan:", response.status_code, response.text)
