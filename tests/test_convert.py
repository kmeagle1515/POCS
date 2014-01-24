from panoptes.utils import Convert

import datetime
import ephem

class TestConvert: 

    mount = None

    def setup(self):
        print ("TestConvert:setup() before each test method")
 
    def teardown(self):
        print ("TestConvert:teardown() after each test method")
 
    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")
        cls.convert = Convert()
 
    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")

    def test_HA_to_Dec(self):

        MaunaLoa = ephem.Observer()
        MaunaLoa.lon = '-155:34:33.90'
        MaunaLoa.lat = '19:32:09.66'
        MaunaLoa.elevation = 3400.
        now = datetime.datetime.now()
        MaunaLoa.date = now.strftime("%Y/%m/%d %H:%M:%S")

        J2000_coordinate = coords.FK5('00h42m44.3s +41d16m9s')
        Jnow_coordinate = J2000_coordinate.precess_to(Time.now())
        print('Astropy J2000: {}'.format(J2000_coordinate.to_string(precision=2, sep=':')))
        print('Astropy Jnow:  {}'.format(Jnow_coordinate.to_string(precision=2, sep=':')))
        HA = convert_to_HADec(J2000_coordinate, MaunaLoa)
        print('HA decimal = {:f}'.format(HA))
