from django.db import models


from django.db import models
import uuid

# Create your models here.


class Banner(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    image = models.ImageField(upload_to='banner', null=True, blank=True)


'''class Faq(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    faq_question = models.CharField(max_length=400, null=True, blank=True)
    faq_answer = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.faq_question'''


class Category(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        upload_to='category_image',  null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='brand_image',  null=True, blank=True)
    category = models.ForeignKey(
        Category,  on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=200, null=True, blank=True)

    ram_choice = [

        ('64', 'R1'), ('128', 'R2'), ('512', 'R3')]
    ram = models.CharField(
        max_length=5, choices=ram_choice, null=True, blank=True)
    image = models.ImageField(upload_to='p_img', null=True, blank=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
   # countInStock = models.IntegerField(default=0, null=True, blank=True)
    #numReviews = models.IntegerField(null=True, blank=True)
    #ratings = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class QuestionCategory(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(
        max_length=200, null=True, blank=True)

    title = models.CharField(
        max_length=200, null=True, blank=True)

    description = models.TextField(
        null=True, blank=True)

    products = models.ManyToManyField(
        Products, null=True, blank=True, related_name='questionscategory')

    def __str__(self) -> str:
        return self.name


class Question (models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    questioncategory = models.ForeignKey(
        QuestionCategory, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)

    question_title = models.CharField(max_length=300, null=True, blank=True)
    question_heading = models.CharField(max_length=300, null=True, blank=True)
    question_subheading = models.CharField(
        max_length=300, null=True, blank=True)

    image = models.ImageField(upload_to='q_image', null=True, blank=True)

    question_category = models.CharField(max_length=200, null=True, blank=True)

    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)

    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    is_checked = models.BooleanField(default=False, null=True, blank=True)

    deduct_amount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.question_title


class Answer (models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    # question = models.ForeignKey(
    # Products, on_delete=models.CASCADE, null=True, blank=True)

    user_answer = models.CharField(max_length=200,  null=True, blank=True)


class ScoreBoard(models.Model):
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name='scoreboard', null=True, blank=True)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    total_deduction = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.total_deduction)


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    order_amount = models.IntegerField(null=True, blank=True)
   # shipping = models.IntegerField(null=True, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_amount)


class OrderItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items', null=True, blank=True)

    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, null=True, blank=True)
    houseno = models.CharField(max_length=200, null=True, blank=True)
    landmark = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=200, null=True, blank=True)
    alternateno = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.landmark)
