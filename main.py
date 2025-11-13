###################################################################################################################
# filter()
# Vazifasi: Berilgan shartlarga mos keladigan yozuvlarni qaytaradi.

# # Mahsulotlarni kategoriya bo'yicha filtrlash
# products = Product.objects.filter(category_id=1)

# # Bir nechta shartlar bilan (AND mantiq)
# products = Product.objects.filter(
#     category_id=1,
#     unit_price__gte=100
# )
###################################################################################################################


###################################################################################################################
# exclude()
# Vazifasi: Berilgan shartlarga mos kelmaydigan yozuvlarni qaytaradi.

# # To'xtatilmagan mahsulotlar
# active_products = Product.objects.exclude(discontinued=True)

# # filter bilan birgalikda
# cheap_available = Product.objects.filter(
#     unit_price__lt=20
# ).exclude(
#     category__category_name='Beverages'
# )
###################################################################################################################


###################################################################################################################
# annotate()
# Vazifasi: Har bir obyektga qo'shimcha hisoblangan maydon qo'shadi va natijada SELECT da ko'rinadi.

# from django.db.models import Count, Sum, Avg
#
# # Har bir kategoriyada nechta mahsulot borligini hisoblash
# categories = Category.objects.annotate(
#     product_count=Count('product')
# )
# for cat in categories:
#     print(f"{cat.category_name}: {cat.product_count} mahsulot")
###################################################################################################################


###################################################################################################################
# alias()
# Vazifasi: Hisoblangan maydon yaratadi, lekin SELECT da ko'rinmaydi. Faqat filter qilish uchun.

# # alias() - faqat filtrlash uchun
# categories = Category.objects.alias(
#     product_count=Count('product')
# ).filter(product_count__gt=5)

# # ANNOTATE - natijada ko'rinadi
# queryset = Category.objects.annotate(cnt=Count('product'))
# print(queryset.values())  # {'id': 1, 'name': 'Beverages', 'cnt': 12}
#
# # ALIAS - natijada ko'rinmaydi
# queryset = Category.objects.alias(cnt=Count('product'))
# print(queryset.values())  # {'id': 1, 'name': 'Beverages'}  # cnt yo'q!
###################################################################################################################


###################################################################################################################
# order_by()
# Vazifasi: Natijalarni tartiblaydi.

# # O'sish tartibida
# products = Product.objects.order_by('unit_price')
#
# # Kamayish tartibida
# products = Product.objects.order_by('-unit_price')
#
# # Bir nechta maydonlar bo'yicha
# products = Product.objects.order_by('category_id', '-unit_price')
###################################################################################################################


###################################################################################################################
# reverse()
# Vazifasi: Mavjud tartibni teskari aylantiradi.

# # Avval o'sish tartibida
# products = Product.objects.order_by('unit_price')
# # Keyin kamayish tartibida
# products_reversed = products.reverse()
#
# # Bu ikkalasi bir xil
# products = Product.objects.order_by('-unit_price')
# products = Product.objects.order_by('unit_price').reverse()
###################################################################################################################


###################################################################################################################
# distinct()
# Vazifasi: Takrorlanuvchi yozuvlarni olib tashlaydi.

# # Unique shaharlar
# cities = Customer.objects.values('city').distinct()
###################################################################################################################


###################################################################################################################
# values()
# Vazifasi: QuerySet o'rniga dictionary qaytaradi.

# # Barcha maydonlar
# products = Product.objects.values()
# # [{'product_id': 1, 'product_name': 'Chai', 'unit_price': 18.00, ...}]
#
# # Faqat kerakli maydonlar
# products = Product.objects.values('product_name', 'unit_price')
# # [{'product_name': 'Chai', 'unit_price': 18.00}]
###################################################################################################################


###################################################################################################################
# values_list()
# Vazifasi: Tuple qaytaradi, dictionary emas.

# # Tuple ko'rinishida
# products = Product.objects.values_list('product_name', 'unit_price')
# # [('Chai', 18.00), ('Chang', 19.00), ...]

# # FARQ:
# # values() - dict
# Product.objects.values('product_name', 'unit_price')
# # [{'product_name': 'Chai', 'unit_price': 18.00}]
#
# # values_list() - tuple
# Product.objects.values_list('product_name', 'unit_price')
# # [('Chai', 18.00)]
###################################################################################################################


