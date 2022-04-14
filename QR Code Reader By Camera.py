import cv2,re,os
regex = re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")
vdo = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _,img = vdo.read()
    data = detector.detectAndDecode(img)[0]
    if data:
        if re.fullmatch(regex, data):
            os.system(f"start \"\" {data}")
            break
        else:
            print(data)
            break
