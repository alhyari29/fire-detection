# 🔥 Fire & Smoke Detection Project

This project uses a YOLOv11 model to detect **fire** and **smoke** in videos.

---

## 🛠️ Technologies Used
- Python
- OpenCV
- PyTorch
- Ultralytics YOLOv11
- Google Colab (for training)

---

## 📄 Project Description
I trained a custom object detection model on a **fire and smoke** dataset using Roboflow and YOLOv11.  
The model is able to detect fire and smoke and highlight them with bounding boxes in real-time on videos.

- ✅ Trained on a high-quality dataset from Roboflow.
- ✅ Tested on different fire and smoke videos.
- ✅ Good real-time performance and accuracy.

---

## 🚀 How to Run the App

### 1. Clone the Repository:
```bash
git clone https://github.com/alhyari29/fire-detection.git
cd fire-detection

Clone the repository:

bash
Copy
Edit
git clone https://github.com/alhyari29/fire-detection.git
cd fire-detection
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the model on a test video:

bash
Copy
Edit
python test_model.py
Note:

Make sure you have a video file (e.g., test 2.mp4) ready.

You can adjust the confidence threshold inside test_model.py.

## 🎯 Model Performance

| Metric         | Fire  | Smoke | Overall |
|:--------------:|:-----:|:-----:|:-------:|
| **Precision**  | 0.925 | 0.879 | 0.902   |
| **Recall**     | 0.940 | 0.799 | 0.870   |
| **mAP@0.5**    | 0.939 | 0.814 | 0.877   |
| **mAP@0.5:0.95** | 0.793 | 0.663 | 0.728   |

📚 Acknowledgments
Dataset from Roboflow.

Model training based on Ultralytics YOLOv11.

💬 Feel free to fork, star, or contribute to improve the project!
✅ You can now paste this into GitHub → README.md → and Commit ✅
