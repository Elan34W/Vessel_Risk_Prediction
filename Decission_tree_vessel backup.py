import csv

# Function to load data from CSV
def load_data_from_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                'umur_kapal': int(row['Age(year)']),
                'panjang_kapal': int(row['Length (m)']),
                'lebar_kapal': int(row['Width (m)']),
                'gross_tonnage': int(row['Gross Tonnage']),
                'deadweight_tonnage': int(row['Summer Deadweight (t)']),
                'klasifikasi': row['Accident Risk'].lower()
            })
    return data

# Load the data
data = load_data_from_csv('Data_vessel.csv')

# Functions for decision tree

# Function to build decision tree
def build_tree(data):
    if len(set(row['klasifikasi'] for row in data)) == 1:
        return {'kelas': data[0]['klasifikasi']}
    else:
        best_attribute, best_threshold = find_best_split(data)
        if best_attribute is None or best_threshold is None:
            return {'kelas': max(set(row['klasifikasi'] for row in data), key=[row['klasifikasi'] for row in data].count)}
        left_data, right_data = split_data(data, best_attribute, best_threshold)
        left_subtree = build_tree(left_data)
        right_subtree = build_tree(right_data)
        return {'splitting_attribute': best_attribute, 'threshold': best_threshold, 'left_subtree': left_subtree, 'right_subtree': right_subtree}

# Function to find the best attribute and threshold for splitting
def find_best_split(data):
    best_gini = float('inf')
    best_attribute = None
    best_threshold = None
    for attribute in data[0].keys():
        if attribute != 'klasifikasi':
            values = sorted(list(set(row[attribute] for row in data)))
            for i in range(1, len(values)):
                threshold = (values[i - 1] + values[i]) / 2
                left_data, right_data = split_data(data, attribute, threshold)
                gini = calculate_gini(left_data, right_data)
                if gini < best_gini:
                    best_gini = gini
                    best_attribute = attribute
                    best_threshold = threshold
    return best_attribute, best_threshold

# Function to split the data based on an attribute and threshold
def split_data(data, attribute, threshold):
    left_data = [row for row in data if row[attribute] <= threshold]
    right_data = [row for row in data if row[attribute] > threshold]
    return left_data, right_data

# Function to calculate Gini index
def calculate_gini(left_data, right_data):
    total_instances = len(left_data) + len(right_data)
    gini_left = 0
    gini_right = 0
    
    if len(left_data) > 0:
        left_classes = [row['klasifikasi'] for row in left_data]
        gini_left = 1 - sum((left_classes.count(c) / len(left_data)) ** 2 for c in set(left_classes))
    
    if len(right_data) > 0:
        right_classes = [row['klasifikasi'] for row in right_data]
        gini_right = 1 - sum((right_classes.count(c) / len(right_data)) ** 2 for c in set(right_classes))
    
    gini_index = (len(left_data) / total_instances) * gini_left + (len(right_data) / total_instances) * gini_right
    return gini_index

# Function to predict using the decision tree
def predict(tree, sample):
    if 'kelas' in tree:
        return tree['kelas']
    else:
        attr = tree['splitting_attribute']
        threshold = tree['threshold']
        if sample[attr] <= threshold:
            return predict(tree['left_subtree'], sample)
        else:
            return predict(tree['right_subtree'], sample)

# Build the decision tree from the data
decision_tree = build_tree(data)

# Test predictions with new samples
new_sample = {
    'umur_kapal': 8,
    'panjang_kapal': 170, 
    'lebar_kapal': 16, 
    'gross_tonnage': 900, 
    'deadweight_tonnage': 400
    }
prediction = predict(decision_tree, new_sample)
print("Prediction:", prediction)

new_sample1 = {
    'umur_kapal': 16, 
    'panjang_kapal': 300, 
    'lebar_kapal': 60, 
    'gross_tonnage': 160271, 
    'deadweight_tonnage': 299868
    }
prediction = predict(decision_tree, new_sample1)
print("Prediction:", prediction)

