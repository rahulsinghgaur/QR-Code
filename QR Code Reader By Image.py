import cv2,os,re
regex = re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")

img = cv2.imread("linkQRCode.png")
detector = cv2.QRCodeDetector()

ans = detector.detectAndDecode(img)[0]

if re.fullmatch(regex, ans):
    os.system(f"start \"\" {ans}")
else:
    print(ans)