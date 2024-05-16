import streamlit as st
from streamlit_webrtc import webrtc_streamer

def main():
    st.title("Simple WebRTC Camera Stream")
    st.write("This example shows the video stream from your camera.")

    webrtc_streamer(key="example", video_transformer_factory=None, media_stream_constraints={"video": True, "audio": False})

if __name__ == "__main__":
    main()
