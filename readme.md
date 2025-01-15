# Generation of Face Images from Sketches

## Project Overview
This project addresses the challenge of translating face sketches into high-quality, realistic color images. It aims to improve public security systems by enhancing the ability to confirm suspect identities through sketch-to-image translation. Additionally, the project caters to the digital entertainment industry, enabling users to convert their sketches into realistic color images with customizable facial attributes such as hair and skin color.

---

## Objectives

1. **Enhance Security Measures**
   - Aid law enforcement in identifying suspects by generating color images from sketches.

2. **Improve Image Comparison**
   - Bridge the gap between sketch images and database color images for accurate matching.

3. **Facilitate Customization in Digital Entertainment**
   - Allow users to transform sketches into color images with personalized features.

---

## Technology Stack

1. **Generative Adversarial Networks (GANs)**
   - Core technology for realistic image generation.

2. **Flask**
   - Backend framework for building the application.

3. **HTML & CSS**
   - Frontend technologies for creating a user-friendly interface.

4. **TensorFlow/PyTorch**
   - Machine learning libraries for training and deploying the GAN model.

5. **OpenCV**
   - Image processing and manipulation.

---

## Features

- **Sketch-to-Image Translation**
  - Generate realistic color images from black-and-white sketches.

- **Facial Attribute Customization**
  - Modify hair color, skin tone, and other attributes during the translation process.

- **User-Friendly Interface**
  - Web application with intuitive controls for uploading sketches and visualizing results.

- **Scalability**
  - Optimized for deployment on various devices and systems.

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/face-sketch-to-image.git
   cd face-sketch-to-image
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   flask run
   ```

5. **Access the Application**
   - Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

1. Upload a sketch image via the web interface.
2. Adjust optional settings for facial attribute customization.
3. Click "Generate" to produce the color image.
4. Download the result or visualize it directly in the browser.

---

## Dataset
- Use publicly available sketch-to-photo datasets or custom datasets for training the GAN model.
- Preprocess the data using OpenCV to ensure compatibility with the model.

---

## Model Training

1. **Prepare the Dataset**
   - Organize sketches and corresponding color images into training and testing sets.

2. **Train the GAN**
   ```bash
   python train.py --dataset_path /path/to/dataset --epochs 100
   ```

3. **Evaluate the Model**
   - Use test data to assess the quality and accuracy of generated images.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- Inspired by advancements in GANs for image generation.
- Special thanks to the open-source community for providing tools and datasets.

---

## Contact
For any questions or feedback, please reach out to:
- **Email**: swarajsolanke02@gmail.com
- **GitHub**: [Swaraj Solanke](https://github.com/Swarajsolanke)

---


