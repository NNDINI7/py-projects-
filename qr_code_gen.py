import qrcode
#take input
upi_id = input("Enter your UPI ID = ")
#format(upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE)
#define the url based on upi id and payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
gpay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr for each app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
gpay_qr = qrcode.make(gpay_url)

#save an img
# phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# gpay_qr.save('gpay_qr.png')

#show qr codes
phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()

