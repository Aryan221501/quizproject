import time
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Skip rate limiting for admin and static files
        if request.path.startswith('/admin/') or request.path.startswith('/static/'):
            return None
            
        # Get client IP
        ip = self.get_client_ip(request)
        
        # Create a cache key based on IP and current minute
        cache_key = f"rate_limit_{ip}_{int(time.time() / 60)}"
        
        # Get current count from cache
        count = cache.get(cache_key, 0)
        
        # If count exceeds limit, block the request
        if count >= 100:  # 100 requests per minute
            return JsonResponse({
                'error': 'Rate limit exceeded. Please try again later.'
            }, status=429)
            
        # Increment count and set expiration to 1 minute
        cache.set(cache_key, count + 1, 60)
        
        return None
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip