from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError
from lists.forms import (DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR,
                         ExistingListItemForm, ItemForm)
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


class ExistingListItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())


    def test_form_validation_for_blank_items(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])


    def test_form_validation_for_duplicate_items(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='no twins!')
        form = ExistingListItemForm(for_list=list_, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])