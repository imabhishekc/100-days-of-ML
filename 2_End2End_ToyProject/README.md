# Day 2: Logistic Regression — Student Placement Prediction

This notebook is part of my **100 Days of Machine Learning** challenge.

On Day 2, I built a simple Machine Learning model using **Logistic Regression** to predict whether a student will be placed based on their **CGPA** and **IQ**.

---

## Project Objective

To understand and demonstrate the basic **ML pipeline** using a toy dataset:

- Dataset: 100 sample student records
- Features: `CGPA`, `IQ`
- Target: `Placement` (0 = Not Placed, 1 = Placed)

---

## Dataset Description

The dataset contains the following columns:

- `cgpa`: Student's cumulative GPA
- `iq`: Student's IQ level
- `placement`: Binary output indicating placement status (1 = Placed, 0 = Not Placed)

> Note: The first column (index or ID) is dropped during preprocessing.

---

## Workflow Overview

The notebook demonstrates the **full Machine Learning workflow**:

1. **Loading the Data**  
   Using `pandas` to load and inspect the dataset.

2. **Preprocessing**  
   Dropping unnecessary columns.

3. **EDA (Exploratory Data Analysis)**  
   Visualizing data distribution with `matplotlib`.

4. **Feature and Label Extraction**  
   Separating inputs (CGPA, IQ) and output (Placement).

5. **Train-Test Split**  
   Using `train_test_split()` to split the data.

6. **Feature Scaling**  
   Normalizing features using `StandardScaler`.

7. **Model Training**  
   Training a `LogisticRegression` model.

8. **Model Evaluation**  
   Calculating accuracy score and making predictions.

9. **Visualization**  
   Plotting decision boundaries using `mlxtend`.

10. **Model Saving**  
    Saving the trained model using `pickle`.

---

## Requirements

Make sure the following Python libraries are installed:

- numpy
- pandas
- matplotlib
- scikit-learn
- mlxtend
- pickle (standard Python module)

Install missing ones using:

```bash
pip install numpy pandas matplotlib scikit-learn mlxtend
