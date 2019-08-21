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
#poincare空間の距離の平均アライメントを計算
def poincare_distance2(list1,list2,model):
	distance_total=0
	wa_number=0
	for wa in list1:
		wb_number=0
		distance=0
		for wb in list2:
			try:
				distance+=abs(model.kv.difference_in_hierarchy(wa,wb))
				wb_number+=1
			except Exception as e:
				pass
		if not wb_number==0:
			wa_number+=1
			distance=distance/wb_number
			distance_total+=distance
	return distance_total/wa_number

#アライメントの平均を計算		
def minimum_alignment(list1,list2,model):
	a1=poincare_distance(list1,list2,model)
	a2=poincare_distance(list2,list1,model)
	return (a1+a2)/2

#最小アライメントがしきい値より低い文章のインデックスを昇順で返す
class Most_similarity:
	def most_similarity(nounlist,database,model,border):
		import numpy as np
		similarity=[]
		a=0
		for data in database:
			a+=1
			si=minimum_alignment(nounlist,data,model)
			similarity.append(si)
			print(a)
			print(si)

		similarity=np.asarray(similarity)
		rank=similarity.argsort()
		ind=[]
		for r in rank:
			if similarity[int(r)]<border:
				ind.append(r)
		return ind