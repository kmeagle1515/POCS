import os.path
from astropy.utils import data
from astroplan import download_IERS_A


def download_all_files():
    download_IERS_A()

    for i in range(4214, 4219):
        fn = 'index-{}.fits'.format(i)
        data_folder = "/var/panoptes/astrometry/data"
        dest = "{}/{}".format(data_folder, fn)

        if not os.path.exists(dest):
            url = "http://data.astrometry.net/4200/{}".format(fn)
            df = data.download_file(url)
            os.rename(df, dest)


if __name__ == '__main__':
    download_all_files()