###################################################################################################################
# dates()
# Vazifasi: Date maydon bo'yicha unique sanalar ro'yxatini qaytaradi.

# # Buyurtmalar berilgan sanalar (yil-oy-kun)
# order_dates = Order.objects.dates('order_date', 'day')
# # [datetime.date(1996, 7, 4), datetime.date(1996, 7, 5), ...]
#
# # Faqat yillar
# years = Order.objects.dates('order_date', 'year')
# # [datetime.date(1996, 1, 1), datetime.date(1997, 1, 1), ...]
#
# # Faqat oylar
# months = Order.objects.dates('order_date', 'month')
# # [datetime.date(1996, 7, 1), datetime.date(1996, 8, 1), ...]
###################################################################################################################


###################################################################################################################
# datetimes()
# Vazifasi: DateTime maydon bo'yicha unique vaqtlar ro'yxatini qaytaradi.

# # Xodimlar ishga qabul qilingan vaqtlar (soat aniqligida)
# hire_times = Employee.objects.datetimes('hire_date', 'hour')
#
# # Yil aniqligida
# hire_years = Employee.objects.datetimes('hire_date', 'year')
#
# # Kun aniqligida
# hire_days = Employee.objects.datetimes('hire_date', 'day')
#
# # Minut aniqligida
# precise_times = Order.objects.datetimes('order_date', 'minute')
###################################################################################################################


###################################################################################################################
# none()
# Vazifasi: Bo'sh QuerySet qaytaradi.

# # Bo'sh natija
# products = Product.objects.none()
# # []
###################################################################################################################


###################################################################################################################
# all()
# Vazifasi: Barcha yozuvlarni qaytaradi.

# # Barcha mahsulotlar
# products = Product.objects.all()
###################################################################################################################


###################################################################################################################
# union()
# Vazifasi: Ikki QuerySet ni birlashtiradi (SQL UNION)

# # Arzon va qimmat mahsulotlarni birlashtirish
# cheap = Product.objects.filter(unit_price__lt=10)
# expensive = Product.objects.filter(unit_price__gt=100)
# combined = cheap.union(expensive)
###################################################################################################################


###################################################################################################################
# intersection()
# Vazifasi: Ikkala QuerySet da ham bo'lgan yozuvlarni qaytaradi.

# # O'rta narxdagi mahsulotlar
# not_cheap = Product.objects.exclude(unit_price__lt=10)
# not_expensive = Product.objects.exclude(unit_price__gt=100)
# medium_priced = not_cheap.intersection(not_expensive)
###################################################################################################################


###################################################################################################################
# difference()
# Vazifasi: Birinchi QuerySet da bor, ikkinchisida yo'q yozuvlarni qaytaradi.

# # Barcha mahsulotlar - tugagan mahsulotlar
# all_products = Product.objects.all()
# discontinued = Product.objects.filter(discontinued=True)
# active = all_products.difference(discontinued)
###################################################################################################################


###################################################################################################################
# select_related()
# Vazifasi: ForeignKey va OneToOne uchun SQL JOIN ishlatadi. Bitta SQL so'rov.

# # N+1 muammo (Yomon)
# products = Product.objects.all()
# for product in products:  # 1 so'rov
#     print(product.category.category_name)  # Har biri uchun +1 so'rov
#
# # Yechim: select_related (Yaxshi)
# products = Product.objects.select_related('category')  # 1 so'rov (JOIN)
# for product in products:
#     print(product.category.category_name)  # DB ga so'rov yo'q
###################################################################################################################


###################################################################################################################
# prefetch_related()
# Vazifasi: ManyToMany va reverse ForeignKey uchun. Alohida SQL so'rovlar.

# # N+1 muammo (Yomon)
# orders = Order.objects.all()
# for order in orders:  # 1 so'rov
#     print(order.orderdetail_set.all())  # Har biri uchun +1 so'rov
#
# # Yechim: prefetch_related (Yaxshi)
# orders = Order.objects.prefetch_related('orderdetail_set')  # 2 so'rov
# for order in orders:
#     print(order.orderdetail_set.all())  # DB ga so'rov yo'q
###################################################################################################################


