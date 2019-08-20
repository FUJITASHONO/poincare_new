#poincare空間の距離の最小アライメントを計算
def poincare_distance(list1,list2,model):
	distance_total=0
	word_number=0
	for wa in list1:
		distance_list=[]
		ka=0
		for wb in list2:
			try:
				distance_list.append(abs(model.kv.difference_in_hierarchy(wa,wb)))
				ka=1
			except Exception as e:
				pass
		if not ka==0:
			word_number+=1
			distance_min=min(distance_list)
			distance_total+=distance_min
	return distance_total/word_number
#最小アライメントの平均を計算		
def minimum_alignment(list1,list2,model):
	a1=poincare_distance(list1,list2,model)
	a2=poincare_distance(list2,list1,model)
	return (a1+a2)/2

#最小アライメントが最も低い文章のインデックスを算出
class Most_similarity:
	def most_similarity(nounlist,database,model):
		import numpy as np
		lista=["医療","化学","経済","情報","心理","電気","土木","動物","法","歴史"]
		similarity=[]
		for i,data in enumerate(database):
			si=minimum_alignment(nounlist,data,model)
			similarity.append(si)
			print(lista[i])
			print(si)
		return np.argmin(similarity)