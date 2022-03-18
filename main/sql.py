
# операции над столбцами
# SELECT, INSERT, UPDATE, DELETE

# SELECT*FROM product;
# Product.objects.all()

#Select id, name from product;
# Product.objects.only('id', 'name')

# Product.objects.defer('id','name')
"""
select * from product where price>50000;
Product.objects.filter(price__gt=50000)

select * from product where price=50000;
Product.objects.filter(price=50000)

select * from product where price<50000;
Product.objects.filter(price__lt=50000)

select * from product where price!=50000;
Product.objects.exclude(price=50000)
or
Product.objects.filter(~Q(price=50000)

select * from product where price<=50000;
Product.objects.filter(price__lte=50000)

select * from product where price>=50000;
Product.objects.filter(price__gte=50000)

select*from product where price between 50000 and 60000;
Product.objects.filter(price__range=[50000, 60000])

Select* from product where price >=50000 and price <=60000;
Product.objects.filter(price__gte=50000).filter(price__lte=60000)
но правильнее делать так
Product.objects.filter(price__gte=50000, price__lte=60000)

select * from product where category_id IN ('smatrphones', 'accessories')
Product.objects.filter(category_id__in=[])

select * from product where category_id ='smatrphones', or category_id = 'accessories'
Product.objects.filter(Q(category_id='smartphones'))|Q(category_id = 'accessories'))

LIKE
ILIKE

select * from product where name like 'Samsung%';
Product.objects.filter(name__startswith='Samsung')

select * from product where name ilike 'Samsung%';
Product.objects.filter(name__istartswith='Samsung')

select * from product where name ilike '%Samsung';
Product.objects.filter(name__iendswith='Samsung')

select * from product where name ilike '%Samsung%';
Product.objects.filter(name__icontains='Samsung')

select * from product where name ilike 'Samsung';
Product.objects.filter(name__iexact='Samsung')

ORDER_BY
select* from product order by price asc;
Product.objects.order_by('price')


select * from product order by price desc;
Product.objects.order_by('~price')

COUNT

select count(*) from product;
Product.objects.count()

select count(*) from product where category_id='smartphones';
Product.objects.filter(category_id=;smartphones').count()

#INSERT
insert into product(...) values(...);
Product.objects.create(name = '', description = '', price= '', category = '')
product = Product(...)
product.save()

insert into product(...) values(...), (...), (...);
Product.objects.bulk_create([
Product(name = '', description = '', price= '', category = ''),
Product(name = '', description = '', price= '', category = ''),
Product(name = '', description = '', price= '', category = '')
])


#UPDATE
update product set price = price - 5000;
Product.objects.update(price=F(price)-5000)

update product set price = price - 4000 where price>50000;
Product.objects.filter(price__gt=50000).update(price=F(price)-4000)


update product set price = 51000 where id-2;
Product.objects.filter('id'=2).update(price=51000)
product = Product.objects.get(id=2)
product.price = 51000
product.save()

#DELETE
delete * from product;
Product.objects.delete()

delete from product where category_id='accessories';
Product.objects.filter(category_id='accessories')

delete from product where id=2;
Product.objects.filter(id=2).delete()

product = Product.objects.get(id=2)
product.delete()


"""
