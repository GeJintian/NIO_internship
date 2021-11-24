import pytest
import json
from pytest import approx

@pytest.fixture(scope='class')
def setup_class(request):
    tester=request.config.getoption("--tester")
    dir ='/home/jenkins/eol_pytest_test/dataset/lidar'
    tester=tester.split('.')[0]
    with open(dir+'/result/'+tester+'.pcd.json','r',encoding='utf8')as f:
        test=json.load(f)
    with open(dir+'/gt/'+tester+'.json','r',encoding='utf8')as f:
        standard=json.load(f)
    return test, standard


class TestSimple:
    #dir = "/home/jenkins/eol_pytest_test/dataset"
    def test_rotate_x(self,setup_class):
        test,standard=setup_class
        assert abs(test['extrinsic_param']['rotation'][0]-standard['extrinsic_param']['rotation'][0]) == approx(0)
    def test_rotate_y(self,setup_class):
        test,standard=setup_class
        assert abs(test['extrinsic_param']['rotation'][1]-standard['extrinsic_param']['rotation'][1]) == approx(0)
    def test_rotate_z(self,setup_class):
        test,standard=setup_class
        assert abs(test['extrinsic_param']['rotation'][2]-standard['extrinsic_param']['rotation'][2]) == approx(0)
    def test_trans_x(self,setup_class):
        test,standard=setup_class
        assert abs(test['extrinsic_param']['translation'][0]-standard['extrinsic_param']['translation'][0]) == approx(0)
    def test_trans_y(self,setup_class):
        test,standard=setup_class
        assert abs(test['extrinsic_param']['translation'][0]-standard['extrinsic_param']['translation'][0]) == approx(0)
    def test_trans_z(self,setup_class):
        test,standard=setup_class
        assert abs(test['extrinsic_param']['translation'][0]-standard['extrinsic_param']['translation'][0]) == approx(0)