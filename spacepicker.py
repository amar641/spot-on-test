import cv2
import pickle

width, height = 75, 48

# Try to load previously saved parking positions
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                break

    # Save updated list to file
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


# Load the video
cap = cv2.VideoCapture(r'C:\Users\Asus\OneDrive\Desktop\Udemy cousres\data science, ML\data analysis\pnadas\video.mp4')

if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

while True:
    ret, img = cap.read()

    if not ret:
        print("Video Ended or Error Reading Frame")
        break

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
