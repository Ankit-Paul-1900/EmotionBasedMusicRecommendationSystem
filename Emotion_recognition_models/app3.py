import cv2
import pandas as pd
import numpy as np
from keras.models import model_from_json
import streamlit as st
from streamlit_webrtc import webrtc_streamer,WebRtcMode
import av #to convert image to ndarray and vice-versa
emotion = {0: "Angry", 1: "Happy", 2: "Neutral", 3: "Sad"}
# load json and create model

json_file = open('emotionModel.json', 'r')

loaded_model_json = json_file.read()

json_file.close()
emotion_model = model_from_json(loaded_model_json)
try:
    emotion1=np.load("emotion.npy")
except:
    emotion1=""    
class EmotionCapture:
    def recv(self,frame):
        fm=frame.to_ndarray(format='bgr24')
        fm = cv2.resize(fm, (1280, 720))
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(fm, cv2.COLOR_BGR2GRAY)
        # detect faces available on camera

        num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=3)

        # take each face available on the camera and Preprocess it
        for (x, y, w, h) in num_faces:
            cv2.rectangle(fm, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)

            roi_gray_frame = gray_frame[y:y + h, x:x + w]

            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            # predict the emotions

            emotion_prediction = emotion_model.predict(cropped_img)

            maxindex = int(np.argmax(emotion_prediction))
            t=emotion[maxindex]
            print(t)
            cv2.putText(fm, t, (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            np.save("emotion.npy",np.array([t]))

        return av.VideoFrame.from_ndarray(fm,format='bgr24')
st.title('Emotion Based Music Recommendation')
#btn1=st.button("Start Camera")
webrtc_streamer(key="key",desired_playing_state=True,video_processor_factory=EmotionCapture)

btn=st.button("Recommend me songs")
sad_df=pd.read_csv("sad_songs.csv")
happy_df=pd.read_csv("happy_songs.csv")
angry_df=pd.read_csv("angry_songs.csv")
neutral_df=pd.read_csv("neutral_songs.csv")
link=""
if btn:
    if emotion:
        emot=emotion1[0]
        if emot == 'Sad':
            st.markdown("<h4 style='text-align: center; color: grey;'><b>Recommended Sad Songs </b></h4>", unsafe_allow_html=True)

            try:
                for a,n,i in zip(sad_df['artist_name'],sad_df['track_name'],range(10)):
                    n=n.replace(" ","")
                    a=a.replace(" ","")
                    link=f'https://www.youtube.com/results?search_query={ n }+{a}'
                    # Recommended song name
                    st.markdown("""<h4 style='text-align: center;'><a href={}>{} - {}</a></h4>""".format(link,i+1,n),unsafe_allow_html=True)

                     # Artist name
                    st.markdown("<h5 style='text-align: center; color: grey;'><i>{}</i></h5>".format(a), unsafe_allow_html=True)
                    st.write("---------------------------------------------------------------------------------------------------------------------")
            except:
                pass
        if emot == 'Happy':
            st.markdown("<h4 style='text-align: center; color: grey;'><b>Recommended Happy Songs </b></h4>", unsafe_allow_html=True)
            try:
                for a,n,i in zip(happy_df['artist_name'],happy_df['track_name'],range(10)):
                    n=n.replace(" ","")
                    a=a.replace(" ","")
                    link=f'https://www.youtube.com/results?search_query={ n }+{a}'
                    # Recommended song name
                    st.markdown("""<h4 style='text-align: center;'><a href={}>{} - {}</a></h4>""".format(link,i+1,n),unsafe_allow_html=True)

                     # Artist name
                    st.markdown("<h5 style='text-align: center; color: grey;'><i>{}</i></h5>".format(a), unsafe_allow_html=True)
                    st.write("---------------------------------------------------------------------------------------------------------------------")
            except:
                pass
        if emot == 'Angry':
            st.markdown("<h4 style='text-align: center; color: grey;'><b>Recommended Angry Songs </b></h4>", unsafe_allow_html=True)
            try:
                for a,n,i in zip(angry_df['artist_name'],angry_df['track_name'],range(10)):
                    n=n.replace(" ","")
                    a=a.replace(" ","")
                    link=f'https://www.youtube.com/results?search_query={ n }+{a}'
                    # Recommended song name
                    st.markdown("""<h4 style='text-align: center;'><a href={}>{} - {}</a></h4>""".format(link,i+1,n),unsafe_allow_html=True)

                     # Artist name
                    st.markdown("<h5 style='text-align: center; color: grey;'><i>{}</i></h5>".format(a), unsafe_allow_html=True)
                    st.write("---------------------------------------------------------------------------------------------------------------------")
            except:
                pass
        if emot == 'Neutral':
            st.markdown("<h4 style='text-align: center; color: grey;'><b>Recommended Neutral Songs </b></h4>", unsafe_allow_html=True)
            try:
                for a,n,i in zip(neutral_df['artist_name'],neutral_df['track_name'],range(10)):
                    n=n.replace(" ","")
                    a=a.replace(" ","")
                    link=f'https://www.youtube.com/results?search_query={ n }+{a}'
                    # Recommended song name
                    st.markdown("""<h4 style='text-align: center;'><a href={}>{} - {}</a></h4>""".format(link,i+1,n),unsafe_allow_html=True)

                     # Artist name
                    st.markdown("<h5 style='text-align: center; color: grey;'><i>{}</i></h5>".format(a), unsafe_allow_html=True)
                    st.write("---------------------------------------------------------------------------------------------------------------------")
            except:
                pass
            st.markdown("<h5 style='text-align: center; color: grey;'><b>Recommended Neutral Songs </b></h5>", unsafe_allow_html=True)
            