# Function to input new sample and predict
def input_new_sample():
    umur_kapal = int(input("\nEnter umur kapal (Age of the ship in years): "))
    panjang_kapal = int(input("Enter panjang kapal (Length of the ship in meters): "))
    lebar_kapal = int(input("Enter lebar kapal (Width of the ship in meters): "))
    gross_tonnage = int(input("Enter gross tonnage: "))
    deadweight_tonnage = int(input("Enter deadweight tonnage: "))
    
    new_sample = {
        'umur_kapal': umur_kapal,
        'panjang_kapal': panjang_kapal,
        'lebar_kapal': lebar_kapal,
        'gross_tonnage': gross_tonnage,
        'deadweight_tonnage': deadweight_tonnage
    }
    
    prediction = predict(decision_tree, new_sample)
    print("Prediction:", prediction)

# Test predictions with new samples
input_new_sample()

# def print_tree(tree, indent=''):
#     if 'kelas' in tree:
#         print(indent + "Leaf Node: " + tree['kelas'])
#     else:
#         print(indent + f"Split: {tree['splitting_attribute']} <= {tree['threshold']}")
#         print(indent + 'Left Subtree:')
#         print_tree(tree['left_subtree'], indent + '  ')
#         print(indent + 'Right Subtree:')
#         print_tree(tree['right_subtree'], indent + '  ')

# # Print the decision tree structure
# print_tree(decision_tree)

# sample_akurasi1 = {'umur_kapal': 5, 'panjang_kapal': 137, 'lebar_kapal': 23, 'gross_tonnage': 10461, 'deadweight_tonnage': 11164}
# prediction = predict(decision_tree, sample_akurasi1)
# print("Prediction:", prediction)

# sample_akurasi2 = {'umur_kapal': 12, 'panjang_kapal': 333, 'lebar_kapal': 60, 'gross_tonnage': 161513, 'deadweight_tonnage': 318123}
# prediction = predict(decision_tree, sample_akurasi2)
# print("Prediction:", prediction)

# sample_akurasi3 = {'umur_kapal': 8, 'panjang_kapal': 333, 'lebar_kapal': 60, 'gross_tonnage': 161319, 'deadweight_tonnage': 300932}
# prediction = predict(decision_tree, sample_akurasi3)
# print("Prediction:", prediction)

# sample_akurasi4 = {'umur_kapal': 38, 'panjang_kapal': 72, 'lebar_kapal': 16, 'gross_tonnage': 2573, 'deadweight_tonnage': 662}
# prediction = predict(decision_tree, sample_akurasi4)
# print("Prediction:", prediction)

# sample_akurasi5 = {'umur_kapal': 56, 'panjang_kapal': 41, 'lebar_kapal': 11, 'gross_tonnage': 387, 'deadweight_tonnage': 179}
# prediction = predict(decision_tree, sample_akurasi5)
# print("Prediction:", prediction)

# sample_akurasi6 = {'umur_kapal': 1, 'panjang_kapal': 230, 'lebar_kapal': 31, 'gross_tonnage': 47653, 'deadweight_tonnage': 8850}
# prediction = predict(decision_tree, sample_akurasi6)
# print("Prediction:", prediction)

# sample_akurasi7 = {'umur_kapal': 14, 'panjang_kapal': 198, 'lebar_kapal': 26, 'gross_tonnage': 32477, 'deadweight_tonnage': 3780}
# prediction = predict(decision_tree, sample_akurasi7)
# print("Prediction:", prediction)

# sample_akurasi8 = {'umur_kapal': 9, 'panjang_kapal': 333, 'lebar_kapal': 60, 'gross_tonnage': 166178, 'deadweight_tonnage': 319896}
# prediction = predict(decision_tree, sample_akurasi8)
# print("Prediction:", prediction)

# sample_akurasi9 = {'umur_kapal': 50, 'panjang_kapal': 111, 'lebar_kapal': 19, 'gross_tonnage': 6991, 'deadweight_tonnage': 855}
# prediction = predict(decision_tree, sample_akurasi9)
# print("Prediction:", prediction)

# sample_akurasi10 = {'umur_kapal': 16, 'panjang_kapal': 183, 'lebar_kapal': 32, 'gross_tonnage': 29300, 'deadweight_tonnage': 53160}
# prediction = predict(decision_tree, sample_akurasi10)
# print("Prediction:", prediction)