class Univariate():
    def quanQual(dataset):
            quan=[]
            qual=[]
            for columnName in dataset.columns:
                #print(columnName)
                if(dataset[columnName].dtype=='O'):
                    #print("quan")
                    qual.append(columnName)
                else:
                    #print("qual")
                    quan.append(columnName)
            return quan,qual