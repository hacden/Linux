#-*-coding:utf-8-*-
import xlrd
import sys
import xlsxwriter
 
def extract(inpath, names, outpath, width):
	WorkBook = xlsxwriter.Workbook(outpath)#创建结果xls文件
	WorkSheet = WorkBook.add_worksheet()#创建一个工作表对象
	data = xlrd.open_workbook(inpath, encoding_override='utf-8')#打开目标文件
	table = data.sheets()[0]#选定表
	nrows = table.nrows#获取行号
	ncols = table.ncols#获取列号
	width = int(width)

	names = names.split(',')
	print('===========>文件%s有行%d,列%d'%(inpath,nrows,ncols))
	for i in range(0, nrows):#第0行为表头
		outrow_data =[]
		rowdata = table.row_values(i)#循环拿出excel表中的一行数据
		if i > 0:
			for name in names:#遍历名字
				outrow_data.append(rowdata)
			
		else:
			outrow_data.append(rowdata)
			
		writer(outpath, i, ncols, names, outrow_data, WorkSheet, width)    
	WorkBook.close()
	print('===========>输出文件%s在本目录下-->完成!'%outpath)
def writer(outpath, i, ncols, names, outrow_data, WorkSheet, width):
	if i <= 1:
		row = i
	#2的时候13行开始
	else:
		row = ((i-1) * len(outrow_data))+1
	#写入多少个名字的数据[[1,1,1],[2,2,2,]]
	for n in range(len(outrow_data)):	
		#写入一行完整数据
		for col in range(len(outrow_data[n])):	
			WorkSheet.set_column('A:Z',width)#设置单元格宽度
			WorkSheet.write(row,col,outrow_data[n][col])# 按一行中的列写入数据
			if i > 0:
				nm = names[n].decode('utf-8')#一定要注意类型转换，excel只支持Unicode编码插入
				WorkSheet.write(row,ncols,nm)
		row+=1

		
	
if __name__ == '__main__':
	try:
		inpath = sys.argv[1]
		names = sys.argv[2]
		outpath = sys.argv[3]
		width = sys.argv[4]
		extract(inpath, names, outpath, width)
	except Exception,e:
		print('Usage: xx.py /data/xlsfile.xls 张三,李四,王五 result.xlsx 20')
	
	

