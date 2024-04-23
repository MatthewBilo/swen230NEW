import pytest
from peewee import SqliteDatabase, Model, CharField, TextField, ForeignKeyField
from util.fileStorage import User, EncryptedData, register_user, check_credentials, update_password, clear_user, save_encrypted_data, get_encrypted_data, delete_encrypted_data


db = SqliteDatabase(':memory:')

def setup_function():
    db.bind([User, EncryptedData])
    db.create_tables([User, EncryptedData])

def teardown_function():
    db.drop_tables([User, EncryptedData])

def test_register_user_true():
    assert register_user('testuser', 'testpass', 'testkey') == True

def test_register_user_false():
    register_user('testuser', 'testpass', 'testkey')
    assert register_user('testuser', 'testpass', 'testkey') == False   

def test_check_credentials_true():
    register_user('testuser', 'testpass', 'testkey')
    assert check_credentials('testuser', 'testpass') == (True, None)
    assert check_credentials('wronguser', 'testpass') == (False, "Wrong username")

def test_check_credentials_false():
    register_user('testuser', 'testpass', 'testkey')
    assert check_credentials('wronguser', 'testpass') == (False, "Wrong username")

def test_update_password_true():
    register_user('testuser', 'testpass', 'testkey')
    update_password('testuser', 'newpass')
    assert check_credentials('testuser', 'newpass') == (True, None)

def test_update_password_false():
    register_user('testuser', 'testpass', 'testkey')
    update_password('wronguser', 'newpass')
    assert check_credentials('wronguser', 'newpass') == (False, "Wrong username")

def test_clear_user_true():
    register_user('testuser', 'testpass', 'testkey')
    clear_user('testuser')
    assert check_credentials('testuser', 'testpass') == (False, "Wrong username")

def test_clear_user_false():
    register_user('testuser', 'testpass', 'testkey')
    clear_user('wronguser')
    assert check_credentials('testuser', 'testpass') == (True, None)

def test_save_encrypted_data_true():
    register_user('testuser', 'testpass', 'testkey')
    save_encrypted_data('testuser', 'testtag', 'testtext')
    assert len(get_encrypted_data('testuser')) == 1
    save_encrypted_data('wronguser', 'testtag', 'testtext')
    assert len(get_encrypted_data('wronguser')) == 0

def test_save_encrypted_dat_false():
    register_user('testuser', 'testpass', 'testkey')
    save_encrypted_data('testuser', 'testtag', 'testtext')
    save_encrypted_data('wronguser', 'testtag', 'testtext')
    assert len(get_encrypted_data('wronguser')) == 0

def test_get_encrypted_data_true():
    register_user('testuser', 'testpass', 'testkey')
    save_encrypted_data('testuser', 'testtag', 'testtext')
    assert len(get_encrypted_data('testuser')) == 1
    assert len(get_encrypted_data('wronguser')) == 0

def test_get_encrypted_data_false():
    register_user('testuser', 'testpass', 'testkey')
    save_encrypted_data('testuser', 'testtag', 'testtext')
    assert len(get_encrypted_data('wronguser')) == 0

def test_delete_encrypted_data_true():
    register_user('testuser', 'testpass', 'testkey')
    save_encrypted_data('testuser', 'testtag', 'testtext')
    encrypted_data = get_encrypted_data('testuser')
    delete_encrypted_data('testuser', encrypted_data[0].id)
    assert len(get_encrypted_data('testuser')) == 0
    delete_encrypted_data('wronguser', 1)
    assert len(get_encrypted_data('wronguser')) == 0

def test_delete_encrypted_data_false():
    register_user('testuser', 'testpass', 'testkey')
    save_encrypted_data('testuser', 'testtag', 'testtext')
    delete_encrypted_data('wronguser', 1)
    assert len(get_encrypted_data('wronguser')) == 0
    assert len(get_encrypted_data('testuser')) == 1

