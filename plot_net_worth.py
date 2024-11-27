import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# set files to read in
files = [
    #{'name': 'MMM01_5_99_5.csv', 'label': 'MMM01_5_99_5', 'color': 'red'},
    {'name': 'M02_3_0.9_3.csv', 'label': 'M02_3_0.9_3'},
    {'name': 'M02_3_0.9_5.csv', 'label': 'M02_3_0.9_5'},
    {'name': 'M02_3_0.9_7.csv', 'label': 'M02_3_0.9_7'},
    {'name': 'M02_3_0.95_3.csv', 'label': 'M02_3_0.9_3'},
    {'name': 'M02_3_0.95_5.csv', 'label': 'M02_3_0.9_5'},
    {'name': 'M02_3_0.95_7.csv', 'label': 'M02_3_0.9_7'},
    {'name': 'M02_3_0.9999_3.csv', 'label': 'M02_3_0.9999_3'},
    {'name': 'M02_3_0.9999_5.csv', 'label': 'M02_3_0.9999_5'},
    {'name': 'M02_3_0.9999_7.csv', 'label': 'M02_3_0.9999_7'},
    {'name': 'M02_5_0.9_3.csv', 'label': 'M02_5_0.9_3'},
    {'name': 'M02_5_0.9_5.csv', 'label': 'M02_5_0.9_5'},
    {'name': 'M02_5_0.9_7.csv', 'label': 'M02_5_0.9_7'},
    {'name': 'M02_5_0.95_3.csv', 'label': 'M02_5_0.95_3'},
    {'name': 'M02_5_0.95_5.csv', 'label': 'M02_5_0.95_5'},
    {'name': 'M02_5_0.95_7.csv', 'label': 'M02_5_0.95_7'},
    {'name': 'M02_5_0.9999_3.csv', 'label': 'M02_5_0.9999_3'},
    {'name': 'M02_5_0.9999_7.csv', 'label': 'M02_5_0.9999_7'},
    {'name': 'M02_7_0.9_3.csv', 'label': 'M02_7_0.9_3'},
    {'name': 'M02_7_0.9_5.csv', 'label': 'M02_7_0.9_5'},
    {'name': 'M02_7_0.9_7.csv', 'label': 'M02_7_0.9_7'},
    {'name': 'M02_7_0.95_3.csv', 'label': 'M02_7_0.95_3'},
    {'name': 'M02_7_0.95_5.csv', 'label': 'M02_7_0.95_5'},
    {'name': 'M02_7_0.95_7.csv', 'label': 'M02_7_0.95_7'},
    {'name': 'M02_7_0.9999_3.csv', 'label': 'M02_7_0.9999_3'},
    {'name': 'M02_7_0.9999_5.csv', 'label': 'M02_7_0.9999_5'},
    {'name': 'M02_7_0.9999_7.csv', 'label': 'M02_7_0.9999_7'},
    {'name': 'MMM01_5_99_5.csv', 'label': 'MMM01_5_99_5', 'color': 'red'},

]

# generate more colour options
colors = list(mcolors.TABLEAU_COLORS) + list(mcolors.CSS4_COLORS)[:24]

# set figure
plt.figure(figsize=(15, 8))

# variables to store minimal and maximal
all_data_max = float('-inf')
all_data_min = float('inf')

# Plot the curve for every read data
for i, file_info in enumerate(files):
    try:
        # read CSV file
        data = pd.read_csv(file_info['name'], header=None, names=['timestamp', 'networth'])
        
        # update with the minimal and maximal
        all_data_max = max(all_data_max, data['networth'].max())
        all_data_min = min(all_data_min, data['networth'].min())
        
        # choose colour
        color = file_info.get('color', colors[i % len(colors)])
        
        plt.plot(data['timestamp'], 
                data['networth'],
                color=color,
                linewidth=1.5,
                label=f"{i+1}. {file_info['label']}",
                alpha=0.8)
        
        # Plot number of the curve
        plt.annotate(f"{i+1}", 
                    (data['timestamp'].iloc[-1], data['networth'].iloc[-1]),
                    xytext=(10, 0),
                    textcoords='offset points',
                    fontsize=10,
                    bbox=dict(facecolor='white', 
                            edgecolor='none',
                            alpha=0.7,
                            pad=0.1))
        
    except FileNotFoundError:
        print(f"Warning: File {file_info['name']} not found. Skipping...")
        continue


if all_data_max != float('-inf') and all_data_min != float('inf'):
    margin = (all_data_max - all_data_min) * 0.1
    plt.ylim(all_data_min - margin, all_data_max + margin)

# set the ticks of x axis
plt.xticks([0, 5000, 10000, 15000, 20000, 25000, 30000],
           ['0', '5000', '10000', '15000', '20000', '25000', '30000'],
           rotation=0)

# add titles and labels
plt.title('Net Worth Comparison Over Time', fontsize=14, pad=15)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Net Worth', fontsize=12)

# 
n_cols = min(3, len(files) // 9 + 1)
plt.legend(bbox_to_anchor=(1.05, 1), 
          loc='upper left', 
          ncol=n_cols,
          borderaxespad=0.,
          fontsize=10)

# add grids
plt.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()

plt.show()