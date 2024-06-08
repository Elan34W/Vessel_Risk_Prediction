import csv

# Data
data = [
    {'umur_kapal': 14, 'panjang_kapal': 143, 'lebar_kapal': 23, 'gross_tonnage': 12974, 'deadweight_tonnage': 16953, 'klasifikasi': 'high'},
    {'umur_kapal': 5, 'panjang_kapal': 320, 'lebar_kapal': 55, 'gross_tonnage': 122967, 'deadweight_tonnage': 243377, 'klasifikasi': 'low'},
    {'umur_kapal': 12, 'panjang_kapal': 113, 'lebar_kapal': 18, 'gross_tonnage': 5422, 'deadweight_tonnage': 7595, 'klasifikasi': 'high'},
    {'umur_kapal': 32, 'panjang_kapal': 91, 'lebar_kapal': 15, 'gross_tonnage': 4200, 'deadweight_tonnage': 695, 'klasifikasi': 'low'},
    {'umur_kapal': 12, 'panjang_kapal': 143, 'lebar_kapal': 17, 'gross_tonnage': 8911, 'deadweight_tonnage': 14592, 'klasifikasi': 'high'},
    {'umur_kapal': 3, 'panjang_kapal': 400, 'lebar_kapal': 61, 'gross_tonnage': 236583, 'deadweight_tonnage': 221251, 'klasifikasi': 'low'},
    {'umur_kapal': 13, 'panjang_kapal': 150, 'lebar_kapal': 23, 'gross_tonnage': 13097, 'deadweight_tonnage': 19998, 'klasifikasi': 'high'},
    {'umur_kapal': 1, 'panjang_kapal': 400, 'lebar_kapal': 62, 'gross_tonnage': 236078, 'deadweight_tonnage': 272373, 'klasifikasi': 'low'},
    {'umur_kapal': 8, 'panjang_kapal': 133, 'lebar_kapal': 23, 'gross_tonnage': 10830, 'deadweight_tonnage': 14911, 'klasifikasi': 'high'},
    {'umur_kapal': 2, 'panjang_kapal': 399, 'lebar_kapal': 61, 'gross_tonnage': 236228, 'deadweight_tonnage': 224982, 'klasifikasi': 'low'},
    {'umur_kapal': 28, 'panjang_kapal': 203, 'lebar_kapal': 31, 'gross_tonnage': 29181, 'deadweight_tonnage': 41590, 'klasifikasi': 'high'},
    {'umur_kapal': 4, 'panjang_kapal': 344, 'lebar_kapal': 42, 'gross_tonnage': 184089, 'deadweight_tonnage': 16887, 'klasifikasi': 'low'},
    {'umur_kapal': 7, 'panjang_kapal': 135, 'lebar_kapal': 23, 'gross_tonnage': 12061, 'deadweight_tonnage': 14986, 'klasifikasi': 'high'},
    {'umur_kapal': 16, 'panjang_kapal': 333, 'lebar_kapal': 38, 'gross_tonnage': 137936, 'deadweight_tonnage': 13413, 'klasifikasi': 'low'},
    {'umur_kapal': 81, 'panjang_kapal': 184, 'lebar_kapal': 18, 'gross_tonnage': 10532, 'deadweight_tonnage': 15850, 'klasifikasi': 'high'},
    {'umur_kapal': 25, 'panjang_kapal': 199, 'lebar_kapal': 24, 'gross_tonnage': 28890, 'deadweight_tonnage': 2557, 'klasifikasi': 'low'},
    {'umur_kapal': 8, 'panjang_kapal': 180, 'lebar_kapal': 30, 'gross_tonnage':21530, 'deadweight_tonnage': 34534, 'klasifikasi': 'high'}, 
    {'umur_kapal': 10, 'panjang_kapal': 200, 'lebar_kapal': 32, 'gross_tonnage': 35884, 'deadweight_tonnage': 63166, 'klasifikasi': 'low'},
    {'umur_kapal': 13, 'panjang_kapal': 229, 'lebar_kapal': 32, 'gross_tonnage': 43790, 'deadweight_tonnage': 80325, 'klasifikasi': 'high'},
    {'umur_kapal': 6, 'panjang_kapal': 362, 'lebar_kapal': 65, 'gross_tonnage': 203953, 'deadweight_tonnage': 399214, 'klasifikasi': 'low'},
    {'umur_kapal': 14, 'panjang_kapal': 250, 'lebar_kapal': 44, 'gross_tonnage': 63294, 'deadweight_tonnage': 115514, 'klasifikasi': 'high'},
    {'umur_kapal': 5, 'panjang_kapal': 228, 'lebar_kapal': 38, 'gross_tonnage': 43693, 'deadweight_tonnage': 74999, 'klasifikasi': 'low'},
    {'umur_kapal': 11, 'panjang_kapal': 255, 'lebar_kapal': 37, 'gross_tonnage': 52467, 'deadweight_tonnage': 63014, 'klasifikasi': 'high'},
    {'umur_kapal': 11, 'panjang_kapal': 228, 'lebar_kapal': 37, 'gross_tonnage': 45452, 'deadweight_tonnage': 81305, 'klasifikasi': 'low'},
    {'umur_kapal': 43, 'panjang_kapal': 139, 'lebar_kapal': 28, 'gross_tonnage': 6969, 'deadweight_tonnage': 1099, 'klasifikasi': 'high'},
    {'umur_kapal': 20, 'panjang_kapal': 174, 'lebar_kapal': 29, 'gross_tonnage': 25507, 'deadweight_tonnage': 38877, 'klasifikasi': 'low'},
    {'umur_kapal': 24, 'panjang_kapal': 294, 'lebar_kapal': 32, 'gross_tonnage': 91011, 'deadweight_tonnage': 11928, 'klasifikasi': 'high'},
    {'umur_kapal': 17, 'panjang_kapal': 182, 'lebar_kapal': 28, 'gross_tonnage': 25174, 'deadweight_tonnage': 38106, 'klasifikasi': 'low'},
    {'umur_kapal': 23, 'panjang_kapal': 293, 'lebar_kapal': 40, 'gross_tonnage': 90090, 'deadweight_tonnage': 10759, 'klasifikasi': 'high'},
    {'umur_kapal': 18, 'panjang_kapal': 330, 'lebar_kapal': 60, 'gross_tonnage': 157245, 'deadweight_tonnage': 300398, 'klasifikasi': 'low'},
    {'umur_kapal': 59, 'panjang_kapal': 85, 'lebar_kapal': 19, 'gross_tonnage': 1486, 'deadweight_tonnage': 460, 'klasifikasi': 'high'},
    {'umur_kapal': 21, 'panjang_kapal': 274, 'lebar_kapal': 48, 'gross_tonnage': 81866, 'deadweight_tonnage': 149962, 'klasifikasi': 'low'},
    {'umur_kapal': 20, 'panjang_kapal': 146, 'lebar_kapal': 24, 'gross_tonnage': 11628, 'deadweight_tonnage': 20704, 'klasifikasi': 'high'},
    {'umur_kapal': 13, 'panjang_kapal': 254, 'lebar_kapal': 43, 'gross_tonnage': 62272, 'deadweight_tonnage': 106668, 'klasifikasi': 'low'},
    {'umur_kapal': 15, 'panjang_kapal': 145, 'lebar_kapal': 23, 'gross_tonnage': 11939, 'deadweight_tonnage': 17095, 'klasifikasi': 'high'},
    {'umur_kapal': 24, 'panjang_kapal': 236, 'lebar_kapal': 38, 'gross_tonnage': 49565, 'deadweight_tonnage': 88018, 'klasifikasi': 'low'},
    {'umur_kapal': 6, 'panjang_kapal': 226, 'lebar_kapal': 24, 'gross_tonnage': 24640, 'deadweight_tonnage': 37411, 'klasifikasi': 'high'},
    {'umur_kapal': 4, 'panjang_kapal': 400, 'lebar_kapal': 62, 'gross_tonnage': 232311, 'deadweight_tonnage': 229039, 'klasifikasi': 'low'},
    {'umur_kapal': 41, 'panjang_kapal': 223, 'lebar_kapal': 23, 'gross_tonnage': 22388, 'deadweight_tonnage': 36245, 'klasifikasi': 'high'},
    {'umur_kapal': 1, 'panjang_kapal': 400, 'lebar_kapal': 61, 'gross_tonnage': 229376, 'deadweight_tonnage': 229348, 'klasifikasi': 'low'},
    {'umur_kapal': 17, 'panjang_kapal': 164, 'lebar_kapal': 23, 'gross_tonnage': 12776, 'deadweight_tonnage': 20718, 'klasifikasi': 'high'},
    {'umur_kapal': 9, 'panjang_kapal': 329, 'lebar_kapal': 45, 'gross_tonnage': 143730, 'deadweight_tonnage': 11793, 'klasifikasi': 'low'},
    {'umur_kapal': 29, 'panjang_kapal': 156, 'lebar_kapal': 21, 'gross_tonnage': 17450, 'deadweight_tonnage': 1790, 'klasifikasi': 'high'},
    {'umur_kapal': 24, 'panjang_kapal': 261, 'lebar_kapal': 32, 'gross_tonnage': 77499, 'deadweight_tonnage': 8165, 'klasifikasi': 'low'},
    {'umur_kapal': 9, 'panjang_kapal': 183, 'lebar_kapal': 32, 'gross_tonnage': 29354, 'deadweight_tonnage': 45923, 'klasifikasi': 'high'},
    {'umur_kapal': 4, 'panjang_kapal': 202, 'lebar_kapal': 32, 'gross_tonnage': 40250, 'deadweight_tonnage': 62014, 'klasifikasi': 'low'},
    {'umur_kapal': 17, 'panjang_kapal': 119, 'lebar_kapal': 18, 'gross_tonnage': 6369, 'deadweight_tonnage': 8950, 'klasifikasi': 'high'},
    {'umur_kapal': 2, 'panjang_kapal': 200, 'lebar_kapal': 32, 'gross_tonnage': 39433, 'deadweight_tonnage': 61250, 'klasifikasi': 'low'},
    {'umur_kapal': 9, 'panjang_kapal': 200, 'lebar_kapal': 32, 'gross_tonnage': 35884, 'deadweight_tonnage': 63166, 'klasifikasi': 'high'},
    {'umur_kapal': 5, 'panjang_kapal': 202, 'lebar_kapal': 32, 'gross_tonnage': 40250, 'deadweight_tonnage': 62003, 'klasifikasi': 'low'}
]

