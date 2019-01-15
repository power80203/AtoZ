from sklearn.preprocessing import StandardScaler


class DataEnginnering:
    def __init__(self):
        pass
    
    #標準化功能
    @classmethod
    def dataScaler(cls,X):
        sc = StandardScaler()
        X = sc.fit_transform(X)
        return X

    #隨機樣本功能
    @classmethod
    def dataSplite(testize=0.25, trainsize=0.75):
        pass

    #DealingMissingData

    #OneHotEncoding

    #LabelEncoding




        
        