# 🅿️ Parking Spot Detection System

![Python version](https://img.shields.io/badge/python-3.x-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## 📝 Overview

The Parking Spot Detection System is an advanced solution that leverages machine learning and computer vision techniques to detect and report available parking spots in real-time. By analyzing video feeds from parking lots, the system accurately monitors and identifies the occupancy status of each parking space. This project aims to enhance parking management efficiency and improve the user experience in various settings, such as malls, airports, and urban centers.

## 🖼️ Demo

![Parking Spot Detection Demo](https://drive.google.com/uc?id=1q5bTfFYcCmGFU_uhAl1bZTV7v_DpohD3)

## 📦 Requirements

To run this project, you need the following libraries:

- OpenCV (Computer Vision)
- scikit-learn (Machine Learning)
- pandas (Data Handling)
- Pillow (Image Processing)
- Matplotlib (Plotting)
- scikit-image (Image Processing)

## ⚙️ Installation

1. Clone this repository:

   ```
   git clone https://github.com/AkshaySatasiya/Parking-Spot-Detection.git
   ```

2. Navigate to the project directory:

   ```
   cd parking-spot-detection
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## 🌐 Additional Resources

- [Dataset](https://drive.google.com/drive/folders/147SiZLL8GY4_Gvgyy4WNu80UnV3ZGtRY?usp=drive_link) - Download the dataset used in this project.

## 🚀 Usage

1. Execute the `main.py` script to start the parking spot detection:

   ```
   python main.py
   ```

2. The `util.py` file contains utility functions that handle image processing and machine learning model predictions.

## 🤖 How it Works

1. `main.py` processes the video feed to detect changes in the parking spots using connected component analysis.
2. The processed image data is then passed through a pre-trained machine learning model to determine the vacancy of each parking spot.
3. The model, loaded in `util.py`, predicts if a parking spot is empty based on the processed image data.

## ⚙️ Configuration

You can adjust the detection sensitivity and other parameters by modifying the designated variables within `main.py`.

## 🤝 Contribution

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that your contributions adhere to the [contribution guidelines](CONTRIBUTING.md).

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

For any queries or support regarding this project, feel free to reach out to us at [akshayajs2811@gmail.com](mailto:akshayajs2811@gmail.com).

Happy Parking! 🚗
