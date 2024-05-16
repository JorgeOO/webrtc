import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

# Define the video transformer class
class VideoTransformer(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Convert back to 3-channel image
        gray_3_channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        return av.VideoFrame.from_ndarray(gray_3_channel, format="bgr24")

# Set up the Streamlit app
st.title("WebRTC with Streamlit - Grayscale Filter")

# Define the RTC configuration with STUN server
RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun1.l.google.com:19302"]}]})

# Initialize the webrtc streamer
webrtc_streamer(key="example", video_processor_factory=VideoTransformer, rtc_configuration=RTC_CONFIGURATION)
