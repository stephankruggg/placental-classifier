# Placental Classifier

Placental pathologies are associated with various adverse perinatal outcomes and are responsible for up to **65% of fetal deaths**. Diagnosis is traditionally performed through anatomopathological examinations, whose request depends on specialist evaluation - a factor that limits their routine application.

This project proposes the use of **Convolutional Neural Networks (CNNs)** with a transfer learning approach as an automated support system for screening morphological patterns in human placentas.

## 🧠 Overview

The study employs **pre-trained deep learning models** - `ResNet-18`, `ResNet-34`, `EfficientNet-B0`, and `EfficientNet-B4` - to:

- Classify the presence or absence of morphological alterations in placentas.
- Identify the type of morphological anomaly present.

The dataset consists of placental images collected from the Obstetrics Department of the University Hospital Polydoro Ernani de São Thiago (HU-UFSC/EBSERH) and other sources.

## ⚙️ Methodology

To overcome dataset size and class imbalance limitations, data augmentation techniques were applied.  
The models were trained using transfer learning and evaluated through standard performance metrics:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

## 📊 Results

The results demonstrated outstanding performance across both tasks:

- Classification of presence or absence of morphological alterations: The ResNet-18 model (with data augmentation) and EfficientNet-B4 (with and without data augmentation) achieved 100% across all metrics.

- Classification of anomaly type: The EfficientNet-B0 model (with data augmentation) achieved an accuracy of 97.4% and an F1-Score of 91.5%.

These results confirm the feasibility of using pre-trained convolutional neural networks for placental anomaly classification, highlighting their potential as decision-support tools in clinical practice.


## 🧩 Keywords

**Placenta**, **Convolutional Neural Networks**, **Transfer Learning**, **Image Classification**, **Macroscopic Placental Analysis**, **Disease-Predictive Placental Alterations**.

## 🏥 Acknowledgments

Developed as part of my Computer Science bachelor’s thesis at the Federal University of Santa Catarina (UFSC).
