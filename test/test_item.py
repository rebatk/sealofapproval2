from __future__ import print_function
from src import item
import nose.tools as ns


class TestItem:
    """Test class for Item class."""

    @classmethod
    def setup_class(cls):
        """Run once for each class before any tests are run."""
        print('setup_class')
        pass

    @classmethod
    def teardown_class(cls):
        """Run once for each class after all tests are run."""
        print('teardown_class')
        pass

    def setUp(self):
        """Run once before each test method is executed."""
        print('setUp method')
        pass

    def tearDown(self):
        """Run once after each test method is executed."""
        print('tearDown method')
        pass

    # TEST METHODS:
    def test_get_title(self):
        print('Test get_title() method')
        myItem = item.Item(1, 'The Title')
        ns.assert_equals('The Title', myItem.get_title())
        pass

    def test_get_identifier(self):
        print('Test get_identifier() method')
        myItem = item.Item(12, 'The Title')
        ns.assert_equals(12, myItem.get_identifier())
        pass

    def test_get_fine_due(self):
        print('Test get_fine_due() method')
        myBook = item.Book(14, 'My Book')
        ns.assert_equals(0.0, myBook.get_fine_due())
        pass


    @ns.raises(TypeError)
    def test_set_checkoute(self):
        print('Test_set_checkout() method')
        myItem = item.Item(1, 'The Title')
        myItem.set_checkout('01/01/2018')
        pass
