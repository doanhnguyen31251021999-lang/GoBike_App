import json

# Read the notebook
with open('Ai_Go_Bike.ipynb', 'r') as f:
    nb = json.load(f)

# Remove problematic metadata
if 'metadata' in nb and 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']
    print("✓ Removed problematic 'widgets' metadata")

# Save the fixed notebook
with open('Ai_Go_Bike.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
    print("✓ Notebook fixed and saved successfully!")