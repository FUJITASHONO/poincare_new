from gensim.models.poincare import PoincareModel,PoincareRelations
relations = PoincareRelations(file_path="../data/word_relation.csv", delimiter=',')
model = PoincareModel(relations, negative=10,size=5)
model.train(epochs=50)