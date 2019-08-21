#テキストの集合から単語（名詞）のリストの集合を作成
class Database:
    def database():
        from preprocess import Preprocess,API_download
        import glob

        #docsにテキストの集合が、id2docにテキスト名が入る
        docs=[]
        id2doc=[]
        pathlist=glob.glob("../data/comparison_data/*")

        for path in pathlist:
            f = open(path)
            text=f.read()
            f.close()
            docs.append(text)
            id2doc.append(path)
        print(id2doc)


        #docsには文章のリストが入っている
        tagger=API_download.mecab_download()
        word_lists=[]
        for doc in docs:
            text=Preprocess.cleaning_text(doc)
            word_class=Preprocess.mecab_list(text,tagger)
            noun_list=Preprocess.noun_extract(word_class)
            noun_list2=Preprocess.noun_squeeze(noun_list)
            word_lists.append(noun_list2)
        return word_lists,id2doc