import cv2 
if __name__ == "__main__":
    ## 读取rtsp视频流并显示
    # cap = cv2.VideoCapture("rtsp://192.168.137.215:8554")
    ## 读取usb-came 0（/dev/video0） 
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    writer = cv2.VideoWriter("video.avi", fourcc, 10, size)
    while cap.isOpened():
        (ret,frame)=cap.read()
        print (frame.shape[0], frame.shape[1], frame.shape[2])
        cv2.putText(frame, "Press q to quit", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
        cv2.imshow("frame",frame)
        writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow("frame")
    cap.release()
