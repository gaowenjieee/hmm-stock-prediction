from sklearn.model_selection import train_test_split
import logging 
 
class StockPredictor(object):
    def __init__(self, company, test_size=0.33,
                 n_latency_days=10, n_hidden_states=4):
        self._init_logger()
 
        self.company = company
        self.n_latency_days = n_latency_days
 
        self.hmm = GaussianHMM(n_components=n_hidden_states)
 
        self._split_train_test_data(test_size)
 
    def _split_train_test_data(self, test_size):
        data = pd.read_csv(
            'data/company_data/{company}.csv'.format(company=self.company))
        _train_data, test_data = train_test_split(
            data, test_size=test_size, shuffle=False)
 
        self._train_data = _train_data
        self._test_data = test_data
 
    def fit(self):
        self._logger.info('&gt;&gt;&gt; Extracting Features')
        feature_vector = StockPredictor._extract_features(self._train_data)
        self._logger.info('Features extraction Completed &lt;&lt;&lt;')

	self.hmm.fit(feature_vector)


