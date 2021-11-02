#!/usr/bin/env python
import cdsapi
import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"y:m:v:",["year=","month=","variable="])
    except getopt.GetoptError:
        print('wrong arguments')
        sys.exit(2)
    for opt, arg in opts:
        if opt in("-y", "--year"):
            year = arg
        elif opt in ("-m", "--month"):
            month = arg
        elif opt in ("-v", "--variable"):
            variable = arg
    c = cdsapi.Client()
    print(variable)
    print(year)
    print(month)

    c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'format': 'netcdf',
                'variable': variable,
                'year': year,
                'month': month,
                'day': [
                    '01', '02', '03', '04',
                    '05', '06', '07',
                    '08', '09', '10',
                    '11', '12', '13',
                    '14', '15', '16',
                    '17', '18', '19',
                    '20', '21', '22',
                    '23', '24', '25',
                    '26', '27', '28',
                    '29', '30', '31',
                    ],
                'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',
                    ],
                'area': [
                    75, -85, 25,
                    75,
                    ],
                },
            't2m.nc'
            )


if __name__ == "__main__":
    main(sys.argv[1:])
