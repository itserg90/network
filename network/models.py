from django.db import models

NULLABLE = {"blank": True, "null": True}


class Plant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Укажите название завода")
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту")
    country = models.CharField(max_length=100, verbose_name="Страна", help_text="Укажите страну")
    city = models.CharField(max_length=100, verbose_name="Город", help_text="Укажите город")
    address = models.CharField(max_length=200, verbose_name="Адрес", help_text="Укажите улицу и номер дома")

    def __str__(self):
        return f"Завод {self.name}."

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class Product(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name='Завод', help_text='Укажите завод')
    name = models.CharField(max_length=200, verbose_name='Название продукта', help_text='Укажите название')
    model = models.CharField(max_length=200, verbose_name='Модель', help_text='Укажите модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок', help_text='Укажите дату выхода на рынок')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Network(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name='Завод')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Розничная сеть: {self.name}.'

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Entrepreneur(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name='Завод')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'ИП: {self.name}.'

    class Meta:
        verbose_name = "Предприниматель"
        verbose_name_plural = "Предприниматели"
