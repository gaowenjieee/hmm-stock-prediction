from hmmlearn.hmm import GaussianHMM
import logging
 
class StockPredictor(object):
    def __init__(self, company, n_latency_days=10, n_hidden_states=4):
        self._init_logger()
 
        self.company = company
        self.n_latency_days = n_latency_days
 
        self.hmm = GaussianHMM(n_components=n_hidden_states)
 
        self.data = pd.read_csv(
            'data/company_data/{company}.csv'.format(company=self.company))
 
    def fit(self):
        self._logger.info('&gt;&gt;&gt; Extracting Features')
        feature_vector = StockPredictor._extract_features(self.data)
        self._logger.info('Features extraction Completed &lt;&lt;&lt;')
 
        self.hmm.fit(feature_vector)

# Predictor for GOOGL stocks
stock_predictor = StockPredictor(company='GOOGL')
