# Fast-and-Robust-UAV-to-UAV-Detection-and-Tracking

This repository is cloned from [https://github.com/jingliinpurdue/Fast-and-Robust-UAV-to-UAV-Detection-and-Tracking](https://github.com/jingliinpurdue/Fast-and-Robust-UAV-to-UAV-Detection-and-Tracking). Thank you to the original authors for their repository.

## Requirements

-   Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Step 1: Infer the models for each fold**

    Run the following command in the terminal to perform inference for all folds (from 1 to 5):
    ```bash
    python main.py
    ```

2.  **Step 2: Evaluate the inference results**

    After inference, use the following command to evaluate the results by computing the F1-score, precision, and recall for each fold:
    ```bash
    python evaluation.py
    ```

3.  **Step 3: Analyze the results**

    For analysis, open and inspect the generated Excel file:
    ```
    results.xlsx
    ```

## Results

Results are saved under the `Experiment_Results` folder and include:

*   `.txt` files with detected bounding boxes.
*   Videos with ground truth and detection results.
* Can access the experimental results at here: https://tql3p-my.sharepoint.com/:f:/g/personal/lexuanhoang120_tql3p_onmicrosoft_com/EpShD3_F7_9ItVvoJjAeJkEB2rSoBv5ILkE7_DAXhZPurg?e=EXktBN

## Dataset

The dataset used in this work can be found at:
[https://engineering.purdue.edu/~bouman/UAV_Dataset/](https://engineering.purdue.edu/~bouman/UAV_Dataset/)

## Citation

If you use this work, please cite the original paper:

J. Li, D. Ye, M. Kolsch, J. Wachs and C. Bouman, "Fast and Robust UAV to UAV Detection and Tracking from Video" in *IEEE Transactions on Emerging Topics in Computing*.
doi: [10.1109/TETC.2021.3104555](https://doi.org/10.1109/TETC.2021.3104555)
url: [https://doi.ieeecomputersociety.org/10.1109/TETC.2021.3104555](https://doi.ieeecomputersociety.org/10.1109/TETC.2021.3104555)
Additional link: [https://www.computer.org/csdl/journal/ec/5555/01/09519550/1wc8Vbe1r7G](https://www.computer.org/csdl/journal/ec/5555/01/09519550/1wc8Vbe1r7G)

```bibtex
@ARTICLE {9519550,
  author = {J. Li and D. Ye and M. Kolsch and J. P. Wachs and C. A. Bouman},
  journal = {IEEE Transactions on Emerging Topics in Computing},
  title = {Fast and Robust UAV to UAV Detection and Tracking from Video},
  year = {5555},
  volume = {},
  number = {01},
  issn = {2168-6750},
  pages = {1-1},
  keywords = {target tracking;cameras;detectors;unmanned aerial vehicles;optical imaging;radar tracking;optical detectors},
  doi = {10.1109/TETC.2021.3104555},
  publisher = {IEEE Computer Society},
  address = {Los Alamitos, CA, USA},
  month = {aug}
}