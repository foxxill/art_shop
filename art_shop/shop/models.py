from django.db import models

# создание моделей в базе данных сайта

# модель для категорий продуктов
class Category(models.Model):
    # создание поля под имя категории
    name = models.CharField(max_length = 200, db_index = True)
    # создание поля под ссылку на категорию
    slug = models.SlugField(max_length = 200, db_index = True, unique = True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Каткгория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name

# модель для подкатегорий продуктов
class Subcategory(models.Model):
    # описание отношения многое к одному (подкатегории -> категория)
    category = models.ForeignKey(Category, related_name = 'subcategory', on_delete = models.CASCADE)
    # создание поля под имя подкатегории
    name = models.CharField(max_length = 200, db_index = True)
    # создание поля под ссылку на подкатегорию
    slug = models.SlugField(max_length = 200, db_index = True, unique = True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        
    def __str__(self):
        return self.name

# модель для продуктов
class Product(models.Model):
    # описание отношения многое к одному (продукты -> подкатегория)
    subcategory = models.ForeignKey(Subcategory, related_name = 'product', on_delete = models.CASCADE)
    # создание поля под имя продукта
    name = models.CharField(max_length = 200, db_index = True)
    # создание поля для URL продукта
    slug = models.SlugField(max_length = 200, db_index = True, unique = True)
    # создание поля для фото продукта
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank = True)
    # создание поля для описания продукта
    description = models.TextField(blank = True)
    # создание поля для указания цены
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    # создание поля для указания наличия продукта
    availabel = models.BooleanField(default = True)
    # создание поля с датой добавления продукта
    created = models.DateTimeField(auto_now_add = True)
    # создание поля с обновленной датой при изменении поля
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name
    
    
        
