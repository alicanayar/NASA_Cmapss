import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns



# Import Data Sets
raw_df=pd.read_csv("/Users/msı/Desktop/LIFT-UP/CMAPSSData/train_FD001.txt", sep= " ", header = None )
print(raw_df.isna().sum())

df=pd.read_csv("/Users/msı/Desktop/LIFT-UP/CMAPSSData/train_FD001.txt", sep= " ", header = None )
print(df.isna().sum())

# Drop nan
df.drop (inplace= True, columns=[26,27])

headers = ["Engine", "Time (Cycles)",
           "Setting 1", "Setting 2", "Setting 3",
           "(Fan Inlet Temperature) (◦R)",
           "(LPC Outlet Temperature) (◦R)",
            "(HPC Outlet Temperature) (◦R)",
            "(LPT Outlet Temperature) (◦R)",
            "(Fan Inlet Pressure) (psia)",
            "(Bypass-Duct Pressure) (psia)",
            "(HPC Outlet Pressure) (psia)",
            "(Physical Fan Speed) (rpm)",
            "(Physical Core Speed) (rpm)",
            "(Engine Pressure Ratio(P50/P2)",
            "(HPC Outlet Static Pressure) (psia)",
            "(Ratio of Fuel Flow to Ps30) (pps/psia)",
            "(Corrected Fan Speed) (rpm)",
            "(Corrected Core Speed) (rpm)",
            "(Bypass Ratio) ",
            "(Burner Fuel-Air Ratio)",
            "(Bleed Enthalpy)",
            "(Required Fan Speed)",
            "(Required Fan Conversion Speed)",
            "(High-Pressure Turbines Cool Air Flow)",
            "(Low-Pressure Turbines Cool Air Flow)"]
df.columns = headers

# dataset info
df.info()
df.describe(include="all")
descrtip_df= df.describe()

# general correlation heat map
plt.figure(figsize=(15,15))
dt_cr = df.corr()
sns.heatmap(df.corr(),
            cmap='RdYlBu',
            annot=True,
            linewidths= 0.2,
            linecolor='lightgrey').set_facecolor('white')

# def plot scatter
def plot_scatter(df_name,column_x, column_y, title, label_x, label_y):
    plt.figure(figsize=(10,6))
    plt.plot(df_name[column_x], df_name[column_y])
    plt.title(title)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.grid(True)
    plt.show()


# plot scatter dot version
def plot_scatter_dots(df, x_column, y_column, title, xlabel, ylabel):
     plt.figure(figsize=(10,6))
     plt.scatter(df[x_column], df[y_column])
     plt.title(title)
     plt.xlabel(xlabel)
     plt.ylabel(ylabel)
     plt.grid(True)
     plt.show()   
    
# Constant variable under Setting 3 
plot_scatter(df,"Time (Cycles)", "Setting 3", "Scatterplot of Setting 3 v Time Cycles", "Time (Cycles)", "Setting 3")

# Time cycle of each engine
plot_scatter_dots(df, "Engine","Time (Cycles)" ,"Scatterplot of Time amount of each engines" , "Engines", "Time (Cycles)")

# pivot def
def pivot(df, index_name, column_name, values):
    x=df.pivot(index= index_name, columns= column_name, values= values)
    x.reset_index(inplace=True)
    return x

# LPC Outlet Temperature dataframe (each column represent different engines)
df_pivot = pivot(df, "Time (Cycles)", "Engine", "(LPC Outlet Temperature) (◦R)")
print(df_pivot.isna().sum())

# 1 by 1 correlation 
def indv_corr(df,column_name):
    plt.figure(figsize=(30,30))
    corr_matrix = df.corr()
    target_corr = corr_matrix[column_name]
    sns.heatmap(target_corr.to_frame(),
                cmap='RdYlBu',
                annot=True,
                linewidths= 2,
                linecolor='lightgrey').set_facecolor('white')
    return target_corr


# correlation for each engine under LPC Outlet Temperature
indv_corr(df_pivot, "Time (Cycles)")

# Plot of each engine under LPC Outlet Temperature condition
count = 1
while(count<10):
    plot_scatter(df_pivot, "Time (Cycles)", count , "Scatterplot of Engine "+str(count)+" under LPC Outlet Temperature condition", "Time Cycles", "Engine "+str(count)+"")
    count = count + 1



