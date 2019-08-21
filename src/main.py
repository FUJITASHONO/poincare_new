border=

#train.pyで学習したモデルのダウンロード
#from train import train
#model=Train.train()
#保存したいとき
#model.save("name.gz")

#フォルダからpoincareモデル(epoch=100)のダウンロード
from gensim.models.poincare import PoincareModel,PoincareRelations
model=PoincareModel.load("../data/poincare_1.gz")


#比較する文章のデータベースの作成
from database import Database
database,id2doc=Database.database()

#対象の文章の読み込み
import glob
path=glob.glob("../data/target_data/*")
path=path[0]
f = open(path)
text=f.read()
f.close()

#入力（対象の文章、判別モデル、文章のデータベース、しきい値）から出力（類似度がしきい値以下の似てる文章を昇順で）を出す
from comparison import Comparison
ind=Comparison.comparison(text,database,model,border)
for i in ind:
	print(id2doc[i])