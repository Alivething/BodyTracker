import mediapipe as mp
import cv2 

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# cap = cv2.VideoCapture(0)

# Initiate pose model
with mp_pose.Pose(min_detection_confidence=0.1, min_tracking_confidence=0.5) as pose:
    
    # while cap.isOpened():
    #     ret, frame = cap.read()
    for i in range(0, 5):

        frame = cv2.imread("C:/Users/kaust/Desktop/College stuff/Book/pic"+str(i)+".jpg")
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Make Detections
        results = pose.process(image)
        bg = cv2.imread("C:/Users/kaust/Desktop/College stuff/Book/Black.jpg")
        
        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        image = cv2.flip(image, 1)
        # bg = cv2.flip(bg, 1)

        print(i)

        #Extracting the coordinates
        try:
            lhand = results.pose_landmarks.landmark[15]
            rhand= results.pose_landmarks.landmark[16]
            lshoulder = results.pose_landmarks.landmark[11]
            rshoulder = results.pose_landmarks.landmark[12]

        except:
            print("No landmarks detected")

        
        #Checking if left or right
        if((lhand.x> lshoulder.x)&(rhand.x> rshoulder.x)):
            print("Left")
            
        elif((lhand.x< lshoulder.x)&(rhand.x< rshoulder.x)):
            print("Right")
            
        elif((lhand.y< lshoulder.y)&(rhand.y< rshoulder.y)):
            print("Up")

        if((lhand.y> lshoulder.y)&(rhand.y< rshoulder.y)&(lhand.x< rhand.x)):
            print("Cross")

        # Draw connection
        cv2.imshow('Raw Webcam Feed', image)
        cv2.waitKey(1000)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# cap.release()
cv2.destroyAllWindows()