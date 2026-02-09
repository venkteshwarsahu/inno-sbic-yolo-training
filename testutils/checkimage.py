import os

dataset_path = "aadhaar-masking-dataset/images/train"
temp_path = "Aadhar-data/old aadhar/batch1"

dataset_files = set(os.listdir(dataset_path))
temp_files = os.listdir(temp_path)

found_list = []
missing_list = []

for file in temp_files:
    if file in dataset_files:
        found_list.append(file)
    else:
        missing_list.append(file)

# Print results
print("\nFOUND FILES:")
for f in found_list:
    print(f)

print("\nMISSING FILES:")
for f in missing_list:
    print(f)

print("\nSummary")
print("Total files in temp:", len(temp_files))
print("Found in dataset:", len(found_list))
print("Missing in dataset:", len(missing_list))
