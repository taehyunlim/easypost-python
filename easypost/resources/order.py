class Order(AllResource, CreateResource):
    def get_rates(self):
        requestor = Requestor(self.api_key)
        url = '%s/%s' % (self.instance_url(), 'rates')
        response, api_key = requestor.request('get', url)
        self.refresh_from(response, api_key)
        return self

    def buy(self, **params):
        requestor = Requestor(self.api_key)
        url = '%s/%s' % (self.instance_url(), 'buy')
        response, api_key = requestor.request('post', url, params)
        self.refresh_from(response, api_key)
        return self
