# What are good data management practices guide

project
  rawdata  
    sub-001  
      ses-01  
        ephys
          sub-001_ses-01_run-01_task-discrim.bin
          sub-001_ses-01_run-02_task-discrim.bin
          sub-001_ses-01_run-03_task-discrim.bin
        behav
          sub-001_ses-01_run-01_task-discrim.mp4
          sub-001_ses-01_run-02_task-discrim.mp4
          sub-001_ses-01_run-03_task-discrim.mp4
    README.md

# Example 3
sub-001
  ses-001
    behav
      sub-001_ses-001_type-positions.csv
      sub-001_ses-001_type-video.mp4
  ses-002  
    ephys 
      sub-001-ses-002_g0
        sub-001-ses-002_g0_imec0
          sub-001_ses-002_g0_t0.imec0.ap.bin
          sub-01_ses-002_g0_t0.imec0.ap.meta
          
sub-002
  ses-001
    micr
      sub-001_ses-001_format-tiff
        image1.tiff
        image2.tiff
        ...
		
		
for https://tree.nathanfriend.io