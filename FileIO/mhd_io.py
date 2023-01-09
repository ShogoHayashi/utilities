"""
Created on Mon Jan 09 2023

@author: ShogoHayashi
"""

import numpy as np
import os
import SimpleITK as sitk
import skimage.io

# --------------------------------
# mhdファイルを読み込み、保存するまで
# --------------------------------

# mhdファイルからraw imageを取得して保存する方法1(simple ITK)
def get_raw_image_sitk_1(mhd_file):
    itkimage = sitk.ReadImage(mhd_file)
    raw_image = sitk.GetArrayFromImage(itkimage)
    sitk.WriteImage(itkimage, "test.mhd")
   
   
# mhdファイルからraw imageを取得して保存する方法2(simple ITK)
def get_raw_image_sitk_2(mhd_file):
    reader = sitk.ImageFileReader()
    reader.SetFileName(mhd_file)
    raw_image = reader.Execute()
    sitk.WriteImage(raw_image, "test.mhd")  


# mhdファイルからraw imageを取得する方法3(skimage.io)
def get_raw_image_skimage(mhd_file):
    raw_image = skimage.io.imread(mhd_file, plugin='simpleitk')
     

# --------------------------------
# 解像度を求める
# --------------------------------    
    
# 解像度を求める方法1
def get_voxel_spacing_1(mhd_file):
    reader = sitk.ImageFileReader()
    reader.SetFileName(mhd_file)
    reader.ReadImageInformation()
    # 解像度を取得する
    voxel_spacing = reader.GetSpacing()
 
 
# 解像度を求める方法2 
def get_voxel_spacing_2(mhd_file):
    itkimage = sitk.ReadImage(mhd_file)
    # 解像度を取得する
    raw_spacing = itkimage.GetSpacing()

