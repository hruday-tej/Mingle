import uuid

def get_randome_code(str1):
	code = str(uuid.uuid5(uuid.NAMESPACE_URL,str1))[:8].replace('-','').lower()
	return code