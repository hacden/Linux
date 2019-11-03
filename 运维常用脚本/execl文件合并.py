#-*- coding:utf-8 -*-

import xlrd
import os
import xlwt
import sys
from xlutils.copy import copy

"""
将文件夹下所有excel文件合并成一个文件
注意：
    本代码仅支持合并excel文件第一个sheet，如果合并的excel文件有多个sheet，只会读取和合并第一个sheet,
思路：
    1.获取路径下所有文件
    2.新建一个excel文件，用于存储全部数据
    3.逐个打开需要合并的excel文件，逐行读取数据，再用一个列表来保存每行数据。最后该列表中会存储所有的数据
    4.向excel文件中逐行写入
"""


def get_allfile_msg(file_dir):
    for root, dirs, files in os.walk(file_dir):
        '''
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件 
        '''
        return root, dirs, [file for file in files if file.endswith('.xls') or file.endswith('.xlsx')]


def get_allfile_url(root, files):
    """
    将目录的路径加上'/'和文件名，组成文件的路径
    :root: 路径
    :files: 文件名称集合
    :return: none
    """
    allFile_url = []
    for file_name in files:
        file_url = root + '/' + file_name
        allFile_url.append(file_url)
    return allFile_url


def all_to_one(root, allFile_url, output_file, kuangdu, have_title=True):
    """
    合并文件
    :root: 输出文件的路径
    :allFile_url: 保存了所有excel文件路径的集合
    :file_name: 输出文件的文件名
    :title: excel表格的表头
    :have_title: 是否存在title(bool类型),默认为true，不读取excel文件的第0行
    :return: none
    """
    # 首先在该目录下创建一个excel文件,用于存储所有excel文件的数据
    output_file = root + '/' + output_file
    create_excel(output_file)

    list_row_data = []
    for f in allFile_url:
        # 打开excel文件
        print('打开%s文件' % f)
        excel = xlrd.open_workbook(f)
        # 根据索引获取sheet，这里是获取第一个sheet
        table = excel.sheet_by_index(0)
        print('该文件行数为：%d，列数为：%d' % (table.nrows, table.ncols))

        # 获取excel文件所有的行
        for i in range(table.nrows):
            # 如果存在表头，则跳过第0行，否则不跳过
            if have_title and i == 0:
                continue
            else:
                row = table.row_values(i)  # 获取整行的值，返回列表
                list_row_data.append(row)
    if have_title:
        print('==========================================')
        print('-------->减去%d个文件的%d个表头剩余总数据量%d' % (len(allFile_url),len(allFile_url),len(list_row_data)))
    else:
        print('总数据量为%d' % len(list_row_data))
    # 写入all文件
    add_row(list_row_data, output_file, kuangdu)


# 创建文件名为output_file,表头为title的excel文件
def create_excel(output_file):
    print('==========创建文件%s==========' % output_file)
    a = xlwt.Workbook()
    # 新建一个sheet
    table = a.add_sheet('sheet1')
    a.save(output_file)


# 向文件中添加n行数据
def add_row(list_row_data, output_file, kuangdu):
    # 打开excel文件
    allExcel1 = xlrd.open_workbook(output_file)
    sheet = allExcel1.sheet_by_index(0)
    # copy一份文件,准备向它添加内容
    allExcel2 = copy(allExcel1)
    sheet2 = allExcel2.get_sheet(0)
    
    # 写入数据
    i = 1
    for row_data in list_row_data:
        for j in range(len(row_data)):
            sheet2.write(sheet.nrows + i, j, row_data[j])
            #设置列的宽度
            if i == 1:
               sheet2.col(int(j)).width = kuangdu
               if int(j+1) ==  len(row_data):
                    print('-------->已设置%d列的宽度为%d'%(len(row_data),kuangdu))
					
        i += 1
    # 保存文件，将原文件覆盖
    allExcel2.save(output_file)
    print('-------->合并完成')


if __name__ == '__main__':
	try:
		# 设置文件夹路径，
		file_dir = sys.argv[1] 
		# 设置文件名，用于保存数据
		output_file = sys.argv[2]
		#设置宽度
		kuangdu = int(sys.argv[3])
		# 获取文件夹的路径,该路径下的所有文件夹，以及所有文件
		root, dirs, files = get_allfile_msg(file_dir)
		# 拼凑目录路径+文件名,组成文件的路径,用一个列表存储
		allFile_url = get_allfile_url(root, files)
		# have_title参数默认为True,为True时不读取excel文件的首行
		all_to_one(root, allFile_url, output_file, kuangdu, have_title=True)
	except Exception,e:
		print('Usage: xx.py dirname filename width')
		sys.exit()
