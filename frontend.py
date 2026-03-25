import streamlit as st
import requests

st.title("Simple Frontend + Backend App")
st.write("Enter a message below")

message = st.text_input("Your message")

if st.button("Send"):
    if message.strip():
        try:
            response = requests.post(
                "http://localhost:5001/api/message",
                json={"message": message},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                st.success("Reponse received from backend")
                st.write("**Original Message**", data["original_message"])
                st.write("**Backend Reply:**", data["reply"])
            else:
                st.error(f"Backend returned status code {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to backend")
        except Exception as e:
            st.error(f"Error {e}")
            
    else:
        st.warning("Please enter a message first")