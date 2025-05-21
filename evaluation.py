import pandas as pd
import os

import re



def read_txt_file(path):
    results = []
    with open(path,'r') as r_file:
        content = r_file.readlines()
    for ct in content:
        information = ct.replace('\n','').split(' detections: ')
        time_layer = information[0]
        detections = information[1]
        bboxes = re.findall(r'\(\d+,\s*\d+,\s*\d+,\s*\d+\)', detections)
        bboxes = tuple(tuple(map(int, re.findall(r'\d+', bbox))) for bbox in bboxes)
        results.append([time_layer,bboxes])
    
    return pd.DataFrame(results)

def find_actual_file_from_prediction(predicted_file):
    actual_number = predicted_file.split('//')[-1].split('_')[0]
    return actual_number


def compute_f1(precision, recall):
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)

def iou(boxA, boxB):
    """
    Computes the Intersection over Union (IoU) between two bounding boxes.
    
    Parameters:
        boxA (tuple): (x1, y1, x2, y2) of the first box
        boxB (tuple): (x1, y1, x2, y2) of the second box
    
    Returns:
        float: IoU value between 0 and 1
    """
    # Determine the coordinates of the intersection rectangle
    x_left   = max(boxA[0], boxB[0])
    y_top    = max(boxA[1], boxB[1])
    x_right  = min(boxA[2], boxB[2])
    y_bottom = min(boxA[3], boxB[3])

    # Compute the area of intersection rectangle
    if x_right < x_left or y_bottom < y_top:
        return 0.0  # No overlap

    inter_area = (x_right - x_left) * (y_bottom - y_top)

    # Compute the area of both bounding boxes
    boxA_area = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxB_area = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    # Compute the IoU
    # iou = inter_area / float(boxA_area + boxB_area - inter_area)
    iou = inter_area/boxB_area
    return iou

def compute_precision_recall(data, iou_threshold=0.5):
    TP = 0
    FP = 0
    FN = 0

    for parts in data.values:  # Skip header

        if len(parts) != 3:
            continue

        actual_bboxes = parts[1]
        predicted_bboxes = parts[2]

        matched_gt = set()
        matched_pred = set()

        for i, pred in enumerate(predicted_bboxes):
            best_iou = 0
            best_gt = -1
            for j, gt in enumerate(actual_bboxes):
                if j in matched_gt:
                    continue
                score = iou(pred, gt)
                if score > best_iou:
                    best_iou = score
                    best_gt = j

            if best_iou >= iou_threshold:
                TP += 1
                matched_gt.add(best_gt)
                matched_pred.add(i)
            else:
                FP += 1

        FN += len(actual_bboxes) - len(matched_gt)

    precision = TP / (TP + FP) if TP + FP > 0 else 0.0
    recall = TP / (TP + FN) if TP + FN > 0 else 0.0

    return precision, recall, TP, FP, FN

def get_list_actual_file():
    actual_folder = 'Data//Annotation_update_180925//'
    list_actual_file = os.listdir(actual_folder)
    actual_file_end = {}
    for actual_file in list_actual_file:
        actual_file.split('_')[1]
        actual_file_end[actual_file.split('_')[1]] = actual_folder + actual_file
    return actual_file_end

def get_actual_file_from_predicted_file(predicted_file):
    actual_file_end = get_list_actual_file()
    actual_number = find_actual_file_from_prediction(predicted_file)
    actual_file = actual_file_end[actual_number]
    return actual_file

def evalute_prediction(predicted_file):
    actual_file = get_actual_file_from_predicted_file(predicted_file)

    df_predicted = read_txt_file(predicted_file)
    df_predicted.columns = ['time_layer','prediction']

    df_actual = read_txt_file(actual_file)
    df_actual.columns = ['time_layer','actual']
    df_merge = df_actual.merge(df_predicted,on='time_layer')

    # Compute metrics
    precision, recall, TP, FP, FN = compute_precision_recall(df_merge)
    return compute_f1(precision,recall),precision, recall, TP, FP, FN

results_folders = 'Experiment_Results'
list_models_folder = os.listdir(results_folders)
results = []
for models_folder in list_models_folder:
    list_file_one_fold = os.listdir(results_folders + '//' + models_folder + '//txt')
    for predicted_file in list_file_one_fold:
        predicted_file = results_folders + '//' + models_folder + '//txt//' + predicted_file
        f1,precision, recall, TP, FP, FN = evalute_prediction(predicted_file)
        results.append([models_folder,predicted_file.split('.')[0].split('//')[-1].split('_')[0],f1,precision, recall, TP, FP, FN])

df = pd.DataFrame(results,columns=['fold','video','f1-score','precision','recall','TP','FP','FN'])
df.to_excel('results.xlsx',index=False)