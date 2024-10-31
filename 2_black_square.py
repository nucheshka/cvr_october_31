import cv2
cap = cv2.VideoCapture(0)
# list_example = [0, 1, 2, 3]
# print(list_example[1:3])
square_legth = 100
while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, wigth, _ = frame.shape
    frame[:square_legth, :square_legth] = [0, 0, 0]
    frame[:square_legth, wigth - square_legth:] = [0, 0, 0]
    frame[height - square_legth:, wigth - square_legth:] = [0, 0, 0]
    frame[height - square_legth:, :square_legth] = [0, 0, 0]
    frame[height // 2 - square_legth // 2: height // 2 + square_legth // 2, wigth // 2 -  square_legth // 2: wigth //2 + square_legth // 2] = [0, 0, 0]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    print(key)
    if key == ord(' '):
        break
    # break
cv2.destroyAllWindows()
cap.release()