import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import os
import datetime
# Read data from a CSV file

# current_dir = os.getcwd()
# csv_file_path = current_dir+'\ivykiss_front_check_list.csv'  # Replace with your CSV file path
csv_file_path = r"C:\Users\KISS Admin\Desktop\IVYENT_DH\Rq25. Image Sql\front_check_list.csv"  
df = pd.read_csv(csv_file_path)

selected_links = []  # Empty list to store selected links

# Check if "no front tag_selected.csv" exists
# output_filename = "no front tag_selected.csv"
# if os.path.exists(output_filename):
#     # Move the file to the "past" folder and add today's date to the filename
#     today_date = datetime.date.today().strftime("%Y-%m-%d")
#     new_filename = f"past/ivykiss_no front tag_selected_{today_date}_moved.csv"
#     os.makedirs("past", exist_ok=True)
#     os.rename(output_filename, new_filename)

# Loop through the DataFrame and display images
for index, row in df.iterrows():
    
    row=row[pd.isna(row)==False]
    print(f"Material: {row['material']}")

    num_links = len(row) - 1
    figsize_width = 5 * num_links if num_links > 1 else 5
    fig, axes = plt.subplots(1, num_links, figsize=(figsize_width, 5))

    if num_links == 1:
        axes = [axes]  # Convert the single Axes object to a list with one element

    for i, (link, ax) in enumerate(zip(row[1:], axes), start=1):
        response = requests.get(link)
        img = Image.open(BytesIO(response.content))
        ax.imshow(img)
        ax.set_title(f"Image {i}")
        ax.axis('off')

    plt.show()

    # Ask the user to select the index of the image
    while True:
        try:
            selected_index = int(input("Select the index of the image: (0 means no good image) "))
            if 0 <= selected_index <= len(row)-1:
                break
            else:
                print("Invalid input. Please enter a number.(0 means no good image)")
        except ValueError:
            print("Invalid input. Please enter a number.(0 means no good image)")
    if selected_index!= 0:
        selected_links.append([row['material'],row[selected_index]])  # Store the selected link

# Create a new DataFrame with the material and selected link
selected_df = pd.DataFrame(selected_links)

selected_df.columns = selected_df.columns.astype(str)
selected_df = selected_df.rename(columns={'0': 'material'})

selected_df.to_csv("no front tag_selected.csv", index=False)
selected_df.to_csv("Product Photo.csv", index=False)

print("end")