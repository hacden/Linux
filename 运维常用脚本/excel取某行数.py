#-*-coding:utf-8-*-
import xlrd
import sys
import xlsxwriter
 
def extract(inpath, columns, outpath, width):
    WorkBook = xlsxwriter.Workbook(outpath)#创建结果xls文件
    WorkSheet = WorkBook.add_worksheet()#创建一个工作表对象
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')#打开目标文件
    table = data.sheets()[0]#选定表
    nrows = table.nrows#获取行号
    ncols = table.ncols#获取列号
    width = int(width)
    columns = columns.split(',')
	
    print('===========>文件%s有行%d,列%d'%(inpath,nrows,ncols))
    print('===========>选择的是%s这几列'%columns)
    for i in range(0, nrows):#第0行为表头
		outrow_data =[]
		rowdata = table.row_values(i)#循环输出excel表中一行数据
		for q in columns:#定义输出第几列
			q = int(q)-1
			result = rowdata[q]#取出行中某列数据
			outrow_data.append(result) 
		writer(outpath, ncols, outrow_data, i, WorkSheet, width)    
    WorkBook.close()
    print('===========>输出文件%s在本目录下-->完成!'%outpath)
def writer(outpath, ncols, outrow_data, i, WorkSheet, width):
	for n in range(len(outrow_data)):
		WorkSheet.set_column('A:Z',width)#设置单元格宽度
		WorkSheet.write(i,n,outrow_data[n])# 写入数据
	
	
	
if __name__ == '__main__':
	try:
		inpath = sys.argv[1]
		columns = sys.argv[2]
		outpath = sys.argv[3]
		width = sys.argv[4]
		extract(inpath, columns, outpath, width)
	except Exception,e:
		print('Usage: xx.py /data/xlsfile.xls 1,3,5 result.xlsx width')
	
	