###################################################################################################################
# extra()
# Vazifasi: Qo'shimcha SQL kodini qo'shish (eskicha, tavsiya etilmaydi).

# # SELECT qismiga qo'shimcha
# products = Product.objects.extra(
#     select={
#         'total_value': 'unit_price * units_in_stock'
#     }
# )

# # Alternative
# from django.db.models import F
#
# # extra() o'rniga F() expressions
# products = Product.objects.annotate(
#     total_value=F('unit_price') * F('units_in_stock')
# )
###################################################################################################################


###################################################################################################################
# defer()
# Vazifasi: Berilgan maydonlarni keyinga qoldiradi (lazy load).

# # description maydonini keyinga qoldirish
# categories = Category.objects.defer('description')
# # SELECT id, category_name FROM categories

# # Keyinchalik murojaat qilsa, alohida so'rov ketadi
# category = Category.objects.defer('description').first()
# print(category.description)  # Endi description uchun so'rov ketadi
###################################################################################################################


###################################################################################################################
# only()
# Vazifasi: Faqat berilgan maydonlarni oladi.

# # Faqat kerakli maydonlar
# products = Product.objects.only('product_name', 'unit_price')
# # SELECT product_id, product_name, unit_price FROM products
###################################################################################################################


###################################################################################################################
# using()
# Vazifasi: Qaysi database dan foydalanishni belgilaydi (multi-DB).

# # settings.py da
# DATABASES = {
#     'default': {...},
#     'database2': {...}
# }

# # Read replica dan o'qish
# products = Product.objects.using('database2').all()
###################################################################################################################


###################################################################################################################
# select_for_update()
# Vazifasi: Row-level locking (transaction ichida).

# from django.db import transaction
#
# # Lock qo'yish
# with transaction.atomic():
#     product = Product.objects.select_for_update().get(pk=1)
#     product.units_in_stock -= 1
#     product.save()
# # Boshqa foydalanuvchilar kutadi
###################################################################################################################


###################################################################################################################
# raw()
# Vazifasi: To'g'ridan-to'g'ri SQL so'rovini bajarish.

# # Oddiy raw SQL
# products = Product.objects.raw('SELECT * FROM products WHERE unit_price > 50')
###################################################################################################################


###################################################################################################################
# & (AND)
# Vazifasi: Ikki shartni ham qanoatlantirish kerak.

# from django.db.models import Q
#
# # Oddiy AND
# products = Product.objects.filter(
#     unit_price__gte=20,
#     units_in_stock__gt=0
# )
#
# # Q obyektlar bilan
# products = Product.objects.filter(
#     Q(unit_price__gte=20) & Q(units_in_stock__gt=0)
# )
###################################################################################################################


###################################################################################################################
# | (OR)
# Vazifasi: Kamida bitta shart qanoatlantirilishi kerak.

# # OR mantiq
# products = Product.objects.filter(
#     Q(unit_price__lt=10) | Q(unit_price__gt=100)
# )
###################################################################################################################


###################################################################################################################
# ^ (XOR)
# Vazifasi: Faqat bitta shart qanoatlantirilishi kerak (ikkalasi ham emas).

# # XOR mantiq
# products = Product.objects.filter(
#     Q(unit_price__lt=10) ^ Q(units_in_stock=0)
# )
# # unit_price < 10 YO units_in_stock = 0 (lekin ikkalasi ham emas)
###################################################################################################################


###################################################################################################################
# get()
# Vazifasi: Bitta obyektni olish. Ko'p bo'lsa yoki yo'q bo'lsa xatolik.

# product = Product.objects.get(product_id=1)  # bir xil
###################################################################################################################


###################################################################################################################
# create()
# Vazifasi: Yangi obyekt yaratib, darhol saqlaydi.

# product = Product.objects.create(
#     product_name='New Product',
#     supplier_id=1,
#     category_id=1,
#     unit_price=25.00,
#     units_in_stock=50
# )
###################################################################################################################


###################################################################################################################
# get_or_create()
# Vazifasi: Topilsa qaytaradi, topilmasa yaratadi.

# product, created = Product.objects.get_or_create(
#     product_name='Chai',
#     defaults={
#         'unit_price': 18.00,
#         'units_in_stock': 39
#     }
# )
# if created:
#     print("Yangi yaratildi")
# else:
#     print("Mavjud edi")
###################################################################################################################


