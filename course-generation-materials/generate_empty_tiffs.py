from pathlib import Path

n_files = 100

base_path = Path(r"C:\fMRIData\git-repo\data-management-course\example_3\sub2-ses1-microscopydata")

for i in range(n_files):

    filename = f"image_{i}.tiff"

    with open(base_path / filename, "w") as file:
        file.write("")

