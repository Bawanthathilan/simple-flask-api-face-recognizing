from flask import Flask ,render_template, Response ,request, jsonify
from camera import camera_stream
import cv2


app=Flask(__name__)

camera = cv2.VideoCapture(0)
def gen_frames():  
     while True:
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return ("Hello world")





if __name__ == '__main__':
    app.run(debug=True)