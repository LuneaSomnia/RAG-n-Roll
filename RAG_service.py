from snowflake.connector import connect
from cortex_search import CortexSearch

class RAGService:
    def __init__(self):
        self.cortex_search = CortexSearch()
        self.snowflake = connect(
            user='your_user',
            password='your_password',
            account='your_account'
        )
    
    def search_resources(self, query, category):
        results = self.cortex_search.search(query)
        return self.process_results(results, category)
