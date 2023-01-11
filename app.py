from re import DEBUG, sub
from unicodedata import mirrored
from flask import Flask, render_template, request, redirect, send_file, url_for,Response
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
import cv2


app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'uploads')
fileObject = open("pathh.txt", "r")
pathh = fileObject.read()
print(pathh)
os.makedirs(uploads_dir, exist_ok=True)
#def play_videoFile(filePath,mirror=False):


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return
    video = request.files['video']
    print(os.path.join(uploads_dir, secure_filename(video.filename)))
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    #subprocess.run("ls")
    subprocess.run(['python', 'detect.py', '--weights', 'runs/train/yolo_road_det7/weights/best.pt', '--conf', '0.1', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])


    obj = secure_filename(video.filename)
    return obj

@app.route("/opencam", methods=['GET'])
def opencam():
    print("Starting...")
    subprocess.run(['python', 'detect.py', '--weights', 'runs/train/yolo_road_det7/weights/best.pt', '--conf', '0.1', '--source', '0'])
    return "done"
    

@app.route('/return-files', methods=['GET'])
def return_file():
    return render_template("download.html",pth=pathh)
#    cap = cv2.VideoCapture(data)
#    cv2.namedWindow('Video Life2Coding',cv2.WINDOW_AUTOSIZE)
#    while True:
#        ret_val, frame = cap.read()
#        if mirrored:
#            frame = cv2.flip(frame, 12)
#            cv2.imshow('Video Life2Coding', frame)
#        if cv2.waitKey(100000) == 27000:
#            break  # esc to qu
#    obj = request.args.get('obj')
#    loc = os.path.join("runs/detect", obj)
#    print(loc)
#    try:
#        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
#        # return send_from_directory(loc, obj)
#    except Exception as e:
#        return str(e)
#
@app.route('/display')
def display_video(filename):
  with open('pathh.txt', 'r') as file:
    file_path = file.read()
  return send_file(file_path, mimetype='video/mp4')