import cv2
#Initilize barcode detector & videocapture
bd=cv2.barcode.BarcodeDetector()
cap=cv2.VideoCapture(0)

detections={}

while True:
    #ret->true if video is detected
    ret, frame= cap.read()
    if ret:
        #ret_bc: detected barcode
        #code: number of the barcode
        #barcode_type: barcode type nothing else to say
        #coords: screen cords
        ret_bc, code,barcode_type, coords = bd.detectAndDecodeWithType(frame)
        if ret_bc:
            
            frame = cv2.polylines(frame, coords.astype(int), True, (255,0,0),3)
            for Code, coord in zip(code,coords):
                if Code in detections:
                    detections[Code]+=1
                    #If the detection appears 30 times, means its not a false positive
                    if detections[Code]>=30:
                        print('Succesful detection: ', Code)                        
                        cv2.waitKey(250)
                        detections.clear()
                        print(coords)
                else:
                    detections[Code]=1
                frame=cv2.putText(frame, Code, coord[1].astype(int),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2, cv2.LINE_AA)
        cv2.imshow('Barcode Scanner', frame)
    #'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
