import hashlib
from django.core.cache import cache

def get_result(key):
	if key:
		hash = hashlib.md5(key).hexdigest()

		result = cache.get(hash)
		if result:
			return result
		else:
			return False

def set_result(key, result):
	if key:
		hash = hashlib.md5(key).hexdigest()
		cache.set(hash, result)

def delete_result(key):
	if key:
		hash = hashlib.md5(key).hexdigest()
		cache.delete(hash)