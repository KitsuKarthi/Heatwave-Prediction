#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install netcdf2csv


# In[ ]:


from netcdf2csv import convert_dir

#net_cdf_dir = Directory containing all netcdf (.nc) files

#csv_dir = Directory to output all csv files(uncleaned- containing null values)

#cleaned_csv_dir = Directory to output cleaned csv files (does not containing null values) (Optional)

#clean_choice = (0 -> if you don't need cleaned csv, 1 -> if you want cleaned csv output)

convert_dir(netcdf_dir,csv_dir,cleaned_csv_dir='./',clean_choice=0)

