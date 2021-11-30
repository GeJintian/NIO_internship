import pytest
import json

@pytest.fixture(scope='class')
def setup_class(request):
    position=request.config.getoption("--position")
    tester=request.config.getoption("--tester")
    thresh=request.config.getoption("--thresh")
    thresh=float(thresh)
    dir ='/home/jenkins/eol_pytest_test/dataset/camera'
    tester=tester.split('.')[0]
    with open(dir+'/result/'+position+'/'+tester+'.bmp.json','r',encoding='utf8')as f:
        test=json.load(f)
    with open(dir+'/gt/'+position+'/'+tester+'.json','r',encoding='utf8')as f:
        standard=json.load(f)
    return test, standard,thresh


class TestSimple:
    #dir = "/home/jenkins/eol_pytest_test/dataset"
    def test_rotate_x(self,setup_class):
        test,standard,thresh=setup_class
        assert abs(test['extrinsic_param']['rotation'][0]-standard['extrinsic_param']['rotation'][0]) < thresh
    def test_rotate_y(self,setup_class):
        test,standard,thresh=setup_class
        assert abs(test['extrinsic_param']['rotation'][1]-standard['extrinsic_param']['rotation'][1]) < thresh
    def test_rotate_z(self,setup_class):
        test,standard,thresh=setup_class
        assert abs(test['extrinsic_param']['rotation'][2]-standard['extrinsic_param']['rotation'][2]) < thresh
    def test_trans_x(self,setup_class):
        test,standard,thresh=setup_class
        assert abs(test['extrinsic_param']['translation'][0]-standard['extrinsic_param']['translation'][0]) < thresh
    def test_trans_y(self,setup_class):
        test,standard,thresh=setup_class
        assert abs(test['extrinsic_param']['translation'][0]-standard['extrinsic_param']['translation'][0]) < thresh
    def test_trans_z(self,setup_class):
        test,standard,thresh=setup_class
        assert abs(test['extrinsic_param']['translation'][0]-standard['extrinsic_param']['translation'][0]) < thresh