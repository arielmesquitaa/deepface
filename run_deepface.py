import os
import sys

# Set default models to avoid empty string crash
os.environ["DEEPFACE_FACE_RECOGNITION_MODELS"] = "VGG-Face"
os.environ["DEEPFACE_FACE_DETECTION_MODELS"] = "opencv"

# Add the src directory to sys.path
sys.path.append(os.path.join(os.getcwd(), "deepface", "api", "src"))

from app import create_app

if __name__ == "__main__":
    app = create_app()
    print("Starting DeepFace API on port 5005...")
    # use_reloader=False prevents the double startup in debug mode
    # debug=True still enables better error messages
    app.run(host="0.0.0.0", port=5005, debug=True, use_reloader=False)
