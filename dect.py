fileObject = open("pathh.txt", "r")
data = fileObject.read()
print(data)

import cv2

def play_videoFile(filePath,mirror=False):

    cap = cv2.VideoCapture(filePath)
    cv2.namedWindow('Video Life2Coding',cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()

        if mirror:
            frame = cv2.flip(frame, 12)

        cv2.imshow('Video Life2Coding', frame)

        if cv2.waitKey(100000) == 27000:
            break  # esc to quit

def main():
    play_videoFile(data,mirror=False)

if __name__ == '__main__':
    main()