###################################################################################################################
# update_or_create()
# Vazifasi: Topilsa yangilaydi, topilmasa yaratadi.

# # update_or_create
# product, created = Product.objects.update_or_create(
#     product_id=1,
#     defaults={
#         'unit_price': 20.00,
#         'units_in_stock': 100
#     }
# )
###################################################################################################################


###################################################################################################################
# bulk_create()
# Vazifasi: Ko'p obyektlarni bir vaqtda yaratish (tezroq).

# # Bir nechta mahsulot yaratish
# products = [
#     Product(product_name='Product 1', unit_price=10),
#     Product(product_name='Product 2', unit_price=20),
#     Product(product_name='Product 3', unit_price=30),
# ]
# Product.objects.bulk_create(products)
###################################################################################################################


###################################################################################################################
# # bulk_update()
# # Vazifasi: Ko'p obyektlarni bir vaqtda yangilash.
#
# products = Product.objects.filter(category_id=1)
# for product in products:
#     product.unit_price += 10
#
# Product.objects.bulk_update(products, ['unit_price'])
###################################################################################################################


###################################################################################################################
# count()
# Vazifasi: Natijalar sonini qaytaradi.

# total_products = Product.objects.count()
###################################################################################################################


###################################################################################################################
# in_bulk()
# Vazifasi: Dictionary ko'rinishida qaytaradi (key sifatida field).

# # Primary key bo'yicha dictionary
# products = Product.objects.in_bulk()
###################################################################################################################


###################################################################################################################
# iterator()
# Vazifasi: Yozuvlarni birma-bir oladi, xotirani tejaydi.

# # Oddiy iteratsiya (barcha yozuvlarni xotiraga oladi)
# products = Product.objects.all()
# for product in products:  # Barcha yozuvlar xotirada
#     print(product.product_name)
#
# # iterator() bilan (xotirani tejaydi)
# products = Product.objects.all().iterator()
# for product in products:  # Har safar bitta yozuv
#     print(product.product_name)
###################################################################################################################


###################################################################################################################
# latest()
# Vazifasi: Eng oxirgi (eng yangi) yozuvni qaytaradi.

# latest_order = Order.objects.latest('order_date')
###################################################################################################################


###################################################################################################################
# earliest()
# Vazifasi: Eng birinchi (eng eski) yozuvni qaytaradi.

# first_order = Order.objects.earliest('order_date')
###################################################################################################################


###################################################################################################################
# first()
# Vazifasi: QuerySet dagi birinchi elementni qaytaradi yoki None.

# # Birinchi mahsulot
# product = Product.objects.first()
# # None qaytaradi agar bo'sh bo'lsa
###################################################################################################################


###################################################################################################################
# last()
# Vazifasi: QuerySet dagi oxirgi elementni qaytaradi yoki None.

# # Oxirgi mahsulot
# product = Product.objects.last()
###################################################################################################################


###################################################################################################################
# aggregate()
# Vazifasi: Barcha QuerySet uchun bitta natija qaytaradi (dictionary).

# from django.db.models import Avg, Count, Max, Min, Sum
#
# # O'rtacha narx
# avg_price = Product.objects.aggregate(Avg('unit_price'))
# # {'unit_price__avg': 28.87}
#
# # Bir nechta agregatsiya
# stats = Product.objects.aggregate(
#     avg_price=Avg('unit_price'),
#     max_price=Max('unit_price'),
#     min_price=Min('unit_price'),
#     total_products=Count('product_id')
# )
###################################################################################################################


###################################################################################################################
# annotate()
# Vazifasi: Har bir obyektga qo'shimcha maydon qo'shadi.

# # Har bir kategoriya uchun mahsulotlar soni
# categories = Category.objects.annotate(
#     product_count=Count('product')
# )
# for cat in categories:
#     print(f"{cat.category_name}: {cat.product_count}")

# # Farqi:
# # aggregate() - bitta natija (dictionary)
# result = Product.objects.aggregate(avg_price=Avg('unit_price'))
# # {'avg_price': 28.87}
#
# # annotate() - har bir obyekt uchun (QuerySet)
# products = Product.objects.annotate(avg_price=Avg('unit_price'))
# # QuerySet of Products, har birida avg_price mavjud
###################################################################################################################


