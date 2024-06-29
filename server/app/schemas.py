from app import ma, db
from .models import Category, Course, Tag, Lesson, User, Order, OrderDetail
from marshmallow import post_load, fields


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        fields = ['name']


class CourseBaseSchema(ma.SQLAlchemyAutoSchema):
    category = fields.Function(lambda obj: obj.category.name if obj.category else None)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'category']


class CourseSchema(CourseBaseSchema):
    class Meta:
        model = CourseBaseSchema.Meta.model
        fields = CourseBaseSchema.Meta.fields + ['price', 'date_created']


class CourseDetailSchema(CourseSchema):
    tags = ma.List(ma.Nested(TagSchema))

    class Meta:
        model = CourseSchema.Meta.model
        fields = CourseSchema.Meta.fields + ['description', 'tags']


class OrderDetailSchema(ma.SQLAlchemyAutoSchema):
    course = ma.Nested(CourseBaseSchema)    
    class Meta:
        model = OrderDetail
        fields = ['order_id', 'course', 'unit_price', 'quantity']


class OrderSchema(ma.SQLAlchemyAutoSchema):
    total_price = fields.Method('sum_price')
    details = ma.List(ma.Nested(OrderDetailSchema))
    
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'active', 'details', 'date_created']
    
    def sum_price(self, obj):
        total_price = 0.0
        for detail in obj.details:
            total_price += detail.unit_price * detail.quantity
        return total_price
    

class LessonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'date_created']


class LessonDetailSchema(LessonSchema):
    tags = ma.List(ma.Nested(TagSchema))

    class Meta:
        model = LessonSchema.Meta.model
        fields = LessonSchema.Meta.fields + ['content', 'tags']


class UserSchema(ma.SQLAlchemyAutoSchema):
    password = fields.Str(load_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'username', 'password', 'avatar']

    @post_load
    def make_user(self, data, **kwargs):
        user = User(**data)
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()
        return user


class EnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return value.name


class CurrentUserSchema(UserSchema):
    role = EnumField(attribute="role")

    class Meta:
        model = UserSchema.Meta.model
        fields = UserSchema.Meta.fields + ['phone', 'role']
