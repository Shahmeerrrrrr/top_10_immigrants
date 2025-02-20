import matplotlib.pyplot as plt
import seaborn as sns

# dataset
countries = ["Mexico", "India", "China", "Philippines", "El Salvador", 
             "Vietnam", "Cuba", "Dominican Republic", "Guatemala", "Korea"]
immigrants = [10.7, 2.71, 2.38, 1.96, 1.42, 1.34, 1.28, 1.26, 1.11, 1.01]


plt.figure(figsize=(13, 5), facecolor='white')
ax = sns.barplot(x=immigrants, y=countries, color='#2772A0', width=0.8)


for index, (country, value) in enumerate(zip(countries, immigrants)):
    
    plt.text(-0.3,  
             index, 
             country, 
             ha='right', 
             va='center', 
             fontsize=13,
             color='black', 
             fontweight='light',
             fontfamily='Times New Roman')
    
    # 
    plt.text(0.15,  
             index, 
             f"{value}M", 
             ha='left', 
             va='center', 
             fontsize=13,
             color='white', 
             fontweight='semibold',)


plt.xlim(left=-2.5)  

# Customization
plt.title("Immigrants' top countries of origin in the United States", 
          fontsize=20, color="black", fontweight='light', 
          fontname="Times New Roman", loc="left", pad=20)


ax.set(xticks=[], yticks=[])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)


plt.tight_layout()

# Show plot
plt.show()