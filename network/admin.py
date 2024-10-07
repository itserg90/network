from django.contrib import admin

from network.models import Plant, Network, Entrepreneur, Product


@admin.action(description="Обнулить долг")
def debt_reset(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'address']
    list_filter = ['country']
    actions = [debt_reset]


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'country', 'city', 'address', 'debt', 'product']
    list_filter = ['city']
    actions = [debt_reset]


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'country', 'city', 'address', 'debt', 'product']
    list_filter = ['city']
    actions = [debt_reset]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'model', 'release_date', 'created_at', 'plant']