###################################################################################################################
# exists()
# Vazifasi: Kamida bitta yozuv bormi, yo'qmi tekshiradi.

# has_products = Product.objects.exists()
###################################################################################################################


###################################################################################################################
# contains()
# Vazifasi: QuerySet ichida ma'lum obyekt bormi tekshiradi.

# products = Product.objects.filter(category_name__contains='A')
###################################################################################################################


###################################################################################################################
# update()
# Vazifasi: QuerySet dagi barcha yozuvlarni yangilaydi.

# # Oddiy update
# Product.objects.filter(category_id=1).update(unit_price=20)
#
# # Bir nechta maydonlar
# Product.objects.filter(discontinued=True).update(
#     units_in_stock=0,
#     units_on_order=0
# )
###################################################################################################################


###################################################################################################################
# delete()
# Vazifasi: QuerySet dagi barcha yozuvlarni o'chiradi.

# Product.objects.filter(discontinued=True).delete()
#
# # Barcha yozuvlarni o'chirish
# Product.objects.all().delete()
###################################################################################################################


###################################################################################################################
# as_manager()
# Vazifasi: QuerySet ni Manager ga aylantiradi.

# # Custom QuerySet
# class ProductQuerySet ( models.QuerySet ) :
#     def active(self) :
#         return self.filter ( discontinued=False )
#
#     def expensive(self) :
#         return self.filter ( unit_price__gte=50 )
#
#     def in_stock(self) :
#         return self.filter ( units_in_stock__gt=0 )
#
#
# # Model da Manager sifatida ishlatish
# class Product ( models.Model ) :
#     # ...
#     objects = ProductQuerySet.as_manager ()
#
#
# # Endi ishlatish
# active_products = Product.objects.active ()
# expensive_in_stock = Product.objects.expensive ().in_stock ()
#
#
# # Yoki Manager class yaratish
# class ProductManager ( models.Manager ) :
#     def get_queryset(self) :
#         return ProductQuerySet ( self.model, using=self._db )
#
#     def active(self) :
#         return self.get_queryset ().active ()
#
#
# class Product ( models.Model ) :
#     # ...
#     objects = ProductManager ()
#
# # Ikkalasi ham bir xil natija beradi
###################################################################################################################


###################################################################################################################
# explain()
# Vazifasi: SQL query execution plan ni ko'rsatadi.

# print(Product.objects.all().explain())
#
# # PostgreSQL bilan
# print(Product.objects.filter(unit_price__gt=50).explain(verbose=True))
###################################################################################################################


###################################################################################################################
# exact ( aniq tenglik )

# product = Product.objects.get(product_name__exact='Chai')
###################################################################################################################


###################################################################################################################
# iexact (case-insensitive tenglik)

# product = Product.objects.get(product_name__iexact='chai')  # topiladi
# product = Product.objects.get(product_name__iexact='CHAI')  # topiladi
# product = Product.objects.get(product_name__iexact='Chai')  # topiladi
###################################################################################################################


###################################################################################################################
# contains (ichida bor, case-sensitive)

# products = Product.objects.filter(product_name__contains='Ch')
# # Chai, Chang, Chocolate, topiladi
# # chai, chang topilmaydi (case-sensitive)
#
# customers = Customer.objects.filter(city__contains='on')
# # London, Boston topiladi
###################################################################################################################


###################################################################################################################
# icontains (ichida bor, case-insensitive)

# products = Product.objects.filter(product_name__icontains='ch')
# # Chai, Chang, Chocolate, chai, CHANG topiladi
###################################################################################################################


###################################################################################################################
# in (ro'yxatda bor)

# # ID lar ro'yxatida
# products = Product.objects.filter(product_id__in=[1, 2, 3, 4, 5])
###################################################################################################################


###################################################################################################################
# gt (greater than - katta)

# # Narxi 50 dan katta
# expensive = Product.objects.filter(unit_price__gt=50)
###################################################################################################################


###################################################################################################################
# gte (greater than or equal - katta yoki teng)

# # Narxi 50 va undan katta
# products = Product.objects.filter(unit_price__gte=50)
###################################################################################################################


