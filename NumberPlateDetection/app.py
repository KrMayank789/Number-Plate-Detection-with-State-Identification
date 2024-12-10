from main import *

import streamlit as st


def main():
    st.title("Number Plate Detection with State Identification")
    st.write("Upload a video to detect and extract number plates.")

    # File uploader for video input
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        st.success("Video uploaded successfully!")

        if st.button("Process Video"):
            st.write("Processing video, please wait...")

            # Initialize video capture
            cap = cv2.VideoCapture(temp_file_path)
            state_detected = None
            output_frame = None

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Detect plates
                plates = detect_plates(frame)

                for (x, y, w, h) in plates:
                    # Crop the plate
                    plate_img = frame[y:y + h, x:x + w]

                    # Extract text
                    plate_text = extract_text_from_plate(plate_img)

                    # Map to state
                    state_name = map_state_from_text(plate_text)

                    if state_name != "Unknown":
                        # Store the first detected frame and state
                        state_detected = state_name

                        # Annotate frame with the state
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(
                            frame,
                            f"State: {state_detected}",
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2,
                        )
                        output_frame = frame
                        break

                if state_detected:
                    break

            cap.release()

            if state_detected and output_frame is not None:
                st.success(f"Detected State: {state_detected}")

                # Display the output frame
                st.image(cv2.cvtColor(output_frame, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)
            else:
                st.error("No recognizable state detected in the video.")

            # Clean up temporary file
            os.remove(temp_file_path)


if __name__ == "__main__":
    main()
