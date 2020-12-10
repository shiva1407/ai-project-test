from flask import Flask, render_template, jsonify, redirect, request
#import cv2
#import matplotlib.pyplot as plt
#from deepface import DeepFace

#import joblib

app = Flask(__name__)

@app.route("/test")
def root():
    return render_template("index.html") 

'''@app.route("/scrape", methods=['GET']) 
def scrape():
    listings = mongo.db.listings
    listings_data = scrape_craigslist.scrape()
    listings.update(
        {},
        listings_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302) '''

@app.route('/get-user-data')
def predict_emotion():
    return 'hello'




   ''' cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    i=0
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite('kang'+str(i)+'.jpg',frame)
    plt.imshow(img1)
    cap.release()

    predictions = DeepFace.analyze(img1, actions = ['emotion'])

    predicted_emotion = predictions['dominant_emotion'] '''

@app.route('/')
def helloworld():
   return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug = True)
