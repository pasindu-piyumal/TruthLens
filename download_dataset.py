from datasets import load_dataset
import pandas as pd

dataset = load_dataset("davanstrien/WELFake")

print("Available splits:", list(dataset.keys()))

df = dataset['train'].to_pandas()

print('\nDataset shape', df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst five rows:")
print(df.head())

df.to_csv("WELFake.csv", index=False)