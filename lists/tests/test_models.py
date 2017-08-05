from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError
# Create your tests here.

class ItemModelTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')


class ListModelTest(TestCase):
    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())


class ListAndItemModelTest(TestCase):

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

        # try:
        #     item.save()
        #     self.fail('xxx')
        #     # text = models.TextField(default='', blank=True)后顺利通过try函数
        # except ValidationError:
        #     pass


    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id))