###################################################################################################################
# lt (less than - kichik)

# # Narxi 20 dan kichik
# cheap = Product.objects.filter(unit_price__lt=20)
###################################################################################################################


###################################################################################################################
# lte (less than or equal - kichik yoki teng)

# # Narxi 20 va undan kichik
# affordable = Product.objects.filter(unit_price__lte=20)
###################################################################################################################


###################################################################################################################
# range (oralig'ida)

# # Narxi 10 va 50 oralig'ida (inclusive)
# mid_price = Product.objects.filter(unit_price__range=(10, 50))
# # SQL: WHERE unit_price BETWEEN 10 AND 50
###################################################################################################################


###################################################################################################################
# startswith (bilan boshlanadi, case-sensitive)

# # 'Ch' bilan boshlanadigan mahsulotlar
# products = Product.objects.filter(product_name__startswith='Ch')
# # Chai, Chang, Chocolate
###################################################################################################################


###################################################################################################################
# istartswith (bilan boshlanadi, case-insensitive)

# # Katta-kichik harfga qaramaydi
# products = Product.objects.filter(product_name__istartswith='ch')
# # Chai, Chang, CHOCOLATE, chai
###################################################################################################################


###################################################################################################################
# endswith (bilan tugaydi, case-sensitive)

# # 'Ltd' bilan tugaydigan kompaniyalar
# customers = Customer.objects.filter(company_name__endswith='Ltd')
###################################################################################################################


###################################################################################################################
# iendswith (bilan tugaydi, case-insensitive)

# # Katta-kichik harfga qaramaydi
# customers = Customer.objects.filter(company_name__iendswith='ltd')
# # 'Ltd', 'LTD', 'ltd'
###################################################################################################################


###################################################################################################################
# date (sana qismi)

# # Ma'lum sanada
# from datetime import date
# orders = Order.objects.filter(order_date__date=date(1997, 7, 4))
###################################################################################################################


###################################################################################################################
# year (yil)

# # 1997 yildagi buyurtmalar
# orders_1997 = Order.objects.filter(order_date__year=1997)
###################################################################################################################


###################################################################################################################
# month (oy)

# # Yanvar oyidagi buyurtmalar
# january_orders = Order.objects.filter(order_date__month=1)
#
# # Dekabr oyi
# december_orders = Order.objects.filter(order_date__month=12)
###################################################################################################################


###################################################################################################################
# day (kun)

# # Oyning 1-kunidagi buyurtmalar
# first_day = Order.objects.filter(order_date__day=1)
#
# # 15-kun
# mid_month = Order.objects.filter(order_date__day=15)
###################################################################################################################


###################################################################################################################
# week (hafta raqami)

# # Yilning 1-haftasi
# week_1 = Order.objects.filter(order_date__week=1)
###################################################################################################################


###################################################################################################################
# week_day (hafta kuni, 1=Yakshanba)

# # Yakshanba kunlari (1)
# sunday_orders = Order.objects.filter(order_date__week_day=1)
#
# # Dushanba (2)
# monday_orders = Order.objects.filter(order_date__week_day=2)
###################################################################################################################


###################################################################################################################
# iso_week_day (ISO hafta kuni, 1=Dushanba)

# # Dushanba (1)
# monday = Order.objects.filter(order_date__iso_week_day=1)
#
# # Juma (5)
# friday = Order.objects.filter(order_date__iso_week_day=5)
###################################################################################################################


###################################################################################################################
# quarter (chorak)

# # Birinchi chorak (Yanvar-Mart)
# q1_orders = Order.objects.filter(order_date__quarter=1)
#
# # Ikkinchi chorak (Aprel-Iyun)
# q2_orders = Order.objects.filter(order_date__quarter=2)
###################################################################################################################


###################################################################################################################
# time (vaqt qismi)

# from datetime import time
#
# # Soat 10:00 da
# orders = Order.objects.filter(order_date__time=time(10, 0))
#
# # Soat 9:00 dan 17:00 gacha (ish vaqti)
# orders = Order.objects.filter(
#     order_date__time__range=(time(9, 0), time(17, 0))
# )
###################################################################################################################


###################################################################################################################
# hour (soat)

# # Soat 10 da
# orders = Order.objects.filter(order_date__hour=10)
###################################################################################################################


