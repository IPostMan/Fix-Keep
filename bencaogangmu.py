# -- coding: UTF-8

import ffmpeg
import numpy
import os
from PIL import Image
import time

def getImage(video_path, image_path):
	img_count = 1
	crop_time = 0.1
	while crop_time <= 90.0:#转化15s的视频
		os.system(' ffmpeg -i %s -f image2 -ss %s -vframes 1 %s.png '% (video_path, str(crop_time), image_path + str(img_count)))
		img_count += 1
		print( 'Geting Image ' + str(img_count) + '.png' + ' from time ' + str(crop_time))
		crop_time += 0.1 #每0.1秒截取—张照片
		print('视频转化完成!!!')


def image_to_txt(image_path, txt_path):
	#这里使用到PIL库convert函数,将RGB图片转化为灰度图,参数'L'代表转化为灰度图
	im = Image.open(image_path).convert( 'L')
	charwidth = 100
	# 这个是设置你后面在cmd里面显示内容的窗口大小,请根据自己的情况,适当调整值
	im = im.resize((charwidth, charwidth // 2))
	target_width, target_height = im.size
	data = numpy.array(im)[ :target_height, :target_width]
	f = open(txt_path, 'w', encoding='utf-8')
	#num = 0
	for row in data:
		#num = num + 1
		#if num == 4 :
			#f.write('*****************************帮助乌干达儿童******************************************')
			#continue
		for pixel in row :
			if pixel > 127:#如果灰度值大于127,也就是偏白的,就写一个字符'*'
				f.write('*')
			else:
				f.write('B')
		f.write( ' \n ')
	f.close()

def getTxt(image_path,txt_path):#调用上面的函数image_to_txt
	img_count = 1#—张图对应一个txt文件,所以每遍历—张图,该值加—
	while img_count <= len(os.listdir(image_path)):
		#os.listdir(image_path)#返回所有图片名称,是个字符串列表
		imageFile = image_path+ str(img_count) + '.png'
		txtFile = txt_path+ str(img_count) + '.txt'
		image_to_txt( imageFile,txtFile)
		print('舞蹈加载中:' + str(img_count) +'%')
		img_count += 1
        
def run(txtPath):
	time.sleep(1)
	txt_count = 1
	while txt_count <= len(os.listdir(txtPath)):
		time.sleep(0.1)
		os.system( 'type ' + txtPath + str(txt_count) + '.txt')
		#这里type命令是windows下的命令,type+文件名,就可以在cmd里面显示文件内容
		txt_count += 1
		#time.sleep(1)

if __name__ == '__main__':
	video_dir_path = r'D:\personal\code\Fix-Keep\image\本草纲目.mp4' #存储视频文件的路径
	txt_dir_path = r'D:\personal\code\Fix-Keep\image\png' + '\\' #存储txt文件的路径
	img_dir_path = r'D:\personal\code\Fix-Keep\image\txt' + '\\' #存储图片的路径
	getImage(video_dir_path, img_dir_path )
	getTxt(img_dir_path,txt_dir_path)
	run(txt_dir_path)
