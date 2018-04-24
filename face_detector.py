import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('photo.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                      minNeighbors=5)

for x, y, width, height in faces:
    img = cv2.rectangle(img, (x, y), (x + width, y + height), (255, 255, 0), 3)
resized_final_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

cv2.imshow('Image_final', resized_final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