# Fungsi untuk membangun decision tree
def build_tree(data):
    # Jika hanya terdapat satu kelas, kembalikan kelas tersebut
    if len(set(row['klasifikasi'] for row in data)) == 1:
        return {'kelas': data[0]['klasifikasi']}
    else:
        # Pilih atribut terbaik untuk splitting
        best_attribute, best_threshold = find_best_split(data)
        left_data, right_data = split_data(data, best_attribute, best_threshold)
        
        # Recursive untuk membangun subtree
        left_subtree = build_tree(left_data)
        right_subtree = build_tree(right_data)
        
        return {'splitting_attribute': best_attribute, 'threshold': best_threshold, 'left_subtree': left_subtree, 'right_subtree': right_subtree}

# Fungsi untuk mencari atribut terbaik untuk splitting
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

# Fungsi untuk membagi data berdasarkan threshold
def split_data(data, attribute, threshold):
    left_data = [row for row in data if row[attribute] <= threshold]
    right_data = [row for row in data if row[attribute] > threshold]
    return left_data, right_data

# Fungsi untuk menghitung Gini index
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

# Fungsi untuk prediksi dengan decision tree
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

# Membangun decision tree dari data
decision_tree = build_tree(data)

# Contoh prediksi untuk data baru
new_sample = {'umur_kapal': 8, 'panjang_kapal': 220, 'lebar_kapal': 32, 'gross_tonnage': 1200, 'deadweight_tonnage': 600}
prediction = predict(decision_tree, new_sample)
print("Prediction:", prediction)

new_sample1 = {'umur_kapal': 20, 'panjang_kapal': 333, 'lebar_kapal': 60, 'gross_tonnage': 160271, 'deadweight_tonnage': 299868}
prediction = predict(decision_tree, new_sample1)
print("Prediction:", prediction)
