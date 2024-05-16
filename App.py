import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return img

def main():
    st.title("WebRTC Video Streaming Example")
    
    # Start the video stream
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()
