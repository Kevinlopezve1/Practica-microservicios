import redis
# Configura Redis
cache = redis.Redis(host='localhost', port=6379, db=0)
# Guarda un valor en la caché
cache.set('usuario1', 'Ana Garcia', ex=60)  # Expira en 60 segundos
# Recupera un valor de la caché
usuario = cache.get('usuario1')
if usuario:
    print(f"Usuario en caché: {usuario.decode('utf-8')}")
else:
    print("Usuario no encontrado en caché.")