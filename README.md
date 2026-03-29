# **Eyelink Pupillometry – Spanish Subjunctive Processing**

This repository contains the implementation of a **pupillometry-based psycholinguistic experiment** investigating how bilingual speakers process **Spanish subjunctive morphology in real time**.

---

## **Project Overview**

This project uses:

- **EyeLink 1000 Plus** for eye-tracking and pupil dilation  
- **Experiment Builder (EB 2.6.11)** for experimental control  
- **Auditory stimuli** for sentence processing tasks  

The experiment measures **pupil dilation as an index of cognitive load** during morphosyntactic processing.

This is an **ongoing research project** focused on testing predictions from the *Bottleneck Hypothesis* across:

- Native speakers  
- Heritage speakers  
- L2 learners  

---

## **System Architecture**

The experiment runs on a **dual-computer setup**:

### **Display PC**
- Runs Experiment Builder  
- Presents stimuli (audio + visual)  
- Records behavioral responses  
- Generates `.dat` files  

### **EyeLink Host PC**
- Records eye-tracking data  
- Stores `.edf` files  
- Communicates with Display PC via Ethernet  
- Host: 100.1.1.1
- Display: 100.1.1.2


---

## **Experiment Implementation (Experiment Builder)**

The experiment was designed and implemented entirely in **Experiment Builder**, including:

- Trial structure definition using **DataSource `.dat` files**
- Integration of **auditory stimuli with precise timing control**
- Use of **custom Python classes (pylink)** for communication with EyeLink
- Calibration and validation routines for eye-tracking accuracy
- Trial-level event logging for synchronization between behavioral and physiological data

Key components:

- **Datasets**: Define trial conditions (e.g., lexical frequency, durations)
- **Timeline structure**: Controls stimulus presentation and response collection
- **Custom code**: Handles EyeLink communication and data transfer
- **Audio playback**: Managed with low-latency configuration (ASIO on Display PC)

---

## **Running the Experiment**

### Important
- Running inside Experiment Builder (**F9 Test Run**) does **NOT** save real data  
- You must run the **compiled `.exe`**

### **Steps**

1. Open the project in Experiment Builder  
2. Compile the experiment  
3. Run the executable from:


---

## **Data Output**

| File Type | Description | Location |
|----------|------------|---------|
| `.dat` | Behavioral data (trial-level responses) | Display PC |
| `.edf` | Eye-tracking + pupil data | EyeLink Host PC |
| `.csv` | Processed datasets | `/data/processed/` |

---

## **Data Processing Pipeline**

1. Export `.edf` files from the EyeLink Host PC  
2. Convert `.edf` → ASCII / CSV  
3. Clean behavioral `.dat` files  
4. Merge behavioral and eye-tracking data  
5. Generate analysis-ready datasets  

---

## Author
Davo Acevedo-Cardona
M.S. Human Language Technology – University of Arizona
