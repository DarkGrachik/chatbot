import os

# Путь для статичных файлов
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Путь к папке со статичными файлами
]

# Путь для сохранения скомпилированных статичных файлов
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL для доступа к статичным файлам
STATIC_URL = '/static/'
