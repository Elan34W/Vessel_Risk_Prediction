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
    if best_attribute is None or best_threshold is None:
        print("No valid split found.")
    else:
        print(f"Best split found on attribute {best_attribute} with threshold {best_threshold}")
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
new_sample = {'umur_kapal': 8, 'panjang_kapal': 220, 'lebar_kapal': 32, 'gross_tonnage': 1200, 'deadweight_tonnage': 600}
prediction = predict(decision_tree, new_sample)
print("Prediction:", prediction)

new_sample1 = {'umur_kapal': 20, 'panjang_kapal': 333, 'lebar_kapal': 60, 'gross_tonnage': 160271, 'deadweight_tonnage': 299868}
prediction = predict(decision_tree, new_sample1)
print("Prediction:", prediction)

# Function to input new sample and predict
def input_new_sample():
    umur_kapal = int(input("Enter umur kapal (Age of the ship in years): "))
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