class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time  Bother Initialization")
        
    def __call__(self, request):
        print("This is Bother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return response
    
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Father Initialization")
        
    def __call__(self, request):
        print("This is Father before view")
        response = self.get_response(request)
        print("This is Father after view")
        return response
    
class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mother Initialization")
        
    def __call__(self, request):
        print("This is Mother before view")
        response = self.get_response(request)
        print("This is Mother after view")
        return response