###################################################################################################################
# minute (daqiqa)

# # Aniq daqiqada
# orders = Order.objects.filter(
#     order_date__hour=10,
#     order_date__minute=30
# )
#
# # Daqiqa oralig'i
# orders = Order.objects.filter(
#     order_date__minute__range=(0, 15)  # 00-15 daqiqa
###################################################################################################################


###################################################################################################################
# second (soniya)

# # Aniq soniyada
# orders = Order.objects.filter(
#     order_date__hour=10,
#     order_date__minute=30,
#     order_date__second=45
# )
###################################################################################################################


###################################################################################################################
# isnull (NULL tekshirish)

# # NULL bo'lgan mahsulotlar
# no_supplier = Product.objects.filter(supplier_id__isnull=True)
#
# # NULL bo'lmagan mahsulotlar
# has_supplier = Product.objects.filter(supplier_id__isnull=False)
###################################################################################################################


###################################################################################################################
# regex (Regular expression, case-sensitive)

# # Email validatsiya
# valid_emails = Customer.objects.filter(
#     contact_name__regex=r'^[\w\.-]+@[\w\.-]+\.\w+$'
# )
###################################################################################################################


###################################################################################################################
# iregex (Regular expression, case-insensitive)

# # Case-insensitive email
# emails = Customer.objects.filter(
#     contact_name__iregex=r'^[\w\.-]+@gmail\.com$'
# )
# # 'user@gmail.com', 'USER@GMAIL.COM' ikkalasi ham
###################################################################################################################


###################################################################################################################
# Avg (O'rtacha)

# from django.db.models import Avg
#
# # Barcha mahsulotlarning o'rtacha narxi
# avg_price = Product.objects.aggregate(Avg('unit_price'))
###################################################################################################################


###################################################################################################################
# Count (Sanash)

# from django.db.models import Count
#
# # Jami mahsulotlar soni
# total = Product.objects.count()
#
# # Aggregate bilan
# result = Product.objects.aggregate(total=Count('product_id'))
###################################################################################################################


###################################################################################################################
# Max (Maksimal)

# from django.db.models import Max
#
# # Eng qimmat mahsulot narxi
# max_price = Product.objects.aggregate(Max('unit_price'))
# # {'unit_price__max': 263.50}
#
# # Har bir kategoriya uchun eng qimmat mahsulot
# categories = Category.objects.annotate(
#     max_price=Max('product__unit_price')
# )
###################################################################################################################


###################################################################################################################
# Min (Minimal)

# from django.db.models import Min
#
# # Eng arzon mahsulot
# min_price = Product.objects.aggregate(Min('unit_price'))
# # {'unit_price__min': 2.50}
#
# # Har bir kategoriya uchun eng arzon
# categories = Category.objects.annotate(
#     min_price=Min('product__unit_price')
# )
###################################################################################################################


###################################################################################################################
# Sum (Yig'indi)

# from django.db.models import Sum, F
#
# # Umumiy ombor qiymati
# total_value = Product.objects.aggregate(
#     total=Sum(F('unit_price') * F('units_in_stock'))
# )
###################################################################################################################


###################################################################################################################
# StdDev (Standart og'ish)'

# from django.db.models import StdDev
#
# # Narxlarning standart og'ishi
# price_stddev = Product.objects.aggregate(
#     stddev=StdDev('unit_price')
# )
###################################################################################################################


###################################################################################################################
# Variance (Dispersiya)

# from django.db.models import Variance
#
# # Narxlarning dispersiyasi
# price_var = Product.objects.aggregate(
#     variance=Variance('unit_price')
# )
###################################################################################################################


###################################################################################################################
# Q() asoslari

# from django.db.models import Q
#
# # Oddiy OR
# products = Product.objects.filter(
#     Q(unit_price__lt=10) | Q(unit_price__gt=100)
# )
#
# # AND (default)
# products = Product.objects.filter(
#     Q(unit_price__gte=20) & Q(units_in_stock__gt=0)
# )
# # Yoki oddiy:
# products = Product.objects.filter(
#     unit_price__gte=20,
#     units_in_stock__gt=0
# )
#
# # NOT
# products = Product.objects.filter(
#     ~Q(discontinued=True)
# )
###################################################################################################################