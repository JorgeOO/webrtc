import asyncio
import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return img

def main():
    st.title("WebRTC Video Streaming Example")
    st.write("This is a simple example of WebRTC video streaming with Streamlit and face detection using OpenCV.")

    # Configurar el bucle de eventos
    asyncio.set_event_loop(asyncio.new_event_loop())

    webrtc_ctx = webrtc_streamer(
        key="example"
    )

    if webrtc_ctx.video_transformer:
        st.write("Streaming started. If you see an error, try refreshing the page.")

if __name__ == "__main__":
    main()
