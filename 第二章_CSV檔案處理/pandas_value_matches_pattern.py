# -*- coding: utf-8 -*-
#!usr/bin/env python3
#(pandas)篩選特定資料列，並輸出至csv - 找尋符合特定文字組合(例如發票為001-開頭，並且是Supplier Y)
"""
Created on Wed Sep 20 14:54:34 2017

@author: vizance
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file, index=False)
