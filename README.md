## Image Processing Pipeline

### Overview

This project demonstrates a image processing pipeline. The focus is on understanding how raw image data can be transformed through processing techniques such as filtering, denoising and histogram equalization. 


### Techniques Covered

The pipeline includes the following stages:

* Image loading and visualization
* Grayscale conversion and normalization
* Noise reduction using spatial filters
* Visualization of intermediate and final results

These techniques form the foundation of many applications in computer vision, including medical imaging.


### Project Structure

* **`main_pipeline.ipynb`** – Primary notebook containing the image processing workflow
* **`experiments_and_notes.ipynb`** – Exploratory experiments and additional trials
* **`README.md`** – Project overview and usage instructions


### How to Run

1. Clone the repository
2. Open `main_pipeline.ipynb` in Jupyter Notebook or Google Colab
3. Run the notebook cells sequentially from top to bottom

All results and visual outputs are generated within the notebook.


### Results

The notebook produces visual comparisons between original and processed images at each stage of the pipeline.


### Key Takeaways

This project highlights the trade-offs involved in general image processing, such as noise reduction versus detail preservation and the sensitivity of results to parameter choices. It emphasizes understanding why specific transformations are applied, not just how to apply them.


### Tools Used

* Python
* OpenCV
* NumPy
* Matplotlib
